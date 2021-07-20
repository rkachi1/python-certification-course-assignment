emptylist = []

count = 0

while(count < 3):
    element = input('Enter elements to be added into the list\n')
    count+=1
    emptylist.append(element) 

for i in emptylist:            
    print('list is ' ,emptylist)
    print('indexes are' , i )