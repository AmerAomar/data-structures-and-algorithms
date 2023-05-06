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
