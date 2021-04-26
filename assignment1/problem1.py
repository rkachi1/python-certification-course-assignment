def factorsEvenOrOdd():
    givenNum = int(input('Enter a given number'))
    i = 1
    while(i <= givenNum):
        if(givenNum % i == 0):
            if(i % 2 == 0):
                print('Factor is even', i)
            else:
                print('factor is odd', i)
        i = i + 1


factorsEvenOrOdd()
