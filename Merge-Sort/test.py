import pytest
from main import merge_sort

def test_merge_sort():
    # Sample Array 1: [8, 4, 23, 42, 16, 15]
    arr1 = [8, 4, 23, 42, 16, 15]
    sorted_arr1 = merge_sort(arr1)
    assert sorted_arr1 == [4, 8, 15, 16, 23, 42]

    # Sample Array 2: [20, 18, 12, 8, 5, -2]
    arr2 = [20, 18, 12, 8, 5, -2]
    sorted_arr2 = merge_sort(arr2)
    assert sorted_arr2 == [-2, 5, 8, 12, 18, 20]

    # Sample Array 3: [5, 12, 7, 5, 5, 7]
    arr3 = [5, 12, 7, 5, 5, 7]
    sorted_arr3 = merge_sort(arr3)
    assert sorted_arr3 == [5, 5, 5, 7, 7, 12]

    # Sample Array 4: [2, 3, 5, 7, 13, 11]
    arr4 = [2, 3, 5, 7, 13, 11]
    sorted_arr4 = merge_sort(arr4)
    assert sorted_arr4 == [2, 3, 5, 7, 11, 13]
