# 1. Take input in run time
# 2. Validate wether its a number or not
# 3. Print either odd, even, prime

# 1. Check if any word in a sentence a Palindrome e.g. 'Mom' == 'Mom'
# 2. Take sentence as a input. e.g. This is mars mission.
# 3. Check if its a Palindrome or not

# 1. Take a input for a numbers.
# 2. Print factors e.g. 1, 3, 5, 15 factors of 15
# 3. Print LCM Least common multiple e.g. 60 is LCM of 5, 12.
var1, var2 = 5, 12
m = var1 if var1 > var2 else var2
while(True):
    if m % var1 == 0 and m % var2 == 0:
        print(m)
        break
    m += 1
print('Outside of while loop')

var3 = 'This is not a Palindrom sentence mom, Bob  its a simple code'
var4 = 0
for word in var3.split(' '):
  word = word.replace(',','').upper()
  if len(word) < 2:
      continue
  if word == word[::-1]:
      var4+=1
  elif True:
      pass
  else:
      print()
print(var4)
