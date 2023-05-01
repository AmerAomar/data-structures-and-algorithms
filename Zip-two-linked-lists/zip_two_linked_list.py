class Node:
    '''
    Node class that has properties for the value stored in the Node, and a pointer to the next Node.

    '''
    def __init__(self, value, next=None):
        '''
        Constructor for Node class.
        '''
        self.value = value
        self.next = next

class LinkedList:
    '''
    Linked List class that has properties for the head of the list.
    '''
    def __init__(self):
        self.head = None

    def insert(self, value):
        '''
        Adds a new node with that value to the head of the list with an O(1) Time performance.
        '''
        node = Node(value)
        if not self.head:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node

                

    def __str__(self):
        '''
        Returns: a string representing all the values in the Linked List, formatted as:
        '''
        if not self.head:
            return "null"
        current = self.head
        output = ""
        while current:
            output += "{" + str(current.value) + "} -> "
            current = current.next
        output += "null"
        return output

def zip_lists(list1, list2):
    '''
    Takes two linked lists as arguments. Zip the two linked lists together 
    into one so that the nodes alternate between the two lists and return a 
    reference to the head of the zipped list.
    '''
    if not list1.head and not list2.head:
        return LinkedList()

    if not list1.head:
        return list2

    if not list2.head:
        return list1

    current1 = list1.head
    current2 = list2.head
    while current1 and current2:
        next1 = current1.next
        next2 = current2.next
        current1.next = current2
        if next1:
            current2.next = next1
        current1 = next1
        current2 = next2

    return list1
