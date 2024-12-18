"""
# This is the first exegesis
# This is the second exegesis
# 

"""
#这是一个多行exegiesis
#可以随意编写
"""

'nininin'
'python'
'I want to learn python in 30 days'
"""
a = '''
This is a multi-line string
'''
print(a)

first_dict_system = {
    'name': 'John',
    'age':24,
    'job':'程序员'
    }
del first_dict_system['age']
print(first_dict_system)

print(1+2)
print(1-2)
print(1*2) #乘法
print(1/2) #除法
print(1//2) #取整除
print(1%2) #取余\取模
print(2**3) #乘方
print(10**2) #幂运算

print(type(10)) #打印数据类型整数
print(type(10.5)) #打印数据类型浮点数
print(type('hello')) #打印数据类型字符串
print(type(True)) #打印数据类型布尔值
print(type(None)) #打印数据类型空值
print(type(first_dict_system)) #打印数据类型字典
print(type(a)) #打印数据类型字符串
print(10>5) #大于
print(10<5) #小于
print(type([1,2,3]))#打印数据类型列表
print(type((1,2,3)))#打印数据类型元组
print(type({'name':'John','age':24,'job':'程序员'}))#打印数据类型字典
print(type(4-4j))#打印数据类型函数

point1=(2,3)
point2=(10,8)
Two_points_distance=((point1[0]-point2[0])**2+(point1[1]-point2[1])**2)**0.5
print(Two_points_distance)#打印两个点的坐标