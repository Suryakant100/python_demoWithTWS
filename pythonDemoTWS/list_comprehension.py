"""
 Def:- A Python list comprehension consists of brackets containing the expression, which is executed 
for each element along with the for loop to iterate over each element in the Python list. 
     
      OR 
 
 List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.


Syntax: newList = [ expression(element) for element in oldList if condition ]

NOTE:- 
1) Return:The return value of a list comprehension is a new list containing the modified elements that satisfy the given criteria.

2) Python List comprehension provides a much more short syntax for creating a new list based on the values of an existing list.
"""

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newList=[]

# Normal way to insert data from one list to another
for x in fruits:
    newList.append(x)
print(newList)    

# List Comprehension way to insert data 
newList2=[x for x in fruits]
print(newList2)

# Insert Only Even Number in list of range 1 to 10 using list comprehension

list_comp_even=[i for i in range(1,11) if i % 2 ==0]
print(list_comp_even)


"""
List Comp Example from HackerRank
https://www.hackerrank.com/challenges/list-comprehensions/problem
"""

x=int(input("Enter the value of x:"))
y=int(input("Enter the value of y:"))
z=int(input("Enter the value of z:"))
n=int(input("Enter the value of n:"))

# Using Normal For Loop:
answer=[]
for a in range(x+1):
    for b in range(y+1):
        for c in range(z+1):
            if a+b+c!=n:
                answer.append([a,b,c])

print(answer)

# Using List Comp:

final_answer=[[a,b,c] for a in range(x+1) for b in range(y+1) for c in range(z+1) if a+b+c!=n]
print(final_answer)