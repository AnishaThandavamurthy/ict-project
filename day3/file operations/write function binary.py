with open('newfile.txt','wb+') as file:
    file.write(b'writing binary content\n')
    file.seek(0)
    content=file.read()
    print(content)