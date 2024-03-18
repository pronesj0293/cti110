#Your Name: Jordan Prones

#Date: 8 Mar 2024

#Assignment Name: P2HW2

#Brief Description of program: Create a program using basic List functions. 


#Recieve user input on grades for the following tests using floating-input.

module1 = float(input('Enter grade for Module 1: '))

module2 = float(input('Enter grade for Module 2: '))

module3 = float(input('Enter grade for Module 3: '))

module4 = float(input('Enter grade for Module 4: '))

module5 = float(input('Enter grade for Module 5: '))

module6 = float(input('Enter grade for Module 6: '))


#Create a descriptive name for each input and combine together to make a singular list.

grade_list = [module1, module2, module3, module4, module5, module6]


#Display the results using the following categories: Lowest Grade, Highest Grade, Sum of Grades, and Average(usig two digits after the decimal).
print()
print('------------Results------------')
print(f'Lowest Grade:       {min(grade_list)}')
print(f'Highest Grade:      {max(grade_list)}')
print(f'Sum of Grades:      {sum(grade_list)}')
print(f'Average:            {sum(grade_list)/ 6:.2f}')
print('----------------------------------------')
