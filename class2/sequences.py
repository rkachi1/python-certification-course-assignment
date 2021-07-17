def findDuplicates():
    initialString = input('Enter a string\n')
    for i in initialString:
        counter = initialString.count(i)
        print(counter,i)


findDuplicates()