import numpy as np
import cv2
from matplotlib import pyplot as plt

#try convoluting with 2-step unsharp mask sharpening filter, better diy convolve function, and reflect edge method
def filter_2d(data, kernel, output_divide):
    #return output data from given input image data and filter kernel
    output = np.zeros(data.shape, dtype=np.int16)
    kernel_half = (kernel.shape[0] - 1) // 2 #border thickness depends on kernel size
    padded_data = reflect_border(data, kernel_half)
    rows, columns = padded_data.shape
    
    for row in range(kernel_half, rows - kernel_half):
        for col in range(kernel_half, columns - kernel_half):
            local_slice = padded_data[row - kernel_half:row + kernel_half + 1, col - kernel_half:col + kernel_half + 1]
            value = local_slice * kernel
            output[row-1, col-1] = value.sum() // output_divide
            
    return output

def reflect_border(image, border_thickness):
    #return padded image data
    #reflected border
    reflected_edges = image[:, :border_thickness][:, ::-1], image[:, -border_thickness:][:, ::-1]
    image_reflected = np.concatenate([reflected_edges[0], image, reflected_edges[1]], axis=1)
    reflected_edges = image_reflected[:border_thickness, :][::-1, :], image_reflected[-border_thickness:, :][::-1]
    image_reflected = np.concatenate([reflected_edges[0], image_reflected, reflected_edges[1]], axis=0)
    
    return image_reflected

def unsharp_mask(image_data):
    #original filtered with [[0, 0, 0], [0, 2, 0], [0, 0, 0]]
    #minus original filtered with box filter [[1, 1, 1], [1, 1, 1], [1, 1, 1]] / 9
    intensify_filter = np.array([[0, 0, 0], [0, 2, 0], [0, 0, 0]], dtype=np.int8)
    box_filter = np.ones_like(intensify_filter)
    
    sharpened = filter_2d(image_data, intensify_filter, 1) - filter_2d(image_data, box_filter, 9)
    return sharpened

#------------------------------------------------------------------------------------
#reproduction of Find Best Match Quiz
def find_best_match(patch, strip):
    #find patch in strip and return x column index of top-left corner
    
    ssd_array = get_ssd_along_strip(patch, strip)
    possible_x = np.where(ssd_array == min(ssd_array))
    return possible_x

def sum_sq_dif(image_a, image_b):
    diff = image_a - image_b
    diff_sq = diff**2
    return np.sum(diff_sq)
    
def get_ssd_along_strip(patch, strip):
    strip_ssd = []
    strip_length = strip.shape[1]
    window_size = patch.shape[1]
    for column in range(1, strip_length - window_size):
        strip_portion = strip[:, column:(column + window_size)]
        ssd = sum_sq_dif(patch, strip_portion)
        strip_ssd.append(ssd)
    return strip_ssd

#load images
left = cv2.imread('left.png', cv2.IMREAD_GRAYSCALE)
right = cv2.imread('right.png', cv2.IMREAD_GRAYSCALE)

#define image patch location
patch_loc = [120, 170] #row, column
patch_size = [100, 100]

#extract patch from left stereo image
rows = patch_loc[0], patch_loc[0] + patch_size[0]
cols = patch_loc[1], patch_loc[1] + patch_size[1]
patch_left = left[rows[0]:rows[1], cols[0]:cols[1]]

#extract strip from right stereo image
strip_right = right[rows[0]:rows[1], :]

#look for the patch in the strip and report the likely starting x position
matching_x = find_best_match(patch_left, strip_right)
best_x = int(matching_x[0])
print(f'Best found at {matching_x[0]}')

#get corresponding patch from right image
patch_right = right[rows[0]:rows[1], best_x:best_x + patch_size[1]]
