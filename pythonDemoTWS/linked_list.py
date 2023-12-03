"""
 - A linked list is a type of linear data structure similar to arrays.
 - It is a collection of nodes that are linked with each other.
 - A node contains two things first is data and second is a link that connects it with another node.
 - 

"""

# Implementation of linked-List data structure

class Node:
    def __init__(self,data):
        self.data = data
        self.nextval=None


class LinkedList:
    def __init__(self):
        self.head = None

"""
"Insertion at Beginning in Linked List":-
  - This method inserts the node at the beginning of the linked list. 
  - In this method, we create a new_node with the given data
  - and check if the head is an empty node or not if the head is
  - empty then we make the new_node as head and return else we insert the head at the next new_node and make the head equal to new_node.
"""
    def insertAtBegin(self,data): # inserting a new node at the beginning of the linked list
        new_node=Node(data) # Creating a new node object 
        if self.head is None: # Checking the linkq List is empty
            self.head = new_node
            return
        else:
            new_node.nextval=self.head
            self.head = new_node

    def insertAtIndex(self,data,index): # inserting
        new_node=Node(data) # Creating a new node
        current_node=self.head
        position=0
        if position==index:
            self.insertAtBegin(data)
        else:
            while(current_node!=None and position+1 != index):
                  position=osition + 1
                  current_node=current_node.nextval
            if current_node!=None:
                new_node.nextval=current_node.nextval  
                current_node.nextval=new_node
            else:
                print("Index not present")        

    def get_item(self):
        current = self.head
        while current is not None:
            print(current.data)  
            current = current.nextval  

if __name__ == '__main__':
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node('a')

    print(n1.data)

    linkList=LinkedList()
    linkList.head=n1
    linkList.head.nextval=n2
    n2.nextval=n3
    n3.nextval=n4
    n4.nextval=None
    
    linkList.get_item()
