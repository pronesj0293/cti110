#Name: Jordan Prones

#Date: 8 Apr 2024

#Assignment Name: P4LAB1B

#A brief description of the project: Draw initials using a 'for' or 'while' loop.

#Import the turtle feature to use this function.
import turtle               
wn = turtle.Screen()        #Create a separate turtle screen. 
wn.title("Greg")            #Create a title.

greg = turtle.Turtle()      #Create greg with attributes.
greg.color("blue")
greg.pensize(6)

greg.right(90)              #Create first initial.
greg.forward(200)
greg.right(90)        
greg.forward(100)
greg.right(90)
greg.forward(50)
greg.backward(50)
greg.right(90)
greg.forward(100)

greg.penup()                #lift pen and put down to start next initial.
greg.forward(50)
greg.pendown()
greg.left(90)
greg.forward(200)

for f in range(4):          #Simplify code if needed to finish initial.
    greg.right(90)
    greg.forward(100)


wn.mainloop()               #Allow turtle screen to stay open until user closes screen.

