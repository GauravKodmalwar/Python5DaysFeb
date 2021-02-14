# Functions - Reusable code to reduce the number code
# This will also simplify code, readable
# They are written for specific purpose\functionality
# e.g. +, -, /, %
# Dmart ==>
# main file {
#   scans all the product label ==> database, exceptional handling
#   generates bill ==> database, exceptional handling
#   pay bill, database, exceptional handling
#   receipt., database, exceptional handling
#}
# def function_name(arguments):
#   block of code
#   return output (OPTIONAL)
def my_function(var1, var2='Pythoner'):
    print("{} - {}".format(var1, var2))
my_function(var1='Hi ')
print(my_function(var2='5', var1='d'))

def databaseConnection(databasename, username, password, connectionType='SharePool'):
    connectionString = username + '@' + databasename + ':' + password
    pass
    return connectionString

print(databaseConnection(username='scott', password='Harris', databasename='Oracle'))

# argument matching function ==> Dynamic number of arguments
# *argument_list
def addition(var1, var2, var3 = 'Simple Example', *arguments):
    print(var1, var2, var3)
    print(type(arguments))
    Total = 0
    for number in arguments:
        Total += number
    return Total
print(addition(50, 100, 299, 10, 11, 550))

# Keyword argument matching function - variable number of argument name + value
def subtraction(var1, var2, var3='subtraction', *arguments, **keyArguments):
    print(var1, var2, var3)
    Total = 0
    for key, value in keyArguments.items():
        Total -= keyArguments.get(key)
    print(arguments)
    return addition(*arguments), Total

print(subtraction(5, 50, 'Grand Total', 50, 10, 20, 40, var4=10, var5=20))

print('**************** LAMBDA function *****************')
# Anonymous function
# Which has only 1 statement which will be a return value
# variable name = lambda input: output
annonymousFunction = lambda var1 : var1 + 10
print(annonymousFunction(10))
addition = lambda var1, var2, var3: var1[0] + var2 + var3
print(addition([5],1,3))

print('------------ ACCESS levels ---------------')

def scope():
    global varLang
    print(varLang)
    varLang = ' Day 3'

varLang = 'Java'
scope()
print(varLang)

print('----------------- yield, filter, reducer, mapper ----------------')
def flowcontrolpaused(var1):
    for i in var1:
        yield i**2
        print('sent 1 value')
for output in flowcontrolpaused([10, 20, 30]):
    print(output)

y = flowcontrolpaused([10, 20, 30])
print(next(y))
print(next(y))
print(next(y))

print('--------------------- filter --------------------')
# function name and sequence - collection
# function should always send Boolean output
var1 = [10, 2, 4, 5, 6, 7, 8, 4, 1]
def calEven(var2):
    if var2 % 2 != 0:
        return True
    else:
        False
print(list(filter(calEven, var1)))
print(list(filter(lambda var2: True if var2%2 == 0 else False, var1)))

print('----------------- mapper ----------------------')
# function name and sequence - collection
# output and input size will be same
var1 = [10, 2, 4, 5, 6, 7, 8, 4, 1]

def square(var1):
    return var1**2

print(list(map(square, var1)))