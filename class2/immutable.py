# immutable and mutable data types
# immutable cannot be changed and mutable can be changed

# an example is below

# mutable means change of value and memory reference remains unchanged

# immutable means change of value and memory reference changes


# example of immutable data types:

x = 10
print(id(x))

x = 5
print(id(x))


y = 12.3
print(id(y))


y = 2.3
print(id(y))


list1 = [12, 3, 4, 5]

print(id(list1))

list1[2] = 2

print(id(list1))

# this concludes that list is an mutable data type


# mutable data types are list,set and dictionary


# immutable data types are integer, float, boolean , complex, string, tuple


dict1 = {'name': 'madhan'}
print(id(dict1))

dict1.update({'text': 'appending to dictionary'})

print(id(dict1))


set1 = {1, 2, 3, 4}
print(id(set1))

set1.add(5)

print(id(set1))


x = True
print(id(x))


x = False
print(id(x))
