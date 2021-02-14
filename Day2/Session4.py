# Tuple are immutable
varTuple = (5, 1, 5, 6, 5, 23, 5, 67)
#varTuple[0] = 10
print(varTuple)
varWeek = tuple([i+1 for i in range(52)])
varDay = tuple([i+1 for i in range(7)])

print(varWeek[4])
print(varTuple.count(5))

for day in varDay:
    print(day)