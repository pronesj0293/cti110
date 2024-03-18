# Your Name: Jordan Prones

# Date: 17 Mar 24

# Assignment Name: P3HW2_Salary

# A brief description of the project: Create a program that calculates pay.


# Create the following inputs: employee name, number of hours worked, and pay rate.

employee_name = input("Enter employee's name: ")

num_hours = float(input('Enter number of hours worked: '))

pay_rate = float(input("Enter employee's pay rate: "))


# Create calculations that portray the overtime hours, overtime pay (using 1.5 hours for time and a half), regular pay rate.

over_time = num_hours - 40

ot_pay = over_time * pay_rate * 1.5

reg_hour_pay = pay_rate * 40

# Output employee name.

print('-------------------------------------')
print('Employee name: ', employee_name)
print()

# Create an if-else statement that will capture the gross pay based on number of hours worked. Example, overtime vs. no overtime.

if num_hours <= 40:
    gross = reg_hour_pay * pay_rate

else:
    gross = reg_hour_pay + ot_pay


# Output the following: Hours Worked, Pay Rate, OverTime, OverTime Pay, RegHour Pay, and Gross Pay.
# Output number amount based on information above.

print('Hours Worked   Pay Rate    OverTime    OverTime Pay        RegHour Pay         Gross Pay')
print('--------------------------------------------------------------------------------------------------')
print(f'{num_hours:<14.1f} {pay_rate:<11.1f} {over_time:<11.1f} {ot_pay:<19.2f} ${reg_hour_pay:<18.2f} ${gross:<18.2f}')
