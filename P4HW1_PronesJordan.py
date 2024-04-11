#Your Name: Jordan Prones

#Date: 11 Apr 2024

#Assignment Name: P4HW1

#Brief Description of program: Building upon P2HW2 while using loops. 


#Recieve user input on scores.

num_score = int(input('How many scores do you want to enter? '))
print()

#Create a loop that will collect the scores and ensure all scores are between 0 - 100.

mod_list = []
i = num_score + 1

for i in range(num_score):
    i += 1
    stu_score = float(input(f'Enter score #{i}:'))
    if stu_score > -1 and stu_score < 101:
        mod_list.append(stu_score)

#If scores are not between 0 and 100, output the following; 'INVALID Score entered!!!!', 'Score should be between 0 and 100' and, 'Enter score #... again'.

    else:
        print()
        print(f'INVALID Score entered!!!!')
        print(f'Score should be between 0 and 100')
        stu_score = float(input(f'Enter score #{i} again: '))
        mod_list.append(stu_score)

#Determine lowest and average scores.

lowest = min(mod_list)
average = sum(mod_list) / 5

#Determine letter grade based on average score.

if average >= 90:
    grade = 'A'
    
elif average >= 80:
    grade = 'B'

elif average >= 70:
    grade = 'C'

elif average >= 60:
    grade = 'D'
    
else:
    average >= 0
    grade = 'F'
print()

#Display the results using the following categories: Lowest Score, Modified List, Scores Average, and Grade.

print()
print('--------------Results-----------')
print(f'Lowest Score  : {(lowest)}')
mod_list.remove(lowest)                             #Remove lowest from mod_list to get an accurate average.
print(f'Modified List : {(mod_list)}')
print(f'Scores Average: {sum(mod_list) / 4:.2f}')   #Ensure two decimal points.
print(f'Grade         : {(grade)}')
print('----------------------------------')

