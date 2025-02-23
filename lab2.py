import re

# Question 1 :
# Write a simple calculator program using match to perform addition, subtraction, multiplication, and division.
# operation = "add"
# a, b = 10, 5
# # Expected Output: 15

operation = input("Enter your needed operation from the following: add, sub, mul, div: ")
x=int(input("Enter your 1st argument: "))
y=int(input("Enter your 2nd argument: "))
match operation:
    case 'add':
        print(f"{x} + {y} = {x+y}")
    case 'sub':
        print(f"{x} - {y} = {x-y}")
    case 'mul':
        print(f"{x} * {y} = {x*y}")
    case 'div':
        print(f"{x} / {y} = {x/y}")

# Question 2 :
# Write a program to filter out even numbers from a list and count how many are left.
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # Expected Output: [1, 3, 5, 7, 9], Count = 5

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers = [num for num in numbers if num % 2 != 0]
print(numbers)
print("Count= ",len(numbers))

# Question 3 :
# Write a program to check if a password meets the following criteria:
# - At least 8 characters long.
# - Contains at least one uppercase letter.
# - Contains at least one digit.
# password = "Pass1234"
# # Expected Output: "Valid Password"
password = input('''Enter password that meets the following criteria:\n
                 # - At least 8 characters long.\n
                 # - Contains at least one uppercase letter.\n
                 # - Contains at least one digit.
                 ''')
if len(password) < 8:
    print("Your password is too short, it must have min length = 8")
elif not re.search(r'[A-Z]', password):
    print("Password should have at least an uppercase character")
elif not re.search(r'\d', password):
    print("Password should have at least 1 digit")
else:
    print("Valid password!")

# Question 4: 
# Write a Python script to concatenate the following dictionaries to create a new one.
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# Sample Dictionary :
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}

newDict = {**dic1,**dic2,**dic3}
print(newDict)


# Question 5: 
# takes a string and prints the longest
# alphabetical ordered substring occured.
# For example, if the string is 'abdulrahman' then the output is:
# Longest substring in alphabetical order is: abdu
def longest_alphabetical_substring(s):
    curr = ""
    longest = ""
    for i in range(len(s)):
        if i == 0 or s[i] >= s[i - 1]: 
            curr += s[i]
        else:
            if len(curr) > len(longest):
                longest = curr
            curr = s[i]
    return longest
print(longest_alphabetical_substring('abdulrahman'))

# Question 6:
# Write a program to check if a Email meets the following criteria:
# - Ensures the email follows a standard format (e.g., local@domain.com).
# - Does not check if the email actually exists or is deliverable.
email = input("Enter your email\n\t")
if re.match(r'^[a-zA-Z0-9_.]+@[a-z]+\.[a-z]{2,}$', email):
    print("Valid Email")
else:
    print("Invalid Email")