# File handling - Input Output
import time
var1 = 10
file = open('./Data/newsData', 'r')
#with open('./Data/newsData') as file:
reader = file.read()
file.seek(4)
#print(file.readline()) # '\n'
#file2 = open('./Data/FileOutput_' + '.txt', 'w')
file2 = open('./Data/FileOutput_' + '.txt', 'w')
file2.write(file.readline())
file2.seek(0)
print(file2.read())
#print(reader)
file.close()
file2.close()