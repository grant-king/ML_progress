"""
Find the maximum product of two distinct numbers in a sequence of (positive) integers.

input: a sequence of positive integers

output: the maximum value that can be obtained by multiplying two different elements from the sequence

Approach: Iterate through all possible pairs of input elements and find the pair with the largest product.
"""
import sys

def mpp(sequence):
    products = []
    for idx in range(len(sequence)):
        for other_idx in range(idx + 1, len(sequence)):
            products.append(sequence[idx] * sequence[other_idx])
    return max(products)

if __name__ == '__main__':
    print(f'\n----- Running {sys.argv[0]} -----\n')
    sequence = [int(item.strip(',')) for item in input("Enter sequence: ").split()]
    print(f'Maximum pairwise product for sequence: {mpp(sequence)}')
