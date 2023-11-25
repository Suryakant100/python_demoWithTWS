"""
Def:- Dictionaries are used to store data values in key:value pairs. Denote as '{}'
Note:-
A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
"""

d1={} # 1st way to create dict empty

d2 = dict() # 2nd way to create dict empty

# Example:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(thisdict)
print(thisdict['year']) # Get value using 'key' 
print(thisdict.get('model')) # Getting the value using get method in dictionaries

thisdict['country']="United States" # Adding new Ket:VAlue in dictionary
thisdict['brand']="FORD" # Updating the dictionary value using key
print(thisdict)

thisdict.update({"owner":"Surya"}) # It will append/update some data into the dictionary
print(thisdict)

print(thisdict.keys()) # It will print a list of Keys in the given dictionary
print(thisdict.values()) # It will print the values in the given dictionary
print(thisdict.items()) # It will print the dictionary in the LIST format

for key in thisdict.keys(): # Iteration of keys in the dictionary using for loop
  print(key)


for value in thisdict.values(): # Iteration of values in the dictionary using for loop
  print(value)

for key, value in thisdict.items(): # Iteration of key values pairs in the dictionary
  print(key , value)