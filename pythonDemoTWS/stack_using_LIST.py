"""
  - Python's built-in data structure list can be used as a stack. Instead of push(), append() is used to add elements to the top of the stack while pop() removes the element in LIFO order. 
  - The biggest issue is that it can run into speed issues as it grows. The items in the list are stored next to each other in memory, if the stack grows bigger than the block of memory that currently holds it, then Python needs to do some memory allocations.
"""

# Implementation of Stack using LIST in python

stack = [] # creat a list which will act like a stack

stack.append(1) # push the first element
stack.append(2) # push the second element
stack.append(3) # push the third element
stack.append(4) # push the fourth element

print(stack) # print the stack

print(max(stack)) # print the maximum value in stack

stack.pop() # pop the stack
print(stack) 