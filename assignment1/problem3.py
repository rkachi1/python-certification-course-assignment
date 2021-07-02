OddNumberCount = []
intialCount = 0
for i in range(1000,3000):
    if(i%2 != 0):
        OddNumberCount.append(i)
        intialCount+=OddNumberCount.count(i) 
print(intialCount)