#Name: Jordan Prones

#Date: 7 Mar 2024

#Assignment Name: P2HW1

#A brief description of the project: Building upon basic math program for travel expenses.

#Retrieve the number user wants to use during travel into the variable budget.

budget = float(input('Enter Budget: '))

print()

#Retrieve the location of the travel destination.

location = input('Enter your travel destination: ')

print()

#Retrive predetermined travel expense variable for fuel, accomodations, and food.

fuel = float(input('How much do you think you will spend on gas? '))

print()

accomodations = float(input('Approximately, how much will you need for accomodation/hotel? '))

print()

food = float(input('Last, how much do you need for food? '))

print()

#Print the generated information gathered above.

print('------------Travel Expenses------------')
print('Location:          ',location)
print(f'Initial Budget:     ${budget:.2f}')
print(f'Fuel:               ${fuel:.2f}')
print(f'Accomodation:       ${accomodations:.2f}')
print(f'Food:               ${food:.2f}')
print('----------------------------------------')

print()
#Print the remaining balance of the budget.

print(f'Remaining Balance:${budget - fuel - accomodations - food:.2f}')


