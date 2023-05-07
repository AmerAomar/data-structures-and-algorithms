from stack import Stack

class PseudoQueue:
    def __init__(self):
        '''
        This PseudoQueue class will implement standard queue interface (the two methods listed below),
        '''
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, value):
        '''
        This method inserts value into the PseudoQueue, using a first-in, first-out approach.
        '''
        self.stack1.push(value)

    def dequeue(self):
     '''
        This method extracts a value from the PseudoQueue, using a first-in, first-out approach.
     '''

     if len(self.stack2) == 0:
         if len(self.stack1) == 0:
             raise ValueError("Cannot dequeue from an empty queue")
         while len(self.stack1) > 0:
             self.stack2.push(self.stack1.pop())
     return self.stack2.pop()
