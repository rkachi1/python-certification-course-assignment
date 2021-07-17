number = int(input('Enter the given number\n'))
factorCount = 1 
while(factorCount <= number):
    if(number%factorCount == 0 and factorCount != 1):
        print('Factor is even',factorCount)
    else:
        print('Factor is odd',factorCount)
    factorCount+=1