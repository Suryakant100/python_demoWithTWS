"""
Stack:-
      - A stack is a linear data structure which stores itsems/values in a form of LIFO(Lat-in First out).
      - In stack, a new element is added at one end and an element is removed from that end only.
      - The insert and delete operations are often called push and pop.

      Functions:-
      > empty() - Returns whether the stack is empty 
      > size() - Returns the size of the stack
      > top() / peek() - Returns a reference to the topmost element of the stack
      > push(a) - Inserts the element ‘a’ at the top of the stack 
      > pop() - Deletes the topmost element of the stack 
"""

# Start STACK using Array
import array

class Stack:
    def __init__(self): # Creating cunstructor of class and self is pointing to a current object in class
        self.my_stack=array.array('i',[]) # Creating empty array
        self.top=-1 # initial position of the stack is -1 which is store in the variabel

    def get_top(self): 
        print(len(self.my_stack)-1)

    def push(self,element): # function to puch element into the stack
        self.my_stack.append(element)    
    
    def is_empty(self): # Function for if the stack is empty or not
        if len(self.my_stack):
            return False
        else:
            return True

    def pop(self): # function to remove element from the stack
        if self.is_empty(): # Checking if the stack is empty or not
            print("Stack is empty cannot be pop")
        else:
            self.my_stack.pop()

     

if __name__ == '__main__': # main function/entry point of code

    stack=Stack() # Creating object of stcak class
    
    stack.get_top() # Get the top

    # Push operations onto stack
    stack.push(1) # Push 1st element
    stack.push(2) # Push 2nd element            
    stack.get_top() # Get the top            
    stack.push(3) # Push 3rd element    

    print( stack.my_stack)  

    # Pop operations onto stack
    stack.pop() # Pop 1st element from stack
    stack.pop() # Pop 2nd element from stack
    stack.pop() # Pop 3rd element from stack
    #stack.pop() # Error cause in stack is size of 3 and we trying to pop 4th element from stack
    print( stack.my_stack) 

    