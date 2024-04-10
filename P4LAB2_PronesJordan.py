#Name: Jordan Prones

#Date: 6 Apr 2024

#Assignment Name: P4LAB2

#A brief description of the project: Using range() and Loops, output with increments of 5.

#Recieve two interger data inputs from user.
first_num = int(input('Enter first number: '))
second_num = int(input('Enter second number: '))

#Second integer must not be less than the first integer. Output 'Second integer can't be less that the first.' if true.
if second_num < first_num:
        print(f'Second integer can\'t be less than the first.', end='')
        
#Using for loop and range, take first integer and increment by 5 staying less than or equal to the second interger.
for i in range(first_num, second_num + 1, 5):
    print(i, end=' ')           #Output data

print()
