
filename = 'learning_python.txt'
with open(filename, encoding = 'utf-8') as file_object:
    content = file_object.read()
    content = content.replace('\n', '')
    print(content)
#print(file_object)