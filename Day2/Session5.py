# Dictionary - key: value pair
# Unordered data collection
# Mutable
# Keys are Unique
varDict1 = dict()
varDict2 = {'Day 1': 'Python Basics', 'Day 2': 'Data structure'}
print(varDict2)
print(varDict2.get('Day 1'))
varDict2['Day 1'] = 'Introduction'
varDict2[3] = 'Functions'
print(varDict2.get('3'))
print(varDict2.keys())
for key in varDict2.keys():
    print('{} - {}'.format(key, varDict2.get(key)))
for key, value in varDict2.items():
    print('{} - {}'.format(key, value))