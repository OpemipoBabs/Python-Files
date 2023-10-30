# Tuples

myTuple = tuple(("Dave", 42, True))

anotherTuple = (1, 4, 2, 8, 2, 2)

print(myTuple)
print(type(myTuple))
print(type(anotherTuple))

newList = list(myTuple)
newList.append("Neil")
newTuple = tuple(newList)
print(newTuple)

(one, *two, hey) = anotherTuple
print(one)
print(two)
print(hey)

print(anotherTuple.count(2))