# Q1. Write a program that asks user for their age and tells the users:
# - Over age when the user's age is more than 39
# - Under age when the user's age is less than 18
# - Proper age when the user's age is between 18 and 39

age = input("How old are you: ")
age = int(age)
if age > 39:
    print("Over age")
elif age < 18:
    print("Under age")
else:
    print("Proper age")