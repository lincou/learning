import os
print(os.getcwd())  # 打印当前工作目录



#第一次打印时读取整个文件；第二次打印时遍历文件对象；第三次打印时
#将各行存储在一个列表中，再在with 代码块外打印它们。
filename = '30DaysOfPython\learning_python.txt'
with open(filename) as f:
    content = f.readline()
    print(content)

with open(filename) as f:
    for line in f:
        print(line.strip())