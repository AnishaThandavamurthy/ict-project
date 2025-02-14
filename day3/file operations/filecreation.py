#code to create a file
try:
    file=open('TEXTFILE.txt','x')
except FileExistsError:
    print("file already exists")



