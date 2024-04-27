#Your Name: Jordan Prones

# Date: 26 Apr 24

# Assignment Name: P5HW

# A brief description of the project: Create a math quiz using fuctions.

#Import random numbers.

import random

#Output greating and define a main menu that includes Adding and Subtracting random numbers and exit.

print('Welcome to Math Quiz')

def main_menu():
    print()
    print('MAIN MENU')
    print('--------------------')
    print('1. Adding Random Numbers')
    print('2. Subtracting Random Numbers')
    print('3. Exit')
    print()

    return choices()

#Define the numbers that correspond to the apropriate choices.

def choices():
    while True:
        choice = input('Please choose one of the menu options: ')
        
        if choice == '1':
            add_math_quiz()
            
        elif choice == '2':
            sub_math_quiz()
            
        elif choice == '3':
            print('Thank you for playing...')       #Add farewell note when '3' is entered.
            print('Bye!!')
            break

        else:
            print('Invalid input.. Please select from options 1, 2, or 3.')     #Add Invalid note when choices other than 1,2 or 3 are entered.
            choice = input('Please choose one of the menu options: ')
            print()
        return

#Define the random addition equation and ensure 

def add_math_quiz():
    rand_number1 = random.randint(1, 250)
    rand_number2 = random.randint(1, 250)
    equation = rand_number1 + rand_number2
    answer = int(input(f' {rand_number1}\n+{rand_number2}\n\nEnter answer.\n'))
    num_answer = 1
    
    while answer != equation:
        if answer < equation:
            print('Sorry, guess is too low.')   #Output note if answer is too low.
            print()
            
        else:
            print('Sorry, guess is too high.')  #Output note if answer is too high.
            print()
            
        answer = int(input('Try again: '))      #output note to try again.
        num_answer +=1

#Output congratulations and number of guesses it took to answer correctly.
            
    print('Congratulations!!!! Your answer is correct.')
    print(f'Number of guesses:', num_answer)

    return main_menu()

#Define the random addition equation and ensure

def sub_math_quiz():
    rand_number1 = random.randint(1, 250)
    rand_number2 = random.randint(1, 250)

    if rand_number1 < rand_number2:     #Create statement that will ensure lowest number is always at the bottom of the equation.
        rand_number1, rand_number2 = rand_number2, rand_number1
        
    equation = rand_number1 - rand_number2
    answer = int(input(f' {rand_number1}\n-{rand_number2}\n\nEnter answer.\n'))
    num_answer = 1

    while answer != equation:
        if answer < equation:
            print('Sorry, guess is too low.')   #Output note if answer is too low.
            print()
            
        else:
            print('Sorry, guess is too high.')  #Output note if answer is too high.
            print()
            
        answer = int(input('Try again: '))      #output note to try again.
        num_answer += 1

#Output congratulations and number of guesses it took to answer correctly.
            
    print('Congratulations!!!! Your answer is correct.')
    print(f'Number of guesses:', num_answer)

    return main_menu()

#Execute string as a script

if __name__ == '__main__':
    main_menu()
    
