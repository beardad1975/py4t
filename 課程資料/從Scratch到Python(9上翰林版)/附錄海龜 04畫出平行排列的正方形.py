import turtle

window = turtle.Screen()
window.setup(480, 360)

john = turtle.Turtle()
john.penup()
john.goto(-140, -20)

for i in range(6) :
    john.pendown()
    for j in range(4) :
        john.forward(30)
        john.right(90)
    john.penup()
    john.forward(60)

window.exitonclick()

        
