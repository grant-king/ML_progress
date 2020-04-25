import cv2
import numpy as np
from numba import cuda
import math

def to_grayscale(color_img):
    grayscale = np.zeros((color_img.shape[0], color_img.shape[1]), dtype=np.float32)

    # We use blocks of 32x32 pixels:
    blockdim = (32, 32)
    # We compute grid dimensions big enough to cover the whole image:
    griddim = (color_img.shape[0] // blockdim[0] + 1, color_img.shape[1] // blockdim[1] + 1)
    print('Grid dimensions:', griddim)

    rgb_to_intensity[griddim, blockdim](color_img, grayscale)
    
    return grayscale

@cuda.jit
def rgb_to_intensity(color_img_array, output_array):
    #convert height x witdth x 3 input to height x width x 1 output
    threadx, thready = cuda.grid(2)
    blue, green, red = color_img_array[thready][threadx]
    #convert rgb to single intensity value for grayscale, according to NTSC rec's
    intensity = 0.299 * red + 0.587 * green + 0.114 * blue
    output_array[thready][threadx] = intensity

if __name__ == '__main__':
    image = cv2.imread('color.jpg')
    grayscale = to_grayscale(image)
    grayscale = np.array(grayscale, dtype=np.uint8)
    cv2.imshow('image', grayscale)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
