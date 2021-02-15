import re
text = """
Ashutosh is of 50 years and Vinita is of 18 years
Raghu is of 19 years and Laxmi is of 30 years"""

ages = re.findall('\d{1,3}', text)
names = re.findall('[A-Z][a-z]*', text)
print(ages)
print(names)

print(re.findall('^Ashutosh', text))
print(re.findall('years$', text))

# Quantifiers
print(re.search('foo-*bar', 'foobar'))
print(re.search('foo-*bar', 'foo-bar'))
print(re.search('foo-*bar', 'foo---bar'))
