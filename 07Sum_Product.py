# 07 Sum/Product Program
# Due Thursday by 11:59pm Points 5 Submitting a file upload
# Write a Python program that reads two integers from the user, 
# calculates the sum and product of the two numbers, and prints
# them on one line with messages identifying each calculated number.

# [X] Input two integers from user
# [X] calculates sum and product of two numbers
# [X] print on one line with messages identifying calculated number.
# [X] refactor for less code
# [X] All tasks complete WAHOO!

# Capture input for first typed input
int1 = int(input("Enter an integer:"))
# Capture input from second typed input
int2 = int(input("Enter a second integer:"))
# Add inputs together to equal sum
sum = int1 + int2
# Multiply inputs together to equal product
product = int1 * int2
# Complete print statement on one line for both addition and multiplication
print('The sum of', int1, '+', int2, '=', sum, 'and the product of', int1, '*', int2, '=', product)