# Your Name: Jordan Prones

# Date: 11 Apr 24

# Assignment Name: P4HW2

# A brief description of the project: Create a program that calculates pay for multiple employees.

#Create the following definitions: regular hourly pay, overtime pay, overtime, gross pay, number of employees.
#Create an input that allows users to enter employee name or Done to terminate loop, 'Enter employee's name or "Done" to terminate:'.

reg_hour_pay = 0
ot_pay = 0
over_time = 0
gross_pay = 0
num_employee = 0
overtime_pay = 0
reg_pay = 0

employee_name = input('Enter employee\'s name or "Done" to terminate: ')

#Create a loop that will require input of number of hours worked, and pay rate from user.

while employee_name != 'Done':
    num_hours = float(input(f'How many hours did {employee_name} work? '))
    pay_rate = float(input(f'What is {employee_name}\'s pay rate? '))
    num_employee += 1

#Create if/else statement to determine overtime, overtime pay, regular hourly pay, and gross. 

    if num_hours <= 40:
        over_time = 0
        ot_pay = 0
        reg_hour_pay = pay_rate * num_hours
        gross = num_hours * pay_rate
    
    else:
        over_time = num_hours - 40
        ot_pay = over_time * pay_rate * 1.5
        reg_hour_pay = pay_rate * 40
        gross = reg_hour_pay + ot_pay

#Add variables.

    gross_pay += gross
    overtime_pay += ot_pay
    reg_pay+= reg_hour_pay

#Output the following after each employee entered: Hours Worked, Pay Rate, OverTime, OverTime Pay, RegHour Pay, and Gross Pay.
#Output number amount based on information above.

    print()
    print('Employee name:   ', employee_name)
    print()
    print('Hours Worked   Pay Rate    OverTime    OverTime Pay        RegHour Pay         Gross Pay')
    print('--------------------------------------------------------------------------------------------------')
    print(f'{num_hours:<14.1f} {pay_rate:<11.2f} {over_time:<11.1f} {ot_pay:<19.2f} ${reg_hour_pay:<18.2f} ${gross:<18.2f}')
    print()
    print()
    employee_name = input('Enter employee\'s name or "Done" to terminate: ')

#Output total numbers based on number of employees entered using the following information; number of employees, overtime pay, regular pay, and gross pay.

print()
print(f'Total number of employees entered:  {num_employee}')
print(f'Total amount paid for overtime:  ${overtime_pay:.2f}')
print(f'Total amount paid for regular hours:  ${reg_pay:.2f}')
print(f'Total amount paid for gross:  ${gross_pay:.2f}')


    
