var1 = 10
var2 = 3
print('Arithmatic Operator')
print(var1 + var2)
print(var1 - var2)
print(var1 * var2)
print(var1 / var2)
print(var1 % var2)
print(var1 // var2)
print(var1 ** var2)
print(pow(var1, var2))
var1 -= 2  # var1 = var1 - 2
var2 *= 3  # var2 = var2 * 3
var1 /= 2  # var1 = var1 / 2
var2 %= 2  # var2 = var2 % 2
var1 //= 3 # var1 = var1 // 3
print(var1, var2)

print('--------------- Comparison Operator -----------------')
print(var1 > var2)
print(4 < var2)
print(var1 >= var2)
print(var1 <= 2)
print(var1 != var2)
var3 = True
print(type(var3))

print('------------------- Bitwise Operator -------------------')
var1 = 100
var2 = 478
print(bin(var1), bin(var2))
print('AND', bin(var1&var2))
print('OR', bin(var1|var2))
print('XOR', bin(var1^var2))
print('NOT', bin(~var2))
print('Left shift', bin(var1 << 2))
print('Right shift', bin(var1 >> 3))

print('------------ Logical Operator --------------')
varSalary = 6400
varAge = 40
print(varSalary > 5000 and varAge < 30)
print(varSalary > 5000 or varAge < 30)
print(not(varSalary > 5000 and varAge < 30))