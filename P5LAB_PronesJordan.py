#Your Name: Jordan Prones

# Date: 20 Apr 24

# Assignment Name: P5LAB

# A brief description of the project: Create a program and define a function using Leap Year.

#Define and call number of days in in february.

def days_in_feb(user_year):
    leap_year = 29              #Leap year is defined in 29 days.
    reg_year = 28               #Regular year is defined in 28 days.

#Create branch/loop statement that determines a leap year.
    #Ensure year is divisible by 4 and 400 but not divisible by 100.
    
    if (user_year % 4 == 0 and user_year % 100 != 0) or (user_year % 400 == 0):
        return leap_year

    else:
        return reg_year

#Execute string as a script and output the following: ("'Year' has 'Number of Days' days in February.").
    
if __name__ == '__main__':
    user_year = int(input('Enter year: '))
    days_print = days_in_feb(user_year)

    print(f'{user_year} has {days_print} days in February.')
