# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 12:45:27 2017

@author: Bidish
"""

import turtle

def dia_draw(a_turtle): 
    
    a_turtle.speed(10)
    a_turtle.forward(50)
    a_turtle.right(30)
    a_turtle.forward(50)
    a_turtle.right(150)
    a_turtle.forward(50)
    a_turtle.right(30)
    a_turtle.forward(50)    
   
def draw():   
    
    playground=turtle.Screen() 
    playground.bgcolor("orange")
    a=turtle.Turtle()
    degree=1
   
    while(degree<30):  
    #for degree in range(0,36):
            dia_draw(a)
            a.right(1)    
            degree+=1
    
    a.right(90)
    a.forward(200)        
    
    playground.exitonclick()

draw()