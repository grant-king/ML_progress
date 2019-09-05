
def list_get_number(number_idx):
    #generate Fibonacci sequence up to desired number, returnn number
    sequence = [1, 1]
    for idx in range(number_idx - 2):
        sequence.append(sequence[idx] + sequence[idx + 1])
    return sequence[-1]

    