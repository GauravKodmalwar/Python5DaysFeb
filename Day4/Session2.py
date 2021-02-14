import os, time, datetime

for _, directories, files in os.walk('./Data'):
    for file in files:
        print(file, directories)

# Create directories ('Monday', 'Tuesday',....)
# Create files
# Read write some garbage data for i in 'ABCD'
# If directory already exists, move all files from that directory to tmp
# read content of a file, write into another file by keeping same filename
# os.remove
# Create new files inside the same directory