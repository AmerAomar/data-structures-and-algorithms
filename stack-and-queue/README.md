# Stack and a Queue Implementation
<!-- Description of the challenge -->
Implement a Stack and a Queue data structure using a Linked List.

## Whiteboard Process
<!-- Embedded whiteboard image -->

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
### Stack

- `push(value)` - Time: O(1), Space: O(1)
- `pop()` - Time: O(1), Space: O(1)
- `peek()` - Time: O(1), Space: O(1)
- `isEmpty()` - Time: O(1), Space: O(1)

### Queue

- `enqueue(value)` - Time: O(1), Space: O(1)
- `dequeue()` - Time: O(1), Space: O(1)
- `peek()` - Time: O(1), Space: O(1)
- `isEmpty()` - Time: O(1), Space: O(1)

## Solution

<!-- Show how to run your code, and examples of it in action -->

### node

```python
class Node :
    def __init__(self, value) :
        self.value = value
        self.next = None
       
```

### Stack

```python
from node import Node

class Stack:
    def __init__(self):
        '''
        This method initializes an empty Stack.'''
        self.top=None
        self.size=0

    def push(self,value):
        '''
        This method adds a new node with that value to the top of the stack with an O(1) Time performance.'''
        node=Node(value)
        if self.top:
            node.next=self.top

        self.top=node
        self.size+=1

    def pop(self):
        '''
        This method removes the node from the top of the stack, and returns the node’s value.
        Raises an exception if called on an empty stack.
        '''
        if self.top:
            temp=self.top
            self.top=self.top.next
            self.size-=1
            return temp.value
        else:
            raise Exception("pop from empty stack")

    def peek(self):
        '''
        This method returns the value of the node located on top of the stack, without removing it from the stack.
        Raises an exception if called on an empty stack.
        '''
        if self.top:
            return self.top.value
        else:
            raise Exception("peek on empty stack")

    def is_empty(self):
        '''
        This method returns a boolean indicating whether or not the stack is empty.
        '''
        if self.top:
            return False
        else:
            return True

```

### Queue

```python
from node import Node

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        '''
        This method adds a new node with that value to the back of the queue with an O(1) Time performance.     
        '''
        node = Node(value)

        if not self.rear:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def dequeue(self):
        '''
        This method removes the node from the front of the queue, and returns the node’s value.
        Raises an exception if called on an empty queue.
        '''
        if not self.front:
            raise Exception("dequeue from empty queue")

        temp = self.front
        self.front = self.front.next
        
        if not self.front:
            self.rear = None
        
        temp.next = None
        return temp.value

    def peek(self):
        '''
        This method returns the value of the node located in the front of the queue, without removing it from the queue.
        Raises an exception if called on an empty queue.
        '''
        if not self.front:
            raise Exception("peek on empty queue")

        return self.front.value  

    def is_empty(self):
        '''
        This method returns a boolean indicating whether or not the queue is empty.
        '''
        if not self.front:
            return True
        return False
```
