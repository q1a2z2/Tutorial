#Tuple:  Tuples are immutable(not changeable)

tuple = (1,'a',True,2,'b',False)

print(tuple)
print(type(tuple))

print(tuple[1:4])

#length
print(len(tuple))

#concatenating

l1 = (1,2,3)
l2 = (3,4,5,5)
print(l1 + l2)

#Repeating tuple element
tuple = ('sparta',300)
print(tuple*3)

# concat and repeat
tuple1 = ('sparta',300)
tuple2 = (1,2,3)
print(tuple1*3 + tuple2)

#find min and max value

tuple3 = (1,2,34,56,67,12)
print(max(tuple3))