def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def suffix(n):
    if input % 100 == 11 or input % 100 == 12 or input % 100 == 13:
        suffix = "th"
    elif input % 10 == 1:
        suffix = "st"
    elif input % 10 == 2:
        suffix = "nd"
    elif input % 10 == 3:
        suffix = "rd"
    else:
        suffix = "th"
    return suffix

input = int(input("Enter an integer: "))
fib = fib(input)
print(f"{input}{suffix(input)} number in Fibonacci sequence is {fib}.")
