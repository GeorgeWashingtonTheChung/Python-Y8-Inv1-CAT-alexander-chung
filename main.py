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



def customtree(n, length, angle, scale):
    
    # Draw a Level-n fractal tree with user-defined properties.



    # n      - level of the tree (0 = nothing)
    # length - length in pixels of the first/trunk branch
    # angle  - angle in degrees between branches
    # scale  - factor by which each branch shrinks per level
                     # e.g. scale=0.75 means each child branch is 75% of its parent
    

    if n == 0:
        return  # Base case: nothing to draw

    # Save position and heading so we can return here after each subtree
    pos = pen.position()
    dir = pen.heading()
    # Left branches
    pen.forward(length)          # Draw branch (length can be changed)
    pen.left(angle)              # Turn by defined angle (was fixed 15)
    customtree(n - 1, length * scale, angle, scale)  # scale shrinks next level
    # Restore to base of this branch
    pen.penup()
    pen.goto(pos)
    pen.setheading(dir)
    pen.pendown()
    # Right branches
    pen.forward(length)          # Redraw branch to get to tip
    pen.right(angle)             # Turn opposite direction
    customtree(n - 1, length * scale, angle, scale)

    pen.penup()
    pen.goto(pos)
    pen.setheading(dir)
    pen.pendown()
# Make sure its not upside down
pen.penup()
pen.goto(0, -250)   # start at bottom
pen.setheading(90)  # face upward
pen.pendown()
# Can use this to set within the code
customtree(8, 100, 20, 0.85)

screen.update()
screen.mainloop()