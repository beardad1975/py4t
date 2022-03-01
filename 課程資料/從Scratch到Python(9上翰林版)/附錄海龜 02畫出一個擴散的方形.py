import turtle

window = turtle.Screen()
john = turtle.Turtle()

for i in range(1, 21) :
    john.forward(i * 10)
    john.right(90)
    
window.exitonclick()

