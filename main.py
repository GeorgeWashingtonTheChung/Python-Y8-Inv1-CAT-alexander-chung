def s_triangle(s):
    # Prints a row of s no. of stars, then calls itself with s-1. Stops when s reaches 0
    if s > 0:
        print("*" * s)
        s_triangle(s - 1)


n = int(input("How many layers? "))
s_triangle(n)