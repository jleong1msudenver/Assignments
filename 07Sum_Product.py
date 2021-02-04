# 07 Sum/Product Program
# Due Thursday by 11:59pm Points 5 Submitting a file upload
# Write a Python program that reads two integers from the user, 
# calculates the sum and product of the two numbers, and prints
# them on one line with messages identifying each calculated number.

# [X] Input two integers from user
# [ ] calculates sum and product of two numbers
# [ ] print on one line with messages identifying calculated number.

# Capture input for first typed input
integer1 = int(input("Enter an integer:"))
# Capture input from second typed input
integer2 = int(input("Enter a second integer:"))
# Add inputs together to equal sum
sum = integer1 + integer2
product = integer1 * integer2
print(sum)
print(product)
print('The sum of', integer1, '+', integer2, 'equals:', sum)