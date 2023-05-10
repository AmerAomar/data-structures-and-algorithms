from zip_two_linked_list import zip_lists, LinkedList

import pytest

@pytest.mark.parametrize("list1_values, list2_values, expected_output", [
    ([1, 3, 2], [5, 9, 4], "{1} -> {5} -> {3} -> {9} -> {2} -> {4} -> null"),
    ([1, 3], [5, 9, 4], "{1} -> {5} -> {3} -> {9} -> {4} -> null"),
    ([1, 3, 2], [5, 9], "{1} -> {5} -> {3} -> {9} -> {2} -> null"),
    ([], [], "null"),
])
def test_zip_lists(list1_values, list2_values, expected_output):
    list1 = LinkedList()
    list2 = LinkedList()

    for value in list1_values:
        list1.insert(value)

    for value in list2_values:
        list2.insert(value)

    assert str(zip_lists(list1, list2)) == expected_output
