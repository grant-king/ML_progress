def fast_get_number(number_idx):
    #return nth Fibonacci number at index
    term1 = power((1 + math.sqrt(5) / 2), number_idx)
    term2 = power((1 - math.sqrt(5) / 2), number_idx)
    term = term1 - term2
    
    number = (1 / math.sqrt(5)) * (term)
    return number
    
def multiply(x, array_number):
    carry = 0
    
    for idx, digit in enumerate(array_number):
        product = digit * x + carry
        array_number[idx] = product % 10
        carry = product // 10
        
    while carry:
        array_number.append(carry % 10)
        carry = carry // 10
        
    return array_number

def power(x, exponent):
    big_number_array = []
    number = x
    
    while(x):
        big_number_array.append(x % 10)
        x = x // 10
        
    for i in range(2, exponent + 1):
        big_number_array = multiply(number, big_number_array)
        
    return int(''.join(list(map(lambda x: str(x), big_number_array[::-1]))))
    