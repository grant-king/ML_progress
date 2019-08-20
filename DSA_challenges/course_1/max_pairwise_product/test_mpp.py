from naive import mpp as slow_mpp
from fast import mpp as fast_mpp
import random

def test_slow_mpp():
    assert slow_mpp([5, 4, 6, 10]) == 60

def test_slow_mpp_long_input():
    sequence = [random.randrange(10) for number in range(1000)]
    sequence.append(11)
    sequence.append(20)
    assert slow_mpp(sequence) == 220

def test_fast_mpp():
    assert fast_mpp([5, 4, 6, 10]) == 60

def test_fast_mpp_long_input():
    sequence = [random.randrange(10) for number in range(100000)]
    sequence.append(11)
    sequence.append(20)
    assert fast_mpp(sequence) == 220

def test_stress_tests():
    print('beginning stress testing')
    
    def stress_test():    
        MAX_LIST_SIZE = 1000
        MAX_ITEM_VALUE = 500

        sequence_size = random.randint(2, MAX_LIST_SIZE)
        sequence = [random.randrange(MAX_ITEM_VALUE) for item in range(sequence_size)]

        result1 = slow_mpp(sequence)
        result2 = fast_mpp(sequence)
        
        if result1 != result2:
            print('results differ')
        else:
            return True

    for i in range(1000):
        assert stress_test() == True
