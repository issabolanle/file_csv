import os
import sys
# open the file
# myfiles = open('phone_list.txt', 'r')
myfiles = open(os.path.join(sys.path[0],'phone_name.csv'),'r')

# read the file using the read function
read_file = myfiles.read()

print(read_file)
myfiles.close()
