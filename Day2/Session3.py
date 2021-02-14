# Set is a collection of values which are Unique
# Unordered collection
# Mutable data structure or collection
setVar1 = {5, 1, 2, 5, 6, 3, 1, 5}
setVar2 = set([50, 10, 20, 20, 20, 49, 30])
setVar2.add(50)
setVar1.add(10)
print(setVar1)
print(setVar2)
print(setVar1.difference(setVar2))
print(setVar1.union(setVar2))
#print(setVar1.difference_update(setVar2))
print(setVar1.intersection(setVar2))
print([number ** 2 for number in setVar1.difference(setVar2)])