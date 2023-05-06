from stack import Stack
from queue import Queue
import pytest
def test_stack():
    stack = Stack()
    assert stack.is_empty() == True

    # Test push method
    stack.push(1)
    assert stack.peek() == 1
    assert stack.is_empty() == False

    # Test push multiple values onto stack
    stack.push(2)
    stack.push(3)
    assert stack.peek() == 3

    # Test pop method
    assert stack.pop() == 3
    assert stack.peek() == 2

    # Test emptying the stack
    stack.pop()
    stack.pop()
    assert stack.is_empty() == True

    # Test calling pop on empty stack raises exception
    with pytest.raises(Exception):
        stack.pop()

    # Test calling peek on empty stack raises exception
    with pytest.raises(Exception):
        stack.peek()


def test_queue():
    queue = Queue()
    assert queue.is_empty() == True

    # Test enqueue method
    queue.enqueue(1)
    assert queue.peek() == 1
    assert queue.is_empty() == False

    # Test enqueue multiple values into queue
    queue.enqueue(2)
    queue.enqueue(3)
    assert queue.peek() == 1

    # Test dequeue method
    assert queue.dequeue() == 1
    assert queue.peek() == 2

    # Test emptying the queue
    queue.dequeue()
    queue.dequeue()
    assert queue.is_empty() == True

    # Test calling dequeue on empty queue raises exception
    with pytest.raises(Exception):
        queue.dequeue()

    # Test calling peek on empty queue raises exception
    with pytest.raises(Exception):
        queue.peek()
