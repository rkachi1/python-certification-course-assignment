# dictionary is a data type which stores the values in the form of key value pairs
# Every element in dictionary is a key value pair
# you can access only by key in dictionary

d = {'name': 'madhan', 'initial': 'sdasdsads'}

print(type(d))

print(d)


print(d['name'])


# can we actually introduce duplicate keys
# keys must be unique but if you introduce the same key again the value would be overwritten
# over the existing one
# dictonary makes the search very fast


# print(dir(dict))


# makes a copy of the dictionary
z = d.copy()
print(z)

# get method gets the value of the key
value = d.get('initial')
print(value)

# Insert an item into the dictionary
inserting = d.update({'color': 'white'})
print(d)


# clears the dictionary
y = d.clear()
print(y)
