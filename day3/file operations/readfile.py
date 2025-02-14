#read a file 
#Example1

file=open("TEXTFILE.txt","r")

#read the data
content=file.read()

#print the content
print(content)

#close the file
file.close()