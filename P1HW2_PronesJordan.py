#Name: Jordan Prones

#Date: 21 Feb 2024

#Assignment Name: P1HW2

#A brief description of the project: Basic math program for travel expenses.

#Retrieve the number user wants to use during travel into the variable budget.

budget = int(input('Enter Budget: '))

print()

#Retrieve the location of the travel destination.

location = input('Enter your travel destination: ')

print()

#Retrive predetermined travel expense variable for fuel, accomodations, and food.

fuel = int(input('How much do you think you will spend on gas? '))

print()

accomodations = int(input('Approximately, how much will you need for accomodation/hotel? '))

print()

food = int(input('Last, how much do you need for food? '))

print()

#Print the generated information gathered above.

print('------------Travel Expenses------------')
print('Location:', location)
print('Initial Budget:', budget)

print()

print('Fuel:', fuel)
print('Accomodation:', accomodations)
print('Food:', food)

print()

#Print the remaining balance of the budget.

print('Remaining Balance:', budget - fuel - accomodations - food)


