class Stack:
    def __init__(self):
        '''
        This method initializes an empty Stack.
        '''
        self.items = []

    def push(self, item):
        '''
        This method adds a new node with that value to the top of the stack with an O(1) Time performance.
        '''
        self.items.append(item)

    def pop(self):
        '''
        This method removes the node from the top of the stack, and returns the node’s value.
        '''
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        '''
        This method returns the value of the node located on top of the stack, without removing it from the stack.
        '''
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        '''
        This method returns a boolean indicating whether or not the stack is empty.
        '''
        return len(self.items) == 0

    def __len__(self):
        '''
        This method returns the length of the stack.
        '''
        return len(self.items)
