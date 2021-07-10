import pytest
from part1 import comparison_number, first_element, karatsuba_mult, last_element, median_of_three, partition, quick_sort, recursive_mult, inversions_number


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

class TestPartitions:
    def test_first_element(self):
        assert partition([3,8,2,5,1,4,7,6], first_element) == ([2, 1], [3], [5, 8, 4, 7, 6])

    def test_last_element(self):
        assert partition([3,8,2,5,1,4,7,6], last_element) == ([3, 2, 5, 1, 4], [6], [8, 7])

class TestQuickSort:
    def test_one_element_list(self):
        assert quick_sort([123]) == [123]

    def test_two_element_list(self):
        assert quick_sort([34, 12]) == [12, 34]

    def test_more_than_two_elem_list(self):
        assert quick_sort([3,8,2,5,1,4,7,6]) == [1,2,3,4,5,6,7,8]

class TestComparisonNumber:
    def test_first_element(self):
        assert comparison_number([3,8,2,5,1,4,7,6], first_element) == 15

    def test_last_element(self):
        assert comparison_number([3,8,2,5,1,4,7,6], last_element) == 15

    def test_median_three(self):
        assert comparison_number([3,8,2,5,1,4,7,6], median_of_three) == 13