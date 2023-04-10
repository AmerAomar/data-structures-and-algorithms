from binary_search import binary_search

def test_binary_search_numeric_array_even():
    actual = binary_search([1,2,3,4],2)
    expected = 1
    assert expected==actual

def test_binary_search_numeric_array_odd():
    actual = binary_search([1,2,3,4,5],4)
    expected = 3
    assert expected==actual

def test_binary_search_not_in_array():
    actual = binary_search([1,2,3,4,5],6)
    expected = -1
    assert expected==actual

def test_binary_search_empty_array():
    actual = binary_search([],1)
    expected = -1
    assert expected==actual