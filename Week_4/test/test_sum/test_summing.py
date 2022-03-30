from bin.summing import *

def test_sum():
    assert simple_sum(3,3) == 6, 'should be 6'

def another_test_sum():
    assert multiple_sum(1,2,3,4,5) == 15
