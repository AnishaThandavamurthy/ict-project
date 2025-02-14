file=open('TEXTFILE.txt','r')
#read first line
line=file.readline()
#read other lines in while loop
while line:
    print(line)
    line=file.readline()
file.close()