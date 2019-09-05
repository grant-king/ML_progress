"""
Determine the nth number of the Fibonacci sequence.

input: a positive integer indicating the position of the desired value

output: value of the item in the sequence at position indicated by input

approach: Count to the desired position by recursively summing up to each element. 
    Quickly overwhelming to memory and CPU. Input < 20 to stay under a second.
"""

def recursive_get_number(number_idx):
    if number_idx <= 1:
        return number_idx
    else:
        return recursive_get_number(number_idx - 1) + recursive_get_number(number_idx - 2)
        