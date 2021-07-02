
def countdigitsAndLetters(str):   
    letterCount = 0
    digitCount = 0
    for i in str:
        if(i.isalpha()) == True:
            letterCount+=1
        elif(i.isnumeric()) == True:
            digitCount+=1
    print('Letters are', letterCount)
    print('Number of digits are', digitCount)

countdigitsAndLetters('Edureka1234')