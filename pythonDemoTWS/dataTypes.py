apples = 50  # Int

marks = 89.45  # Float

name = "Surya kant"  # String

is_raining = False  # Boolean

print(type(name))
print(type(marks))
print(type(apples))
print(type(is_raining))


# type Casting (Two types)
  # a) Implicit Type Conversion:- In this, method, Python converts the datatype into another datatype automatically. Users don’t have to involve in this process. 

# Eg. - 
print("Implicit Type Conversion---------")
a=7
b=4.0
c=a+b
print(type(c))
       

# b) Explicit Type Conversion:- In this method, Python needs user involvement to convert the variable data type into the required data type. 
# eg. - 
x=5 #int
n=float(x)
print(type(n)) # output:- Float
