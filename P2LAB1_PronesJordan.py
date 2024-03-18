#Name: Jordan Prones

#Date: 29 Feb 2024

#Assignment Name: P2LAB1

#A brief description of the project: LAB: Driving Costs touching on Variables and Expressions

# Retrieve user input in miles per gallon and cost per gallon.

miles_gallon = float(input('Enter miles: '))
dollars_gallon = float(input('Enter cost: '))

#Determine cost per gallon based on distance.

gas_milage1 = (dollars_gallon * 20) / miles_gallon
gas_milage2 = (dollars_gallon * 75) / miles_gallon
gas_milage3 = (dollars_gallon * 500) / miles_gallon

#Print information based on set values.

print(f'{gas_milage1:.2f} {gas_milage2:.2f} {gas_milage3:.2f}')
