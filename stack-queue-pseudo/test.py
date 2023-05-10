import pytest
from pseudo_queue import PseudoQueue

def test_enqueue():
    '''
    Can successfully enqueue into a queue
    '''
    q = PseudoQueue()
    q.enqueue(10)
    assert q.stack1.peek() == 10
    q.enqueue(20)
    assert q.stack1.peek() == 20
    q.enqueue(30)
    assert q.stack1.peek() == 30

def test_dequeue():
    '''
    Can successfully dequeue out of a queue the expected value
    '''
    q = PseudoQueue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    assert q.dequeue() == 10
    assert q.stack2.peek() == 20
    assert q.dequeue() == 20
    assert q.stack2.peek() == 30
    assert q.dequeue() == 30

def test_dequeue_from_empty():
    '''
    Can successfully peek into a queue, seeing the expected value
    '''
    q = PseudoQueue()
    with pytest.raises(ValueError):
        q.dequeue()


def test_dequeue_after_enqueue():
    '''
    Can successfully empty a queue after multiple dequeues
    '''
    q = PseudoQueue()
    q.enqueue(10)
    q.enqueue(20)
    assert q.dequeue() == 10
    q.enqueue(30)
    assert q.dequeue() == 20
    assert q.dequeue() == 30
    assert q.stack1.is_empty()
    assert q.stack2.is_empty()

def test_enqueue_after_dequeue():
    '''
    Can successfully enqueue after multiple dequeues
    '''
    q = PseudoQueue()
    q.enqueue(10)
    q.enqueue(20)
    assert q.dequeue() == 10
    q.enqueue(30)
    assert q.dequeue() == 20
    q.enqueue(40)
    assert q.stack1.peek() == 40
    assert q.stack2.is_empty()
