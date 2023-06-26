# class Node:
#     def __init__(self,value):
#         self.value=value
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def insert(self,value):
#            node1 = Node(value) 
#            if self.head == None:
#                 self.head = node1
#            else:
#                 node1.next = self.head
#                 self.head = node1

#     def include(self,key):
#          included = self.head
#          if included is None:
#               return False
#          while included is not None:
#               if included.value == key:
#                    return True
#               included = included.next
#          if included is None:
#               return False
         
#     def __str__(self):
#         output= ""
#         if self.head is None:
#             output = "the linked list is empty!"
#         else:
#             current = self.head
#             while(current):
#                 output += f'{current.value}> '
#                 current = current.next
            
#             output += "None"
#         return output  
             



class Node:
    def __init__(self, value):
        self.value=value
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None   


    def insert(self, value):
        new_node=Node(value) 

        if self.head==None:
            self.head=new_node

        else:    

            pointer=self.head

            while pointer.next !=None:
                pointer= pointer.next

            pointer.next=new_node


    def delete(self, value):
        if self.head == None:
            return "empty"
        
        else:
            pointer=self.head 
            while pointer.next !=None:
                if pointer.next.value == value:
                    pointer.next=pointer.next.next
                    return"value deleted"
                
                pointer=pointer.next

            if pointer.next==None:
                return"Not found"        







    def print_list(self):
        current = self.head
        while current is not None:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

if __name__ == "__main__":
    LinkedList = LinkedList()
    LinkedList.insert(10)
    LinkedList.insert(20)
    LinkedList.insert(30)
    LinkedList.print_list()
    LinkedList.delete(20)
    LinkedList.print_list()        
