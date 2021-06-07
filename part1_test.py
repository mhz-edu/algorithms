import pytest
from part1 import karatsuba_mult, recursive_mult, inversions_number


class TestRecursive:
    def test_recursive_mult1(self):
        assert recursive_mult('2', '3') == 6
    
    def test_recursive_mult2(self):
        assert recursive_mult('12', '35') == 420
    
    def test_recursive_mult3(self):
        assert recursive_mult('1234', '5678') == 7006652
    
    def test_recursive_mult4(self):
        assert recursive_mult('1234', '1') == 1234
    
    def test_recursive_mult5(self):
        assert recursive_mult('3141592653589793238462643383279502884197169399375105820974944592',
                              '2718281828459045235360287471352662497757247093699959574966967627') == 8539734222673567065463550869546574495034888535765114961879601127067743044893204848617875072216249073013374895871952806582723184
    
    def test_recursive_mult6(self):
        assert recursive_mult('1234', '0') == 0
    
class TestKaratsuba:
    def test_karatsuba_mult1(self):
        assert karatsuba_mult('2', '3') == 6

    def test_karatsuba_mult2(self):
        assert karatsuba_mult('12', '35') == 420
    
    def test_karatsuba_mult3(self):
        assert karatsuba_mult('1234', '5678') == 7006652
    
    def test_karatsuba_mult4(self):
        with pytest.raises(AssertionError):
            karatsuba_mult('1234', '1') == 1234
    
    def test_karatsuba_mult5(self):
        assert karatsuba_mult('3141592653589793238462643383279502884197169399375105820974944592',
                              '2718281828459045235360287471352662497757247093699959574966967627') == 8539734222673567065463550869546574495034888535765114961879601127067743044893204848617875072216249073013374895871952806582723184
    
    def test_karatsuba_mult6(self):
        with pytest.raises(AssertionError):
            karatsuba_mult('123', '456')

class TestInversions:
    def test_inversions_number1(self):
        assert inversions_number([1,3,5,2,4,6]) == 3
    
    def test_inversions_number2(self):
        assert inversions_number([1,3,5,4,6,2]) == 5
    
    def test_inversions_number3(self):
        assert inversions_number([1]) == 0
    
    def test_inversions_number4(self):
        assert inversions_number([2,1]) == 1
