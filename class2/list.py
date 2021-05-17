
# List is a data types which has the capability of adding multiple values

y = [1, 2, 3, 4, 5]

# To add an element to the end of the List use the built in function append
y.append(1)

# Note that you can add more than one element by using the append function you have to
# use the builtin function called extend

y.extend([1, 2, 3, 4])
# print(y)

# sorts the list in ascending order
y.sort()
print(y)

# sorts the list in descending order
descending = y.sort(reverse=True)
print(descending)

# makes a copy of the list
z = y.copy()
print(z)
