#Name: Jordan Prones

#Date: 1 Apr 2024

#Assignment Name: P4LAB1A

#A brief description of the project: Draw two shapes, a square and a triangle using a 'for' or 'while' loop.

#Import the turtle feature to use this function.
import turtle               
wn = turtle.Screen()        #Create a separate turtle screen. 
wn.title("Greg & Tyler")    #Create title to differentiate the different shapes.

greg = turtle.Turtle()      #Create greg with or without attributes.
tyler = turtle.Turtle()      #Create alex with or without attributes.

for q in range(3):          #Create a triangle for greg.
    greg.forward(80)        
    greg.left(120)

for r in range(4):          #Create a square for tyler going the opposite direction.
    tyler.backward(50)      
    tyler.right(90)

wn.mainloop()               #Allow turtle screen to stay open until user closes screen.
