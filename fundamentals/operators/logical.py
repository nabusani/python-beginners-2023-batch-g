# Used for performing logic - a way to chain multiple conditions

print(1 > 0 and 10 < 5)
print(10 in [1, 2, 3] and 10 > 5)
print(1 < 0 and 10 < 5)

print(1 > 0 or 10 < 5)
print(1 > 0 or 10 > 5)
print(1 < 0 or 10 < 5)

print("\n")
print(not 1 < 0 or not 10 < 5)
print(not 1 > 0 and not 10 < 5)

print("\n")
print(True or False)
print(True and False)
print(5 or 1)
print(5 and 1)