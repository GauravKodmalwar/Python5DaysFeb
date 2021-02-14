# Sequencing example - String, List, Tuple...
var1 = 'This is Session2 of Python.'
print(var1 + ' Session1 completed')
print(3 * var1)
print(len(var1))
print(var1[0])
print(var1[-27])
print(var1[0:4]) # Slice string - [start:end:step (optional)]
print(var1[0:10:2])
print(var1[::-1])
print(var1[5::5])
print('=================')
print(var1[-1:-5:-1])

print('{} a text of length {}'.format(var1, len(var1)))
print('{1} a text of length {0}'.format(var1, len(var1)))

print("------------------------------")
#var1 = '5.5'
print(var1.replace('Python', 'Java'))
print(var1.find('is'))

'Take User input'
'Print number of characters after and before the digit'
'This is Python session 2 and practising with string'

print('----------------convert variable ------------------------')
var1 = '53'
print(type(var1))
print(int(var1)*5, var1*3)
number1 = 5
print(str(number1)*6)
print(float(var1))