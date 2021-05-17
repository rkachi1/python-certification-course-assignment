# Tuples are same as list just that only the difference once a tuple is declared
# using a bracket and it is readonly meaning you can't update any existing values
# accessing values is faster since memory allocation is done only for fixed segments where as list
# does memory allocation for variable segment and fixed segments since list can be modifed and added,
# append etc

x = (1, 3, 4, 5)


# an example of this is provided below
x[0] = 'apple'
print(x)
