# #DAY3

# print(True)
# print(False)
# print(type(True))
# x = 16
# x//=3  #整除
# print(x)

# #除了上述比较运算符之外，Python 还使用：

# #is: 如果变量相等，返回 True(x is y)
# #is not: 如果变量不相等，返回 True(x is not y)
# #in: 如果列表包含某变量，返回 True(x in y)
# #not in: 如果列表不包含某变量(x in y)

# print('A in Asabeneh', 'A' in 'Asabeneh') # True - 字符串中含有元素 A
# print('B in Asabeneh', 'B' in 'Asabeneh') # False - 没有大写字母 B
# print('coding' in 'coding for all') # True - 因为 coding 都在 'coding for all' 中
# print('a in an:', 'a' in 'an')      # True
# print('4 is 2 ** 2:', 4 is 2 ** 2)   # True

# print(3 > 2 and 4 > 3)


# #计算三角形面积
# base= float(input('Enter the base of the triangle: '))
# height =float(input('Enter the height of the triangle: '))
# print("The area of the triangle is:", 0.5*base*height)

# #计算三角形的周长，注意提示用户
# theFirstside=int(input('PLease input the trangle the first side length:'))
# theSecondside=int(input('Please input the trangle the second side length:'))
# theThirdside=int(input('Please input the trangle the third side length:'))
# if theFirstside+theSecondside>theThirdside and theFirstside+theThirdside>theSecondside and theSecondside+theThirdside>theFirstside:
#     print('The perimeter of the triangle is:', theFirstside+theSecondside+theThirdside)
# else:
#     print('The triangle is not valid')

# #计算矩形得面积和周长
# rectangleLength=int(input('Please input the rectangle length:'))
# rectangleWidth=int(input('Please input the rectangle width:'))
# print('The rectangle area is:', rectangleLength*rectangleWidth)
# print('The rectangle perimeter is:', 2*(rectangleLength+rectangleWidth))

# #计算圆的面积和周长
# pi=3.14159
# radius=float(input('Please input the radius of the circle:'))
# print('The area of the circle is:', pi*radius**2)
# print('The circumference of the circle is:', 2*pi*radius)

# #计算y=2x-2的斜率、x截距和y截距
# print('y=2x-2')
# print('The slope of the line is:', 2)
# print('The y-intercept is:', -2)
# print('The x-intercept is:', 0)

# #斜率是 (m = y2-y1/x2-x1)。找到点 (2, 2) 和点 (6,10) 之间的斜率和欧几里得距离
# point1=(2,2)
# point2=(6,10)
# x1,y1=point1
# x2,y2=point2
# m=(y2-y1)/(x2-x1)
# print('The slope of the line is:', m)
# distance=((x2-x1)**2+(y2-y1)**2)**0.5
# print('The distance between the two points is:', distance)

# #比较上面两者的斜率
# slope1=2
# slope2=m
# print(slope1)
# print(slope2)
# print(slope1 > slope2)

# #计算 y 的值（y = x^2 + 6x + 9）。尝试使用不同的 x 值，并找出 y 何时为 0
# while True:
#     x=float(input('Please input the value of x:'))
#     y=x**2+6*x+9
#     print('The value of y is:', y)
#     if y==0:
#         print('y=0 at x=', x)
#         break

# #求出 'python' 和 'dragon' 的长度，并进行一个假的比较语句。
# print('The length of "python" is:', len('python'))
# print('The length of "dragon" is:', len('dragon'))
# print( len('python') > len('dragon'))

# #使用 and 运算符检查 'python' 和 'dragon' 中是否都有 'on'
# print('on' in ('python' and 'dragon')) # True
# print('on' in 'python' and 'dragon')

# #I hope this course is not full of jargon。使用 in 运算符检查句子中是否有 jargon。

# if 'jargon' in 'I hope this course is not full of jargon':
#     print('Yes, there is jargon in the sentence.')

# #找到文本 python 的长度，并将该值转换为浮点数，然后将其转换为字符串。
# string1=len('python')
# print(string1)
# stringConverted=str(float(string1))
# print(type(stringConverted))
# print(stringConverted)

# #偶数可以被 2 整除，余数为零。如何使用 Python 检查一个数字是偶数还是奇数
# num=int(input('Please input a number:'))
# if num%2==0:
#     print(num,'is even')
# else:
#     print(num,'is odd')

# #检查 7 除以 3 的Floor除法是否等于 2.7 的整数转换值。
# num1=7/3
# num2=7//3
# print(int(num1))
# print(num2)
# if int(num1)==num2:
#     print('7 除以 3 的Floor除法等于 2.7')
# else:
#     print('7 除以 3 的Floor除法不等于 2.7')

# # 编写一个 Python 脚本，显示以下表格
# # 1 1 1 1 1
# # 2 1 2 4 8
# # 3 1 3 9 27
# # 4 1 4 16 64
# # 5 1 5 25 125
# #注意for循环前面打印的内容和for循环打印的内容平级
# tuple1=(1,2,3,4,5)
# for i in tuple1:
#     print()
#     print(i, end=' ')
#     for j in range(1,5):
#         print(i**(j-1), end=' ')
# print()
