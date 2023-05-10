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
