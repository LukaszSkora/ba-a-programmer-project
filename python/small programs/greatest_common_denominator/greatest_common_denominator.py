def gcd(a, b):
    while b != 0:
        temp = a
        a = b
        b = temp % b

    return a


num_a = int(input('Enter first number (int): '))
num_b = int(input('Enter second number (int): '))

gcd = gcd(num_a, num_b)

print(f'The greatest common denominator of {num_a} and {num_b} is {gcd}.')
