from linked_list_insertion.linked_list_insertions import linked_list

def test_append():
    lst = linked_list()
    lst.append(1)
    assert lst.head.value == 1
    lst.append(2)
    assert lst.head.next.value == 2
    lst.append(3)
    assert lst.head.next.next.value == 3


def test_insert_before():
    lst = linked_list()
    lst.append(1)
    lst.append(2)
    lst.append(3)
    lst.insert_before(2, 4)
    assert lst.head.value == 1
    assert lst.head.next.value == 4
    assert lst.head.next.next.value == 2
    assert lst.head.next.next.next.value == 3

def test_insert_before_first():
    lst = linked_list()
    lst.append(1)
    lst.append(2)
    lst.insert_before(1, 3)
    assert lst.head.value == 3
    assert lst.head.next.value == 1
    assert lst.head.next.next.value == 2

def test_insert_after():
    lst = linked_list()
    lst.append(1)
    lst.append(2)
    lst.append(3)
    lst.insert_after(2, 4)
    assert lst.head.value == 1
    assert lst.head.next.value == 2
    assert lst.head.next.next.value == 4
    assert lst.head.next.next.next.value == 3

def test_insert_after_last():
    lst = linked_list()
    lst.append(1)
    lst.append(2)
    lst.insert_after(2, 3)
    assert lst.head.value == 1
    assert lst.head.next.value == 2
    assert lst.head.next.next.value == 3
    assert lst.head.next.next.next is None



