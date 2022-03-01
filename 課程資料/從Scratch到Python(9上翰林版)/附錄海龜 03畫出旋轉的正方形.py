import turtle

window = turtle.Screen()
john = turtle.Turtle()

for i in range(12) :
    for i in range(4) :
        john.forward(100)
        john.right(90)
    john.right(30)
    
window.exitonclick()

    