name="suryakant"

print(name)

print(len(name))

print(name[0])

print(name[0:4])  # Slice of string

"""
slice() Syntax
The syntax of slice() is:

slice(start, stop, step)
- start (optional) - Starting integer where the slicing of the object starts. Default to None if not provided.
- stop - Integer until which the slicing takes place. The slicing stops at index stop -1 (last element).
- step (optional) - Integer value which determines the increment between each index for slicing. Defaults to None if not provided.

"""
print(name[0:9:2])
print(name[7:-1])
print(name[::-1]) # Reverse the string