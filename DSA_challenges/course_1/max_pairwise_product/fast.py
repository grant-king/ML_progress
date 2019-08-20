"""
Find the maximum product of two distinct numbers in a sequence of (positive) integers.

input: a sequence of positive integers

output: the maximum value that can be obtained by multiplying two different elements from the sequence

Approach: Find largest two items in sequence, multiply and return
"""
import sys

def mpp(sequence):
    big1 = sequence.pop(sequence.index(max(sequence)))
    big2 = sequence.pop(sequence.index(max(sequence)))
    return big1 * big2

if __name__ == '__main__':
    print(f'\n----- Running {sys.argv[0]} -----\n')
    sequence = [int(item.strip(',')) for item in input("Enter sequence: ").split()]
    print(f'Maximum pairwise product for sequence: {mpp(sequence)}')