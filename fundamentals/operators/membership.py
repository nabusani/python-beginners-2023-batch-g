# Membership operator is used to check for the existance of a certain data in another
# It is also returns boolean.

numbers = [1, 2, 3, 4, 5, 6]
print(1 in numbers)
print(15 in numbers)
print(1 not in numbers)
print(15 not in numbers)

print("\n")

name = "Aliyu"
print("i" in name)
print("a" in name)
print("A" in name)

print("\n")

person = {"name":"Said", "age":19, "height":1.9, "weight":85.6}
print(19 in person)
print("age" in person)