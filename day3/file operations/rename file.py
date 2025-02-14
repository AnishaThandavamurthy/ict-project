import os
if os.path.exists("TEXTFILE2.txt"):
    os.rename('TEXTFILE2.txt','newfile.txt')
    print("File renamed..!!!")

else:
    print("The file doesnt exists !!!!")