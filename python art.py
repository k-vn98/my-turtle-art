"""
Check out the official docs here: https://docs.python.org/3/library/turtle.html
"""
# I HEREBY DUB THEE : The Hope In An Abyss



#Imports
from turtle import * 
import turtle
from random import randint
#Turtles n' Settings
bob = turtle.Turtle()
bob.speed(6)
wn = turtle.Screen()
wn.bgcolor(('#242424')) #the rgb format doesnt work

#↓Function(s)↓
def jump(t,x,y):
  t.penup()
  t.goto(x,y)
  t.pendown()
def polygon(turtle,sides, distance):
  angle = 360/sides
  for i in range(sides):
    turtle.forward(distance)
    turtle.right(angle)
#↑Funtion(s)↑
#↓Code↓

#This Is a abyss/void
#Stripes  40 random instances of lines
bob.color('#757575')
bob.speed(0)
for i in range(40):  
  anglechoice = randint(1,4)
  if anglechoice == 1:
    bob.setheading(45)
  elif anglechoice == 2:
    bob.setheading(-45)
  elif anglechoice == 3:
    bob.setheading(90)
  elif anglechoice == 4:
    bob.setheading(0)
  x = randint(-300,300)
  y = randint(-160,160)
  jump(bob,x,y)
  bob.forward(10)
#Random Shapes 
bob.speed(0)
for i in range(10): #10 random instances of triangles
  x = randint(-300,300)
  y = randint(-160,160)
  jump(bob,x,y)
  r = randint(0,360)
  bob.setheading(r)
  polygon(bob,3,10)
for i in range(2): #2 random instances of squares
  x = randint(-300,300)
  y = randint(-160,160)
  jump(bob,x,y)
  r = randint(0,360)
  bob.setheading(r)
  polygon(bob,4,10)


  
#The "Hope"
bob.speed(6)
jump(bob,0,-50)
bob.setheading(45)
bob.pensize(8)
bob.begin_fill()
for i in ['#940000', '#006611', 'gold', '#000094']: 
  bob.color(i)
  bob.forward(75)
  bob.left(90)
bob.color('black','white')
bob.end_fill()

#The +
bob.color('#e5e5e5')
jump(bob,0,-10)
bob.setheading(90)
bob.forward(20)
jump(bob,-10,0)
bob.setheading(0)
bob.forward(20)

bob.ht() #Turtle Disappears!

turtle.done() #Keeps the window open