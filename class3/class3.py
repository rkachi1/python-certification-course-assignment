def add():
    a = input('Enter the first number to add\n')

    b = input('Enter the second number to add\n')

    while(a.isnumeric or b.isnumeric):
        if(a.isalpha or b.isalpha or a.isalnum or b.isalnum):
            print('Please enter a valid input')
            break
        else:
            print(int(a) + int(b))
            break
add()
