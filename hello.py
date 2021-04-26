age = input('Enter a number\n')

while(1):
    if(age.isalpha or age.isalnum):
        print('Please enter a valid input')
    else:
        print(age * 5)
