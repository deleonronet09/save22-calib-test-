import turtle

t = turtle

def A():
    t.reset()
    t.rt(90)
    t.penup()
    t.fd(150)
    t.rt(90)
    t.fd(200)
    t.pendown()
    t.rt(120)
    t.fd(400)
    t.rt(120)
    t.fd(400)
    t.penup()
    t.lt(180)
    t.fd(200)
    t.lt(60)
    t.pendown()
    t.fd(200)

def E():
    t.reset()
    t.penup()
    t.fd(100)
    t.lt(90)
    t.fd(200)
    t.lt(90)
    t.pendown()
    t.fd(250)
    t.lt(90)
    t.fd(400)
    t.lt(90)
    t.fd(250)
    t.penup()
    t.lt(180)
    t.fd(250)
    t.rt(90)
    t.fd(200)
    t.rt(90)
    t.pendown()
    t.fd(125)

def I():
    t.reset()
    t.penup()
    t.lt(90)
    t.fd(200)
    t.pendown()
    t.lt(180)
    t.fd(400)
    t.penup()
    t.rt(90)
    t.fd(120)
    t.lt(180)
    t.pendown()
    t.fd(240)
    t.lt(90)
    t.penup()
    t.fd(400)
    t.lt(90)
    t.pendown()
    t.fd(240)

def O():
    t.reset()
    t.penup()
    t.rt(90)
    t.fd(20)
    t.rt(90)
    t.fd(200)
    t.lt(90)
    t.pendown()
    t.circle(200)

def U():
    t.reset()
    i=1
    t.penup()
    t.lt(90)
    t.fd(100)
    t.lt(90)
    t.fd(150)
    t.lt(90)
    t.pendown()
    t.fd(300)
    while i != 18:
        t.lt(i)
        t.fd(i)
        i+=1
    t.lt(27)
    t.fd(320)

def J():
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
    
def main():
    choice = raw_input("Enter J for J or V for Vowels: ")
    if choice =='J':
        J()
    elif choice == 'V':
        while 1:
            vowel=raw_input("Enter a vowel: ")
            if(vowel=='a'):
                A()
            elif(vowel=='e'):
                E()
            elif(vowel=='i'):
                I()
            elif(vowel=='o'):
                O()
            elif(vowel=='u'):
                U()
            else:
                print 'Vowels only'
    else:
        print 'Choose only from J or V'


main()
