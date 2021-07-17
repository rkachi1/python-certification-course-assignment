def sum():
    num = str(input('Enter the number you want find sum for\n'))
    sum = 0
    for i in range(0, len(num)):
        rem = int(num) % 10
        sum = sum + rem
        num = int(num)/10
    print('Sum of numbers is', sum)
sum()