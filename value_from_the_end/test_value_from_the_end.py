import pytest
from .value_from_the_end import LinkedList

@pytest.mark.parametrize("lst, k, expected", [
    ([1, 3, 8, 2], 0, 2),
    ([1, 3, 8, 2], 1, 8),
    ([1, 3, 8, 2], 3, 1),
    ([1, 3, 8, 2], 4, ValueError),
    ([1, 3, 8, 2], 5, ValueError),
    ([1, 3, 8, 2], -1, ValueError),
    ([], 0, ValueError),
    ([1], 0, 1),
    ([1, 3, 8, 2, 5], 2, 8)
])
def test_kth_from_end(lst, k, expected):
    ll = LinkedList()
    for val in lst:
        ll.add(val)

    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            ll.kth_from_end(k)
    else:
        assert ll.kth_from_end(k) == expected
