import turtle #imports turtle module that draws graphics

def draw_square(some_turtle):       #defines function draw_square
    for i in range(1,5):            #creates 4 iteration loop
        some_turtle.forward(100)    #.forward is called from the turtle class that tells variable some_turtle to move forward 100 units
        some_turtle.right(90)       #.right is called from the turtle class that tells variable some_turtle to move 90 degrees to the right

def draw_art():                     #defines function draw_art
    windows = turtle.Screen()       #defines variable windows with turtle.Screen() <-- which pulls up a window
    windows.bgcolor("gray")         #this is an example of using class a blue print. assigns screen call with gray screen.
    #Create turtle Brad - Draws a square
    brad = turtle.Turtle()          #defines variable brad with turtle class
    brad.shape("turtle")            #.shape allows bob to call turtle as the lead for outlining the draw
    brad.color("yellow")            #.color defines color
    brad.speed(2)                   #sets speed
    for i in range(1,37):           #defines loop of 36 iterations
        draw_square(brad)           #brad has been defined by shape, color and speed via turtle class. this draw will feature that as variable to above fucntion draw_square
        brad.right(10)              #this will move the starting point of brad the turtle 10 degrees right before the iterations starts again

    windows.exitonclick()

draw_art()                          #executes draw_art with defined features within.
