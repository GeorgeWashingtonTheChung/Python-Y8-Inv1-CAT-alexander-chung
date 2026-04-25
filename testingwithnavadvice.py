import turtle

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Fractal Tree")
screen.tracer(0)

pen = turtle.Turtle()
pen.color("green")
pen.speed(0)
pen.hideturtle()



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