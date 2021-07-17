def sortingAlphabetically(inputStr):
    splittedString = inputStr.split(',')
    splittedString.sort()
    
    for word in splittedString:
        print(word)
        
sortingAlphabetically('Hello')