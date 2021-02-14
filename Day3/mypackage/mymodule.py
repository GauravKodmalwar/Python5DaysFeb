def my_function(var1, var2='Pythoner'):
    print("{} - {}".format(var1, var2))

def addition(*arguments):
    Total = 0
    for number in arguments:
        Total += number
    return Total