# creating a set
set1 = {1, 2, 3, 4}
print(type(set1))

list1 = [1, 2, 3, 4, 5]

set1.add(5)
print(set1)

set2 = {5, 6, 7, 8, 9}

set3 = set1.union(set2)
print(set3)


set4 = set1.intersection(set2)
print(set4)


set5 = set1.difference(set2)
print(set5)
