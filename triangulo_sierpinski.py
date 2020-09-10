'''
n = numero de copias
s = factor de reduccion

en un cuadrado de dimension 2, si le aplicamos un factor de division de 3, el numero de copias sera de 9, entonces:
n = s°D
log n = D * log S
D = log n / log s
'''


import turtle
import random
import math
from copy import deepcopy

#Coordenadas & Plano
###########################################################################

turtle.setup(width=500,height=500)
turtle.bgcolor("white")
turtle.hideturtle()
turtle.speed(100)

coords = []

for x in range(500):
    for y in range(500):
        coords.append([-250+x,-250+y])


plano = [[0,250],[0,-250],[250,0],[-250,0]]

for x in range(4):
    turtle.goto(plano[x])
    turtle.penup()
    turtle.goto(0,0)
    turtle.pendown()

turtle.penup()

p0 = random.choice(coords)
p1 = random.choice(coords)
p2 = random.choice(coords)
p3 = random.choice(coords)
#p1 = [0,250]
#p2 = [250,0]
#p3 = [-250,0]
iterations = 10000

points = [p0, p1, p2, p3]

for x in range(4):
    turtle.goto(points[x])
    if x == 0:
        turtle.dot(5)
    elif x == 1:
        turtle.dot(5, "red")
    elif x == 2:
        turtle.dot(5, "green")
    else:
        turtle.dot(5, "blue")

###########################################################################

def middle_dot(position):

    global p0
    mitad = (math.hypot(p0[0] - position[0], p0[1] - position[1])/2)
    myradians = math.atan2(p0[1]-position[1], p0[0]-position[0])
    mydegrees = math.degrees(myradians)

    if position[1] > p0[1] and position[0] > p0[0] or position[1] > p0[1] and position[0] < p0[0]:
        if mydegrees < 0:
            turtle.left(mydegrees)
        else:
            turtle.right(mydegrees)

    elif position[1] < p0[1] and position[0] > p0[0] or position[1] < p0[1] and position[0] < p0[0]:
        if mydegrees < 0:
            turtle.right(mydegrees)
        else:
            turtle.left(mydegrees)

    turtle.forward(mitad)
    tpos = turtle.position()
    p0 = deepcopy(tpos)
    turtle.dot(3, "green")
    
for x in range(iterations):
    dice = random.choice(["1", "2", "3"])
    #print(dice, p0)
    if dice == "1":
        turtle.setheading(0)
        turtle.goto(p1)
        middle_dot(p1)

    elif dice == "2":
        turtle.setheading(0)
        turtle.goto(p2)
        middle_dot(p2)
    else:
        turtle.setheading(0)
        turtle.goto(p3)
        middle_dot(p3)

print("The painting is done!!")
turtle.done()
