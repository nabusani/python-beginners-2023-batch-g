# print - Print results to terminal
print(1+2)

# len - used to check the length of an iterable - string, list, tuple, dict
print("\n")
print(len("Ahmad"))
print(len(["Ahmad", "Ibrahim"]))
print(len((1, 2, 3)))
print(len({"name":"Ibrahim", "age":16}))

# type - used to check the type of data
print("\n")
print(type(1))
print(type(1.1))
print(type("1.1"))
print(type(["1.1", 1, 1.1]))
print(type(("1.1", 1, 1.1)))
print(type({"a":'A', "b":"B"}))

# input - used to collect user input from the terminal
print("\n")
# name = input("What is your name please: ")
# print("Great, welcome on board "+name)

# int - used to convert compatible data to integer
print("\n")
a = "1"
print(a+"1")
print(type(a))
a = int(a)
print(a+1)
print(type(a))

b = int("400")
print(b)
print(type(b))

# str - used to convert data to string type
print("\n")
a = [1, 2, 3]
print(a[0])
print(a+[1])
print(type(a))
a = str(a)
print(a+"ahmad sani"+",something, else")
print(a[0])
print(type(a))

# list - converts a compatible data to a list
print("\n")
a = (1, 2, 3)
a = list(a)
print(a)
b = {'name':'Ahmad', 'age':10}
b = list(b.items())
print(b)

# tuple - converts a compatible data to a tuple
print("\n")
a = [1, 2, 3]
a = tuple(a)
print(a)
b = {'name':'Ahmad', 'age':10}
b = tuple(b.items())
print(b)

# dict - it create a new dictionary
print("\n")
a = dict([("name", "Abba"), ("age", 19)])
print(a)

# bool - used to convert compatible data type to a boolean
print("\n")
t = "0"
print(t)
print(type(t))
t = bool(t)
print(t)
print(type(t))