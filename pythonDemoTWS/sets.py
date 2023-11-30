"""
 Set:- Sets are used to store multiple items in a single variable.
     - set is a collection which is unordered, unchangeable*, and unindexed.
     - Set items are unchangeable, but you can remove items and add new items.
     - Sets are written with curly brackets
     - Sets are unordered, so you cannot be sure in which order the items will appear.
     - Set items are unordered, unchangeable, and do not allow duplicate values.
     - Set items can appear in a different order every time you use them, and cannot be referred to by index or key.
     - Set items are unchangeable, meaning that we cannot change the items after the set has been created.
     - Once a set is created, you cannot change its items, but you can remove items and add new items.
     - The values True and 1 are considered the same value in sets, and are treated as duplicates
     - The values False and 0 are considered the same value in sets, and are treated as duplicates

     eg.- 
     myset = {"apple", "banana", "cherry"}
"""

 # Creating a new set

myset={"apple", "banana", "cherry"} # Create a set with given value
print(myset)

set1={} # Its look like a set but its a empty dictionary
print(type(set1)) # Dict type
# If we want to create a empty set then we have to use set() cunstructor

set2 = set()
print(type(set2)) # Set type

set_of_cars={"BMW","AUDI","Volvo","Marcedez","BMW","audi","TATA"}
print(set_of_cars) # Print a set with remove duplicates values from set and its also a case sensitive and also print in unorderd way

set_of_cars.add("skoda") # Adding new element into the set() using set method
print(set_of_cars) 

set_of_cars.remove("audi") # Remove an element from set using remove() method
print(set_of_cars)

# print(set_of_cars[0]) #error cause set' object is not subscriptable(The term "subscriptable" in Python means a data type that stores multiple values that you can access individually.)

set_of_cars2={"TATA","MARUTI","MAHINDRA"}
# set2=set_of_cars.union(set_of_cars2) # It will merge the two set into one set using union() method
set2 = set_of_cars | set_of_cars2 # Union method using '|' operator
print(set2) # Print a union set of two sets

intersection_set=set_of_cars.intersection(set_of_cars2) # It will find the common element from two sets using intersection() method
print(intersection_set)


a={1,2,3,4,5,6}
b={2,5,6,7,8}
print(b.difference(a)) # Print the set b but if any element from a which is common to b it will remove

# print(dir(a))

first_set = set(("Connor", 32, (1, 2, 3)))
print(first_set)

second_set = set("Connor")
print(second_set)

correct_set = {"Apples", ("Bananas", "Oranges")}
print(correct_set)

# incorrect_set = {"Apples", ["Bananas", "Oranges"]} #  each element needs to be an immutable object. So if you add a list (which is a mutable object) to a set, you'll run into an error
# print(incorrect_set)

add_set={1, 2, 3, 4, 'violin', 'cello',"Pencil","Pen"} 
print(add_set)
add_set.remove("Pen") # It will remvove "Pen" from the set
print(add_set)
# add_set.remove("V") #Throw an error cause 'V' is not a part of the set

# NOTE:-
"""
There are a couple of other ways to remove an element(s) from a set:

 - the discard(x) method removes x from the set, but doesn't raise any error if x is not present in the set.
 - the pop() method removes and returns a random element from the set.
 - the clear() method removes all elements from a set.
"""
print("###############")

m_set = set((1, 2, 3, 4))
print(m_set)

m_set.discard(5) # no error raised even though '5' is not present in the set
print(m_set)

m_set.pop() # It will remove last element from the list
print(m_set)

m_set.clear() # It will remove all elements from the set
print(m_set)





"""
Diff b/w Add and update in a set of python

 - We can use add() and update() method to add elements to set. 
 - add() used to add one element to set.
 - update() method used to add multiple elements to set. Note: Both add() and update() methods will modify the original set itself.
"""