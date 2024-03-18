# Your Name: Jordan Prones

# 16 Mar 2024

# Assignment Name: P3HW1

# A brief description of the prgram: Buiding upon List assignment, fix the program and finish the code.

# This program takes a number grade, determines average and displays letter grade for average.

# Enter grades for six modules using floating-input.

mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

# Add grades entered to a list.

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

# Determine lowest, highest, sum, and average using grades list.

print()
print('------------Results------------')
print(f'Lowest Grade:       {min(grades)}')
print(f'Highest Grade:      {max(grades)}')
print(f'Sum of Grades:      {sum(grades)}')
print(f'Average:            {sum(grades)/ 6:.2f}')
print('----------------------------------------')

# Determine average by dividing sum of grades and the number of modules. 

avg = sum(grades) / len(grades)

# Determine letter grade based on average score output 'Your grade is: (the letter grade)'.

if avg >= 90:
    print('Your grade is: A')
    
elif avg >= 80:
    print('Your grade is: B')

elif avg >= 70:
    print('Your grade is: C')

elif avg >= 60:
    print('Your grade is: D')
    
else:
    avg >= 0
    print('Your grade is: F')




