varSalary = 400
varAge = 34
# if elif else
print('---------------- Conditional comparison ---------------')
if varSalary > 5000: # if condition:
    print('Salary is greater than 5k')
    varSalary *= varAge
    print('Revised salary is {}'.format(varSalary))
elif varAge < 28:
    print('Age is lower than 28 and salary is {}'.format(varSalary))
elif varAge > 30:
    if varSalary > 300:
        print('Salary is greater than daily wages')
    print('Age is higher than 30')
else:
    print('Salary is too low to provide Credit Card')
    varSalary += 1000
print('End of code execution, salary is {}'.format(varSalary))

condition = 1000 if varSalary > 5000 else 200
# varName = Value if CONDITION else Value
print(condition)