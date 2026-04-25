import turtle

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Fractal Tree")
screen.tracer(0)

pen = turtle.Turtle()
pen.color("green")
pen.speed(0)
pen.hideturtle()

def simpletree(n):
    if n == 0:
        return

    # Save position and heading at base of this branch
    pos = pen.position()
    dir = pen.heading()

    # Draw branch, recurse left, restore, recurse right, restore
    pen.forward(50)
    pen.left(15)
    simpletree(n - 1)

    pen.penup()
    pen.goto(pos)
    pen.setheading(dir)
    pen.pendown()

    pen.forward(50)
    pen.right(15)
    simpletree(n - 1)

    pen.penup()
    pen.goto(pos)
    pen.setheading(dir)
    pen.pendown()

# Position turtle at bottom centre facing up
pen.penup()
pen.goto(0, -250)
pen.setheading(90)
pen.pendown()

simpletree(10)

screen.update()
screen.mainloop()