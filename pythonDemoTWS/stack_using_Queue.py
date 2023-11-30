"""
- Queue module also has a LIFO Queue, which is basically a Stack. Data is inserted into Queue using the put() function and get() takes data out from the Queue. 

Functios:-
    - maxsize - Number of items allowed in the queue.
    - empty() - Return True if the queue is empty, False otherwise.
    - full() - Return True if there are maxsize items in the queue. If the queue was initialized with maxsize=0 (the default), then full() never returns True.
    - get() - Remove and return an item from the queue. If the queue is empty, wait until an item is available.
    - get_nowait() - Return an item if one is immediately available, else raise QueueEmpty.
    - put(item) - Put an item into the queue. If the queue is full, wait until a free slot is available before adding the item.
    - put_nowait(item) - Put an item into the queue without blocking. If no free slot is immediately available, raise QueueFull.
    - qsize() - Return the number of items in the queue.

"""
# Implementation of Stack useing by Queue in python

from queue import LifoQueue # Import queue from LifoQueue class

stack = LifoQueue(maxsize=4) # initialize the stack with prviding the max size of stack

print(stack.qsize()) # print the size of the stack

stack.put('s') # put an item into the stack
stack.put('u') # put an item into the stack
stack.put('r') # put an item into the stack
stack.put('y') # put an item into the stack
stack.put('a') # put an item into the stack

print(stack.qsize()) # print the size of the stack

print(stack.get())
print(stack.get())
print(stack.get())