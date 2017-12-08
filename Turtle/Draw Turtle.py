import turtle
def draw_shapes():
    window = turtle.Screen()
    window.bgcolor("gray")
  
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.speed(1)
    brad.color("yellow")
    
    square_finish = 4
    square_init = 0

    while (square_init < square_finish):
        brad.forward(100)
        brad.right(90)
        square_init = square_init + 1

    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)
 
draw_shapes()
  
window.exitonclick()
