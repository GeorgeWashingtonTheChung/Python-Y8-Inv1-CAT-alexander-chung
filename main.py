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

print(fibonacci(20))

