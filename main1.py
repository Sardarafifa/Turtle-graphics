import turtle as t
import random

t.colormode(255)

directions=[0,90,180,270]
my_turtle=t.Turtle()

my_turtle.pensize(15)
my_turtle.speed("fast")
def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    randomcolor= (r,g,b)
    return randomcolor

for _ in range(200):
    my_turtle.forward(30)
    my_turtle.setheading(random.choice(directions))
    my_turtle.color(random_color())
