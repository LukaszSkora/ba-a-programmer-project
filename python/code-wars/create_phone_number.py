def create_phone_number(n):
    # your code here
    num = ''
    for i in n:
        num = num + str(i)
    phone_number = '(' + num[:3] + ') ' + num[3:6] + '-' + num[6:]
    return phone_number
