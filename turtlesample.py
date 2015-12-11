import turtle
i=0;x=0
turtle.penup()
turtle.lt(90)
turtle.fd(200)
turtle.lt(90)
turtle.fd(40)
turtle.lt(180)
turtle.pendown()
turtle.fd(33)

turtle.lt(270)
turtle.fd(150)

while i != 19:
    turtle.lt(-i)
    turtle.fd(i)
    i+=1
    
turtle.penup()
turtle.fd(150)
turtle.lt(263)
turtle.fd(101)
turtle.lt(268)
turtle.fd(7)
turtle.pendown()


turtle.fd(150)

while x != 11:
    turtle.rt(x+2)
    turtle.fd(x-1)
    x+=1
    
turtle.rt(70)
turtle.fd(43)

turtle.lt(59)
turtle.fd(30)


turtle.exitonclick()


