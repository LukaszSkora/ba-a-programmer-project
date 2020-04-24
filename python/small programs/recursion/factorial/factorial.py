def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

input = int(input("Enter an integer: "))
factorial = factorial(input)
print(f"Factorial of {input} is {factorial}.")
