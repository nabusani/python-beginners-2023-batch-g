# 1. Create a variable to hold "A2Z"
v = "A2Z"
print(v)
# 2. Create a new string to hold the middle item from the above string
m = v[1:2]
print(m)
# 3. Create a tuple of the two strings above
t = v, m
print(t)
# 4. Create a list to hold the items from the above tuple
l = []
l.extend(t)
print(l)
# 5. Add two boolean values to the end of the new list one for true the other for false
l.append(True)
l.append(False)
print(l)
# 6. Create an integer to store the current year
i = 2023
print(i)
# 7. Create a float to store your exagerated weight
w = 95.9
print(w)
# 8. Add the above integer and float to the previous list
l.append(i)
l.append(w)
print(l)
# 9. Create a new list to hold the last 4 items from the old list
nl = l[-4:]
print(nl)
# 10. Reverse the new list with a method and reverse it back without a method
nl.reverse()
print(nl)
nl = nl[::-1]
print(nl)