import os
if os.path.exists('newfile.txt'):
    os.remove('newfile.txt')
    print("File deleted")

else:
    print("the file doesnt exists")