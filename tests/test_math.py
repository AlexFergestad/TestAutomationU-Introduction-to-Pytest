import pytest
""" In Python, the assert statement is used to check whether a 
 condition is true. If the condition is true, the assert 
 statement does nothing and the program continues to run. 
 If the condition is false, the assert statement raises an 
 AssertionError exception. This exception can be caught and handled, 
 but if it is not, it will cause the program to terminate. """
def test_one_plus_one():
    assert 1 + 1 == 2

def test_one_plus_two():
    a = 1
    b = 2
    c = 3
    assert a + b == c

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError) as e:
        num = 1 / 0

    assert 'division by zero' in str(e.value)

# Multiplication test ideas:
# two positive integers
# identity: multiply by 1
# zero: multiply by 0
# positive by negative
# negative by negative
# floats
products = [
    (2, 3, 6),
    (1, 99, 99),
    (0, 99, 0),
    (3, -4, -12),
    (-5, -5, 25),
    (2.5, 6.7, 16.75)
]
@pytest.mark.math
@pytest.mark.parametrize('a, b, product', products)
def test_multiplication(a, b, product):
    assert a * b == product

