import re

text = 'Its A corona everywhere and offices WFH. Vaccination started now hopefully' \
       'will get some relief soon'
output = re.compile('[a-e]') # case sensitive and all categories []
print(output.findall(text))

text = 'It was valentine day on 14th Feb and it was started in 1980 at 11 AM'
output = re.compile('\d') # Only decimal numbers
print(output.findall(text))

output = re.compile('\d+') # more than 1 decimal numbers
print(output.findall(text))

text = 'Ola cab number DL12H2432 arrived at airport gate1' \
       ' at 11PM. Driver was Mr. Surinder singh dialed 98********'
output = re.compile('\w') # [a-zA-z0-9]
print(output.findall(text))

output = re.compile('\w+') # [a-zA-z0-9]+
print(output.findall(text))

output = re.compile('\W') # Non [a-zA-z0-9]
print(set(output.findall(text)))

output = re.compile('ab*') # '*' replaces the no. of occurrence of a character.
print(output.findall(text))