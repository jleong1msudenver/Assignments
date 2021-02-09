# Take a string as input for a name and a string for course number and outputs a welcome message.
# For example: if the input name is “Jane” and the course name is “CS 1030”, the output is: “Welcome, Jane, to course CS 1030!” 

# # Capture input for name of student that is assigned to variable student_name
# student_name = str(input("What is your name?"))
# # Capture input for course number that is assigned to variable course_number
# course_number = int(input("Enter your Course Number:"))
# # Full print statement with input variables in correct places of sentence
# print("Welcome", student_name, "to course", "CS", course_number,"!")

# 2nd Assignment
# Take a string as input, say input_string, then print the first 2 and the last 2 characters in the string. 
# Assume the input string is 2 or more characters. The print should look like:
#  "The first 2 characters are: "the first 2
#  "The last  2 characters are: "the last 2
input_string = str(input("Give a string here:"))
# Assign variable to sliced string from input starting at 0 position to position 2 
# so we get the first two letters only
first2_char = input_string[0:2]
# Add print statement with variable first2_char replaced with input
print("The first 2 characters are: ", first2_char)
# Assign variable to sliced string from input working backwards from end -2 times
last2_char = input_string[-2:]
# Add print statement with variable last2_char replaced with input
print("The last 2 characters are: ", last2_char)