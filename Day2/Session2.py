paragraph = """This is not a Palindrom sentence mom, Bob  its a simple code
but this new line will not have any palindrome
how can mom"""
print(id(paragraph))
paragraph += '\n Additional sentence'
print(id(paragraph))
temp = paragraph.split('\n')
# List is a collection of different data values or list
#print(type(temp[0]))
# Declaration using [ ] or list()
# Mutable object
# Indexing to access individual values
# Slicing [start:end:stepcount]
# List comprehention
varList1 = [5, 10, '23', 50.8]
varList2 = list([10,20,405,60])
print(type(varList1))
print(len(varList1))
print(type(varList1[2]))
print(varList2[2])
print(id(varList1))
varList1.append(50)
varList1[0] = 'New Value'
print(id(varList1))
print(varList1.index(50))
print(varList1[4])
print(varList1)
print('---------------------------------------------------')
print(varList1.remove(10))
print(varList1)
print(varList1.pop(2))
print('---------------------------------------------------')
print(varList1)
varList3 = [15,62,29,66,20,48,'New', 'Python']
varList1.extend(varList3)
print([6, 10, 6, 10] + [5])
print(varList1)
print(varList1[2:4:1])

temp = list()
for i in range(10): # range has default values like in slicing range(start:end:stepSize)
    temp.append(i)
print(temp)

print('---------------- List Comprehension ----------------')
varList4 = [5, 1, 16, 26, 29]
even = [i for i in varList4 if i % 2 == 0]
odd = [i+1 for i in varList4 if i % 2 != 0]
# variable = [expression for statement condition]
print(even, odd)

print('------------- Multi dimensional list ----------------')
varList5 = [[6, 10, 29, 59], [29, 49, 53, 13, 59]]

for i in varList5:
    for j in i:
        print(j)

import time

start = time.time()
temp = [i**3 for i in range(500000)]
end = time.time()
print(end-start)

temp = list()
start = time.time()
for i in range(500000):
    temp.append(i**3)
end = time.time()
print(end-start)