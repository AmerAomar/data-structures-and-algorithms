class Node:
    def __init__(self,value):
        self.value=value
        self.next = None

class Linked_list:
    def __init__(self):
        self.head = None

    def insert(self,value):
           node1 = Node(value) 
           if self.head == None:
                self.head = node1
           else:
                node1.next = self.head
                self.head = node1

    def include(self,key):
         included = self.head
         if included is None:
              return False
         while included is not None:
              if included.value == key:
                   return True
              included = included.next
         if included is None:
              return False
         
    def __str__(self):
        output= ""
        if self.head is None:
            output = "the linked list is empty!"
        else:
            current = self.head
            while(current):
                output += f'{current.value}> '
                current = current.next
            
            output += "None"
        return output  
             