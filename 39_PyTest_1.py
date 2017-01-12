import pytest

#naming is very important in pytest
#when we initially run pytest it will look for any program that strats with word 'test'
#and the it will look for any function that starts with word 'test'
#run all the test programs with py.test

#use setup_class() method to do test prep
#use teardown_class() method to clean up after tests

######### in a file called myprogram.py ################
import sys

def doubleit(x):
    return x * 2

#if we directly run myprogram.py code in this if block will get executed
#if we import the myprogram.py to another program code in this if block will not get executed

if __name__ == '__main__':
    input_val = sys.argv[1]
    doubled_val = doubleit(input_val)
    print 'the value of {0} is {1}'.format(input_val, doubled_val)

######### in a file called test_myprogram.py ################
#import myprogram

def test_doubleit():
    assert doubleit(10) == 20

#assert if we pass a string to doubleit it will raise a TypeError
def test_doubleit_type():
    with pytest.raises(TypeError):
        doubleit('hello')

