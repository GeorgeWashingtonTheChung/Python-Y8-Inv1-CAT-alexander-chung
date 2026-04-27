import turtle
import random
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Fractal Tree Generator")
screen.tracer(0)


screen.setup(width=800, height=800)

pen = turtle.Turtle()
pen.color("green")
pen.speed(0)
pen.hideturtle()

# Task 4
def s_triangle(n):
    # Prints a row of n no. of stars, then calls itself with n-1. Stops when n reaches 0
    if n > 0:
        print("*" * n)
        s_triangle(n - 1)

# Task 5
def triangular(n):
    # Returns the nth triangular number (1+2+...+n)
    # T(n) = n + T(n-1), base case T(0) = 0
    if n <= 0:
        return 0
    return n + triangular(n - 1)

# Task 6
def fibonacci(n):
    # Fibonacci: 1, 1, 2, 3, 5... (each number is the sum of the two before it)
    if n <= 2:
        return 1 # The first two numbers are always 1
    return fibonacci(n - 1) + fibonacci(n - 2)




# Task 7
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



# Task 8
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

# Task 10
def randomfractaltree(n, length, angle, scale):
   
    if n == 0:
        return

    pos = pen.position()
    dir = pen.heading()

    # Pick a random angle: vary by up to +/- 15 degrees from the base angle
    rand_angle = angle + random.uniform(-15, 15)

    # Pick a random scale: vary by up to +/- 0.1 from the base scale
    # clamp it so it stays between 0.1 and 0.99 (avoids broken trees)
    rand_scale = scale + random.uniform(-0.1, 0.1)
    rand_scale = max(0.1, min(0.99, rand_scale))

    # Draw branch and recurse left
    pen.forward(length)
    pen.left(rand_angle)
    randomfractaltree(n - 1, length * rand_scale, angle, scale)

    # Restore and recurse right
    pen.penup()
    pen.goto(pos)
    pen.setheading(dir)
    pen.pendown()

    pen.forward(length)
    pen.right(rand_angle)
    randomfractaltree(n - 1, length * rand_scale, angle, scale)

    # Restore for caller
    pen.penup()
    pen.goto(pos)
    pen.setheading(dir)
    pen.pendown()
# Task 11
def realistictree(n, length, angle, scale, max_n):

    # New thingies
    #  1. Branch thickness means trunk is thick, tips are thin
    #  2. Branch colour: brown at the bottom, green near the tips
    #  3. Leaf dots: small green circles drawn at the tip branches (n==0)

   
    

    # draw a leaf dot instead of just returning 
    if n == 0:
        pen.penup()
        pen.color("#228B22")        # forest green for leaves(Used hexadecimal converter)
        pen.begin_fill()
        pen.circle(4)               # small filled circle
        pen.end_fill()
        pen.pendown()
        return

    # Save position and heading
    pos = pen.position()
    dir = pen.heading()

    # Branch thickness
    pen.pensize(max(1, n))

    # Branch colour
    depth_ratio = n / max_n
    if depth_ratio > 0.5:
        # Lower half of tree: brown trunk colour
        pen.color("#8B4513")        # saddle brown(Hexadecimal converter)
    elif depth_ratio > 0.25:
        # Middle: transition to dark green
        pen.color("#556B2F")        # dark olive green(Hexadecimal converter)
    else:
        # Near tips: bright green
        pen.color("#228B22")        # forest green(Hexadecimal converter)

    # All below is same as Task 10
    rand_angle = angle + random.uniform(-15, 15)
    rand_scale = max(0.1, min(0.99, scale + random.uniform(-0.1, 0.1)))

    # Draw branch and recurse left
    pen.pendown()
    pen.forward(length)
    pen.left(rand_angle)
    realistictree(n - 1, length * rand_scale, angle, scale, max_n)

    # Restore and recurse right
    pen.penup()
    pen.goto(pos)
    pen.setheading(dir)
    pen.pendown()

    pen.forward(length)
    pen.right(rand_angle)
    realistictree(n - 1, length * rand_scale, angle, scale, max_n)

    # Restore for caller
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
            angle = float(input("Angle between branches in degrees (e.g. 30)? "))
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
def reset_turtle():
    pen.clear()
    pen.penup()
    pen.goto(0, -250)
    pen.setheading(90)
    pen.pendown()

# Main Menu(Task 9)
def menu():
    print("\n╔----------------------------------╗")
    print("|    Fractal Tree Generator        |")
    print("╚----------------------------------╝")

    while True:
        print("\n--- Main Menu ---")
        print("1. Draw a regular fractal tree")
        print("2. Draw a random fractal tree")
        print("3. Draw a realistic fractal tree")
        print("4. Quit")

        choice = input("\nEnter your choice (1-4): ").strip()


        if choice == "1":
            print("\nEnter tree parameters:")
            n      = get_level()
            length = get_length()
            angle  = get_angle()
            scale  = get_scale()

            print("\n  Drawing tree...")
            reset_turtle()
            customtree(n, length, angle, scale)
            screen.update()
            print("  Done!")

        elif choice == "2":
            print("\nEnter tree parameters:")
            n      = get_level()
            length = get_length()
            angle  = get_angle()
            scale  = get_scale()

            print("\n  Drawing random tree...")
            reset_turtle()
            randomfractaltree(n, length, angle, scale)
            screen.update()
            print("  Done! Run again to get a different tree.")

        elif choice == "3":
            print("\nEnter tree parameters:")
            n      = get_level()
            length = get_length()
            angle  = get_angle()
            scale  = get_scale()
            print("\n  Drawing realistic tree...")
            reset_turtle()
            # pass n as max_n so the function knows the full depth
            realistictree(n, length, angle, scale, max_n=n)
            screen.update()
            print("  Done! Run again for a different tree.")

        elif choice == "4":
            print("\nGoodbye!")
            break

        else:
            print("  Please enter 1, 2, 3 or 4.")
# Run 
menu()
screen.mainloop()