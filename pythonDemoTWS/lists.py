# Two way to create list in python
# 1) using []
# 2) using list() object

# [] is more faster than list() --->>>>

fruits = [1,34.4,True,"Surya",'kant']

print(fruits)


names=list()
print(type(names))

# "Operations on lists"

list_of_players=[]
list_of_players.append("Virat") # Append-> Add items to the end of the list
list_of_players.append("Kohli")
list_of_players.append("Rohit")

print(list_of_players)

list_of_players.clear()  #Clear-> It will clear/empty the list
print(list_of_players)

nums=[1,2,2,3,2,4,5,2,44,5,5,6,5,7,2]
print(nums.count(2)) # Count-> it will count the frequrency appear of specific item

nums2=[1,3,500,4000]
nums.extend(nums2) # extends->This methos add/append the all items of another list to the current list
print(nums)

 # print(dir(nums)) # dir-> It will print all the operations we can operate on the given list

list_of_star=["Salmon", "King Khan" , "Ranbir","Ranbeer"]
print(len(list_of_star)) # len-> length of the list

for star in list_of_star: # iterartion using for loop
    print(star)

for i in range(0,len(list_of_star)):
    print(list_of_star[i])    