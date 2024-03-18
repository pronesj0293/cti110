# Name: Jordan Prones

# Date: 16 Mar 2024

# Assignment Name: P3LAB

# A brief description of the project: Create a program using branching.

# Create string to retrieve the year from user input using intergers. 

input_year = int(input('Enter year: '))

# Ensure year is divisible by 4 and 400 but not divisible by 100.
# Then output "- leap year" if input is divisible by 4 and 400.

if (input_year % 4 == 0 and input_year % 100 != 0) or (input_year % 400 == 0):
    print(input_year, '- leap year')

# Output "- not a leap year" if divisible by 100.

else:
    print(input_year, '- not a leap year')
