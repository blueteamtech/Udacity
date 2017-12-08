import turtle

def draw_flower(flower):
    for i in range(1,4):
        flower.forward(100)
        flower.right(120)
windows = turtle.Screen()
windows.bgcolor("white")
daisy = turtle.Turtle()
daisy.shape("turtle")
daisy.color("yellow")
daisy.speed(10)
for i in range(1,61):
    draw_flower(daisy)
    daisy.right(6)
daisy.right(90)
daisy.forward(300)

windows.exitonclick()



draw_flower()
