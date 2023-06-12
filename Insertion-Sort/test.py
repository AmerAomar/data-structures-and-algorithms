import pytest

from main import insertion_sort

def test_insertion_sort():
    # Test Case 1
    arr1 = [8, 4, 23, 42, 16, 15]
    expected1 = [4, 8, 15, 16, 23, 42]
    assert insertion_sort(arr1) == expected1

    # Test Case 2
    arr2 = [20, 18, 12, 8, 5, -2]
    expected2 = [-2, 5, 8, 12, 18, 20]
    assert insertion_sort(arr2) == expected2

    # Test Case 3
    arr3 = [5, 12, 7, 5, 5, 7]
    expected3 = [5, 5, 5, 7, 7, 12]
    assert insertion_sort(arr3) == expected3

    # Test Case 4
    arr4 = [2, 3, 5, 7, 13, 11]
    expected4 = [2, 3, 5, 7, 11, 13]
    assert insertion_sort(arr4) == expected4

    # Additional Test Case
    arr5 = [1]
    expected5 = [1]
    assert insertion_sort(arr5) == expected5

    arr6 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    expected6 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert insertion_sort(arr6) == expected6

    arr7 = [1, 2, 3, 4, 5]
    expected7 = [1, 2, 3, 4, 5]
    assert insertion_sort(arr7) == expected7

    arr8 = []
    expected8 = []
    assert insertion_sort(arr8) == expected8

if __name__ == '__main__':
    pytest.main()
