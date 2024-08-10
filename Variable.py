# Python Variable
# 1
x = 5
y = "John"
print(x)
print(y)
# 2
x = 4
x = "sally"
print(x)
# 3
x = str(3)
print(type(x))
X = float(3)
print(type(X))

# Python Variables - Assign Multiple Values
# 1
x, y, z, = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
# 2
x = y = z = "Orange"
print(x, y, z)
# 3
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x, y, z)

# Python - Output Variables
# 1
x = "Python is awesome"
print(x)
# 2
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)
# 3
x = 5
y = 10
print(x + y)
# 4
x = 5
y = "John"
print(x, y)

# Global Variables
# 1
x = "awesome"


def myfunc():
    x = "fantastic"
    print("Python is " + x)


myfunc()
print("Python is " + x)
# 2
x = "awesome"


def myfunc():
    global x
    x = "fantastic"


myfunc()
print("Python is " + x)