# Array:- Array is the data structure which stores similar type of data but list store hetrogenous type of data.

# We can't use array directly in python because python treats arrays as a List 
# So we need to import the array from python library

# Creating an Array:
# Array in Python can be created by importing an array module. array(data_type, value_list) is used to create an array with data type and value list specified in its arguments

import array

arr = array.array('i',[]) # Creating empty array
print(type(arr))
print(arr)

arr2 = array.array('i',[2,4,3,5,6]) # Creating array with data 
print(arr2)

arr2.append(12) # Adding new elements to the array using append method
print(arr2)

arr2.insert(2,12) # Adding new elements to the array at specific index using inset method

arr2.pop() # removing elements from the array which will be removed from the end of the array
print(arr2)

arr2.pop(1) # removing elements from using index number
print(arr2)

print(arr2[0:3]) # Sclice the array

arr2[3]=100 # updating the array
print(arr2)

arr2.reverse() # Reverse the array
print(arr2) 