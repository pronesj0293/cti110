#Name: Jordan Prones

#Date: 3 Mar 2024

#Assignment Name: P2LAB2

#A brief description of the project: LAB: Simple Statistics using Types


#Retrieve user input using float().

num1 = float(input('Enter number: '))
num2 = float(input('Enter number: '))
num3 = float(input('Enter number: '))
num4 = float(input('Enter number: '))

#Use conversion specifiers to output averages

avg_grade = num1 * num2 * num3 * num4 
avg_grade2 = num1 + num2 + num3 + num4
avg_grade2 = avg_grade2 / 4

#Print output average with two rounded interger and two floating-point with three digits after the decimal point.

print(f'{avg_grade:.0f} {avg_grade2:.0f}')
print(f'{avg_grade:.3f} {avg_grade2:.3f}')
