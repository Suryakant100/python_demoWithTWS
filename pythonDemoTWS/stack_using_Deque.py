"""
 - Python stack can be implemented using the deque class from the collections module. 
 - Deque is preferred over the list in the cases where we need quicker append and pop operations from both the ends of the container
 - deque provides an O(1) time complexity for append and pop operations as compared to list which provides O(n) time complexity. 
"""

# Implementation of Stcak using the deque class from the collections module in python

from collections import deque # impoting the deque class from the collections module

stack = deque() # Create a variable or object of deque class

stack.append('a') # adding element to stack
stack.append('b')
stack.append('c')
stack.append('d')

print(stack)

stack.pop() # remove element from stack

print(stack)

for i in range(len(stack)):
    print(stack[i])