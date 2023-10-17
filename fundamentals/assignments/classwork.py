# Q1. Create a variable to hold the string "AHMAD" and change all occurances of
# "A" with "O"

name = "AHMAD"
name = name.replace("A", "O")
print(name)

# Q2. Create an empty list and append all items in the above variable using the
# appropraite list method
chars = []
chars.extend(name)
print(chars)

# Q3. Using list slicing, get the first two characters from the list above
# Q4. Without using the reverse method, reverse the list above