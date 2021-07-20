str = input('Enter the string\n')
print('alphabetical characters are')
for i in str:
    if(i.isalpha() == True and (str.index(i) % 2 ==0)):
        print(i, end='')
    