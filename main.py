import turtle

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Fractal Tree")
screen.tracer(0)

pen = turtle.Turtle()
pen.color("green")
pen.speed(0)
pen.hideturtle()


def s_triangle(n):
    # Prints a row of n no. of stars, then calls itself with n-1. Stops when n reaches 0
    if n > 0:
        print("*" * n)
        s_triangle(n - 1)


def triangular(n):
    # Returns the nth triangular number (1+2+...+n)
    # T(n) = n + T(n-1), base case T(0) = 0
    if n <= 0:
        return 0
    return n + triangular(n - 1)


def fibonacci(n):
    # Fibonacci: 1, 1, 2, 3, 5... (each number is the sum of the two before it)
    if n <= 2:
        return 1 # The first two numbers are always 1
    return fibonacci(n - 1) + fibonacci(n - 2)



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