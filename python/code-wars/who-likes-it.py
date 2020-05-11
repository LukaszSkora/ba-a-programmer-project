def main():
    names = ['Peter', 'Paul', 'Mary', 'Pepper']
    print(likes(names))


def likes(names):
    if len(names) < 1:
        return 'no one likes this'
    if len(names) == 1:
        return str(names[0]) + ' likes this'
    if len(names) == 2:
        return str(names[0]) + ' and ' + str(names[1]) + ' like this'
    if len(names) == 3:
        return str(names[0]) + ', ' + str(names[1]) + ' and ' + str(names[2]) + ' like this'
    if len(names) > 3:
        return str(names[0]) + ', ' + str(names[1]) + ' and ' + str(len(names) - 2) + ' others like this'


if __name__ == '__main__':
    main()
