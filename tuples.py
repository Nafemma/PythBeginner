#tuples are immutable
#tuples are ordered
#tuples can contain duplicates
#tuples can contain different data types
#tuples are defined using parentheses ()

x = ('a', 'b', 'c', 'd')
y = list(x) #convert tuple to list in order to change value of element
y[1] = "B"
x = tuple(y) #convert list to tuple

print(x)