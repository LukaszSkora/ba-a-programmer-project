def sum_of_digits(n):
    if n < 10:
        return n
    else:
        return n % 10 + sum_of_digits(n // 10)


input = int(input("Enter an integer: "))
sum_of_digits = sum_of_digits(input)
print(f"Sum of digits of {input} is {sum_of_digits}.")
