import turtle

def draw_square():
    
    window=turtle.Screen()
    window.bgcolor("gray")

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.speed(3)
    brad.color("yellow")

    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)

    window.exitonclick()
    
draw_square()
