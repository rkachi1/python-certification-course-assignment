inputStr = input('Enter a string to count the characters\n')

for i in inputStr:
    charCount = inputStr.count(i)
    print(i,charCount)