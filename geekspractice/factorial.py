def fact(num):
    i = 1
    fact = 1
    while(i <= num):
        fact = fact * i
        i+=1
    print('Factorial of the number is', fact)


fact(5)