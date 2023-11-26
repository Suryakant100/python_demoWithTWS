"""
Tuple:- Tuples are used to store multiple items in a single variable.
        - A tuple is a collection which is ordered and unchangeable and allow duplicate values.
        - A tuple also support unpacking of data into some diffrent variables 
Different types of tuples

1: Empty tuple
my_tuple = ()
print(my_tuple)

2: Tuple having integers
my_tuple = (1, 2, 3)
print(my_tuple)

3: tuple with mixed datatypes
my_tuple = (1, "Hello", 3.4)
print(my_tuple)

4: nested tuple
my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
print(my_tuple)

NOTE:- Create a Python Tuple With one Element
     eg: var1 = ("Hello") # string
         var2 = ("Hello",) # tuple         
"""

var1 = ("Hello") # string
var2 = ("Hello",) # tuple
print(type(var1))
print(type(var2))

"""
#Negative Indexing:
The index of -1 refers to the last item, -2 to the second last item and so on. For example,
# accessing tuple elements using negative indexing
letters = ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')

print(letters[-1])   # prints 'z' 
print(letters[-3])   # prints 'm'
"""
letters = ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')

print(letters[-1])   # prints 'z' 
print(letters[-3])   # prints 'm'

"""
 Slicing in TUPLE:
"""
# accessing tuple elements using slicing
my_tuple = ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')

# elements 2nd to 4th index
print(my_tuple[1:4])  #  prints ('r', 'o', 'g')

# elements beginning to 2nd
print(my_tuple[:-7]) # prints ('p', 'r')

# elements 8th to end
print(my_tuple[7:]) # prints ('i', 'z')

# elements beginning to end
print(my_tuple[:]) # Prints ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')

# NOTE: In Python ,methods that add items or remove items are not available with tuple:-

my_tuple1 = ('a', 'p', 'p', 'l', 'e',)
print(my_tuple1[0]) # prints the 0th element of the tuple

# my_tuple1[1]='s' # Error because Tuple is not changable
# print(my_tuple1) # prints

# Iterating through a Tuple in Python

languages = ('Python', 'Swift', 'C++')

for language in languages:
    print(language)


# Demonstrating the tuple
t=([1,2,3],4,5) # Creating a tuple which contain a list and some int values
print(t) # prints
print(t[2]) # prints 2nd index pf tuple

# t[2]=500 # Error because Tuple is not changable 

t[0].append(500) # But here it will not show any error because 0th index of tuple contain a list which is mutable nature

print(t) # Print updated tuple


########################

t2 = (10,20,30)
print(t2) # prints t2 tuple BUT

a,b,c =(10,20,40) # unpacking a tuple which will assign each value to each variable i.e a,b,c

print(a,b,c)

#  Compare Tuple vs List which is fast?

import timeit

print(timeit.timeit('x=(1,2,3,4)',number=1000000)) #
print(timeit.timeit('x=[1,2,3,4]',number=1000000)) #

# Hence Tuple is more fater than List cause it will not create dynamic memory 

"""
Advantages of Tuple over List in Python:
   - We generally use tuples for heterogeneous (different) data types and lists for homogeneous (similar) data types.
   - Since tuples are immutable, iterating through a tuple is faster than with a list. So there is a slight performance boost.
   - Tuples that contain immutable elements can be used as a key for a dictionary. With lists, this is not possible.
   - If you have data that doesn't change, implementing it as tuple will guarantee that it remains write-protected.

"""