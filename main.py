import turtle

screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Fractal Tree Generator")
screen.tracer(0)

# Add this line — hides the window until we actually draw
screen.setup(width=800, height=800)

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



def get_level():
    # Keep asking until the user enters a valid whole number >= 0
    while True:
        try:
            n = int(input("What level of tree? "))
            if n >= 0:
                return n
            else:
                print("Please enter 0 or greater.")
        except ValueError:
            print("Please enter a whole number.")

def get_length():
    # Keep asking until the user enters a positive number
    while True:
        try:
            length = float(input("Trunk length in pixels (e.g. 100)? "))
            if length > 0:
                return length
            else:
                print("Please enter a number greater than 0.")
        except ValueError:
            print("Please enter a number.")

def get_angle():
    # Keep asking until the user enters a number between 1 and 90
    while True:
        try:
            angle = float(input("Branch angle in degrees (e.g. 30)? "))
            if 1 <= angle <= 90:
                return angle
            else:
                print("Please enter a number between 1 and 90.")
        except ValueError:
            print("Please enter a number.")

def get_scale():
    # Keep asking until the user enters a number between 0 and 1
    while True:
        try:
            scale = float(input("Scale factor (the higher the number the longer the lines)? "))
            if 0 < scale < 1:
                return scale
            else:
                print("Please enter a number between 0 and 1.")
        except ValueError:
            print("Please enter a number.")

# ── Main menu loop ─────────────────────────────────────────────────────────────
def menu():
    print("\n╔══════════════════════════════╗")
    print("║    Fractal Tree Generator    ║")
    print("╚══════════════════════════════╝")

    while True:
        
        print("1. Draw a fractal tree")
        print("2. Quit")

        choice = input("\nEnter your choice (1 or 2): ").strip()

        if choice == "1":
            print("\nEnter tree parameters:")

            # Call each input function to get the parameters
            n      = get_level()
            length = get_length()
            angle  = get_angle()
            scale  = get_scale()

            # Clear the previous tree and draw the new one
            print("\n  Drawing tree...")
            pen.clear()
            pen.penup()
            pen.goto(0, -250)
            pen.setheading(90)
            pen.pendown()

            screen.tracer(0)
            customtree(n, length, angle, scale)
            screen.update()
            print("Done!")

        elif choice == "2":
            print("\nGoodbye!")
            break

        else:
            print("Please enter 1 or 2.")

# ── Run ────────────────────────────────────────────────────────────────────────
menu()
screen.mainloop()