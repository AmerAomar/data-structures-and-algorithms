from array_insert_shift import insertShiftArray

def test_array_insert_shift_first_test():
    actual = insertShiftArray([7, 6, 8, 1], 10)
    expected = [7, 6, 10, 8, 1]
    assert actual == expected


def test_array_insert_shift_second_test_empty_array():
    actual = insertShiftArray([], 5)
    expected = [5]
    assert actual == expected


def test_array_insert_shift_third_test_odd_array_index():
    actual = insertShiftArray([1, 2, 3, 4, 5], 6)
    expected = [1, 2, 3, 6, 4, 5]
    assert actual == expected

    
def test_array_insert_shift_fourth_test_of_strings():
    actual = insertShiftArray(["apple", "banana", "orange", "grape", "watermelon"], "kiwi")
    expected = ["apple", "banana", "orange", "kiwi", "grape", "watermelon"]
    assert actual == expected