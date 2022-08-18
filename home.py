#house drawing in Pytohn
from turtle import *
import turtle 
speed(8)
hideturtle()
width(4)

def rel_pos(x,y):
    penup()
    goto(pos()+(x,y))
    pendown()
    
def roof():
    width(8)
    begin_fill()
    fillcolor("#cc6600")
    seth(180)
    fd(200)
    seth(-120)
    fd(100)
    seth(0)
    fd(200)    
    end_fill()
    seth(60)
    fd(100)
    
    seth(-60)
    fd(100)
    width(4)
    seth(180)
    fd(100)
      
def Walls():
    seth(-90)
    fd(120)
    seth(180)
    fd(200)
    seth(90)
    fd(120)
    seth(0)
    fd(300)
    seth(-90)
    fd(120)
    seth(180)
    fd(100)
    
def Door():
    color("#004080")
    width(5)
    fd(80)
    begin_fill()
    fillcolor("red")
    seth(90)
    fd(80)
    seth(180)
    fd(40)
    seth(-90)
    fd(80)
    end_fill()
    
    rel_pos(25,40)
    width(4)
    circle(5)
    
    
def Window():
    begin_fill()
    color("#004080")
    fillcolor("#336699")
    seth(-90)
    width(5)
    fd(15)
    seth(180)
    fd(30)
    seth(90)
    fd(30)
    seth(0)
    fd(30)
    seth(-90)
    fd(15)    
    end_fill()
    width(2)
    seth(180)
    fd(30)
    backward(15)
    seth(90)
    fd(15)
    backward(30)
 
    
def House():
    roof()
    Walls()
    Door()
    rel_pos(-50,0)
    Window()
    rel_pos(135,15)
    Window()
    rel_pos(105,25)
    Window()
    rel_pos(-250,250)
    done()
    
House()
