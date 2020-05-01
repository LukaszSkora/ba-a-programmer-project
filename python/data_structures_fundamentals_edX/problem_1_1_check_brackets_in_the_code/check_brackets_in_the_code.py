code_to_check = "foo()[](bar[i);"


def main():
    print(check_brackets(code_to_check))


def check_brackets(string_of_code):
    stack = []
    count = 0
    for char in code_to_check:
        count += 1
        if char in '([{':
            stack.append(char)
        else:
            if char not in ')]}':
                continue
            if len(stack) == 0:
                return count
            top = stack.pop()
            if (top == '[' and char != ']') or (top == '(' and char != ')') or (top == '{' and char != '}'):
                return count
    return "Success"


if __name__ == '__main__': main()
