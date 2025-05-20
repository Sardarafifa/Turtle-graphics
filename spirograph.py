import turtle as t
import random

t.colormode(255)

my_turtle=t.Turtle()

my_turtle.speed("fastest")
def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    randomcolor= (r,g,b)
    return randomcolor

#def spirograph(size_of_gap)
   
def spirograph(size_of_gap):
   for _ in range(int(360/size_of_gap)):      
       my_turtle.color(random_color())
       my_turtle.circle(100)
       my_turtle.setheading(my_turtle.heading()+ size_of_gap)

spirograph(5)

screen=t.Screen()
screen.exitonclick()
