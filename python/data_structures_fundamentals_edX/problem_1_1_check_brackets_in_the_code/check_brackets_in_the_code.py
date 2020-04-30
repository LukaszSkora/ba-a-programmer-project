code_to_check = "a)"


def main():
    print(check_brackets(code_to_check))


def check_brackets(string_of_code):
    stack = []
    for char in code_to_check:
        if char in '([{':
            stack.append(char)
        else:
            if char not in ')]}':
                continue
            if len(stack) == 0:
                return string_of_code.index(char)+1
            top = stack.pop()
            if (top == '[' and char != ']') or (top == '(' and char != ')') or (top == '{' and char != '}'):
                return one_based_index(string_of_code, char)
    return "Success"


def one_based_index(string, char):
    return string.index(char) + 1


if __name__ == '__main__': main()
