"""
 - the queue is a linear data structure that stores items in a First In First Out (FIFO) manner.
 - With a queue, the least recently added item is removed first. A good example of a queue is any queue of consumers for a resource where the consumer that came first is served first.

 Functios:
  - Enqueue: Adds an item to the queue. If the queue is full, then it is said to be an Overflow condition – Time Complexity : O(1)
  - Dequeue: Removes an item from the queue. The items are popped in the same order in which they are pushed. If the queue is empty, then it is said to be an Underflow condition – Time Complexity : O(1)
  - Front: Get the front item from queue – Time Complexity : O(1)
  - Rear: Get the last item from queue – Time Complexity : O(1)
"""

# Implementation of queue using Array 

import array # Import the array

class Queue: # Creating th class instance of Queue
  def __init__(self): # Creating Cunstructur of class
    self.my_queue=array.array('i',[]) # Creating empty array

  def enqueue(self,element): # Enqueuing the element to the queue from rear side
    self.my_queue.append(element) 
  
  def IsEmpty(self): # Checking if queue is empty
    if(len(self.my_queue)):
      return False
    else:
      return True  
  
   

  def dequeue(self): # poping the element from queue and it will remove from front side of queue
    if self.IsEmpty():
      print("Queue is empty can't preform dequeue operation")
    else: 
      self.my_queue.pop(0)   

if __name__ == "__main__": # Main method  or Entry point of code
        queue=Queue() # Creating The object of the queue
        print(queue.my_queue)

        queue.enqueue(1) # Appending the element to the queue
        queue.enqueue(2)
        queue.enqueue(3)
        print(queue.my_queue)

        queue.dequeue()
        print(queue.my_queue)

        queue.dequeue()
        print(queue.my_queue)
        queue.dequeue()

        print(queue.my_queue)
        queue.dequeue()
