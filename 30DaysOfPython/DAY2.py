#python 中的变量
#变量是存储数据的地方，在程序运行时，变量可以用来存储数据，并在程序的不同部分使用。
#变量的命名规则：
#1. 变量名只能包含字母、数字和下划线。
#2. 变量名不能以数字开头。
#3. 变量名的长度没有限制。
#4. 变量名区分大小写。
#5. 变量名应简短，但意义明确。
#6. 变量名应避免与关键字冲突。
#7. 变量名应简明扼要，避免使用无意义的变量名。
#8. 变量名应与实际意义相符。
#9. 变量名应避免使用缩写。
#10. 变量名应避免使用拼音。
FirstName = "John"
LastName = "Doe"
Age = 30
isMarried = True
First_Name = "Jane" # 变量名包含下划线，但不推荐

#print()和len()函数
#print()函数用于输出变量的值。
print(FirstName)
print(LastName)
print('Hello,world!')
print('Hello,world',',','!')
print(len('Hello,world')) # 输出字符串的长度

#len()函数用于获取变量的长度。

#在一行中声明多个变量
First_Name, Last_Name, Age, isMarried = "Tim", "Dee", 25, True
print(First_Name)
print(Last_Name)
print(Age)
print(isMarried)
print('first_name:', First_Name)
print('last_name:', Last_Name)
print('age:', Age)

#input()函数
#input()函数用于获取用户输入的数据。
#first_name = input('What is your name: ')
#age = input('How old are you? ')

#print(first_name)
#print(age)

#数据类型的转换 
#int()函数用于将字符串转换为整数。
#float()函数用于将字符串转换为浮点数。
#str()函数用于将整数或浮点数转换为字符串。
#list()函数用于将元组或字符串转换为列表。
#tuple()函数用于将列表或字符串转换为元组。
#set()函数用于将列表或字符串转换为集合。
#dict()函数用于将列表或字符串转换为字典。

#practice
firstName,lastName,fullName,country,city,age,year,isMarried,isTrue,isLightOn='nnn','xxx','xxx-yyy','CN','BeiJing','25','2024',True,False,True
print(isLightOn)
print(type(firstName))
print(len(firstName))

numOne=5
numTwo=4
total=numOne+numTwo
diff=numOne-numTwo
product=numOne*numTwo
division=numOne*numTwo
remainder=numOne%numTwo
exp=numOne**numTwo
floorDivision=numOne//numTwo
