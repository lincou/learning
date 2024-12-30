# #字符串用单引号或者双引号'',""
# #多行字符串使用三个单引号 (''') 或者三个双引号 (""") 创建
# #字符串联
# first_name = 'Asabeneh'
# last_name = 'Yetayeh'
# space = ' '
# full_name = first_name  +  space + last_name
# print(full_name) # Asabeneh Yetayeh

# %s - 字符串 (或者任何可以用字符串表述的对象，例如数字)
# %d - 整型
# %f - 浮点型
# "%.小数位数f" - 固定精度的浮点数

#将字符串 'Thirty', 'Days', 'Of', 'Python' 连接为一个字符串 'Thirty Days Of Python'。
String1 = 'Thirty'
String2 = 'Days'
String3 = 'Of'
String4 = 'Python'
print(String1+' '+String2+' '+String3+' '+String4)

company='Coding For All'
print(company[0:6])#从零索引开始，直到 6 但不包括 6
print(len(company))
print(company.upper())#全部大写
print(company.lower())#全部小写
print(company.capitalize())#首字母大写
print(company.title())#每个单词的首字母大写
print(company.swapcase())#大小写互换
print(company.index('Coding'))#查找子串的索引位置
print(company.replace('Coding','Python'))
print(company.split(' '))
company2='Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
print(company2.split(','))
print(company[(len(company)-1)])#在Python中，字符串的索引是从 0 开始的。也就是说，第一个字符的索引是 0，第二个字符的索引是 1，一直到最后一个字符。为了得到最后一个字符的索引，我们需要用字符串的长度减去 1。
#为名称 'Coding For All' 创建首字母缩略词或缩写。
words = company.split()
acronym =''.join(word[0] for word in words)
print(acronym)

#使用索引确定 'Coding For All' 中 C 第一次出现的位置和F 第一次出现的位置。
print(company.index('C')) #index() 方法查找子串的索引位置，如果没有找到，则会引发 ValueError 异常。
print(company.find('F')) #find() 方法查找子串的索引位置，如果没有找到，则会返回 -1。
#使用 rfind 确定 'Coding For All People' 中 l 最后一次出现的位置。
print(company.rfind('l'))

#删除以下句子中短语 'because because because'：'You cannot end a sentence with because because because is a conjunction'
sentence = 'You cannot end a sentence with because because because is a conjunction'
new_sentence = sentence.replace('because because because', '')
print(new_sentence)
print(sentence.find('because'))
#''Coding For All' 是否以子字符串 Coding 开头？
print(company.startswith('Coding'))
#''Coding For All' 是否以子字符串 Coding 结尾？
print(company.endswith('Coding'))
#'   Coding For All      '  , 删除给定字符串中左右空格。
print(company.strip())

print('30DaysOfPython'.isidentifier())
print('thirty_days_of_python'.isidentifier())


## join(): 返回连接后的字符串
# web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
# result = ' '.join(web_tech)
# print(result) # 'HTML CSS JavaScript React'
# web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
# result = '# '.join(web_tech)
# print(result) # 'HTML# CSS# JavaScript# React'
#以下列表包含一些 Python 库的名称：['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']。使用空格连接字符串。
libs = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(' '.join(libs))

#换行
print('I am enjoying this challenge.\nI just wonder what is next.')
#使用制表符专业序列输出
print('Name\t\tage\tCountry\tCity\n')
print('Asabeneh\t250\tFinland\tHelsinki')

#使用字符串格式化方法
radius = 10
area = 3.14 * radius ** 2
#The area of a circle with radius 10 is 314 meters square.
print('The area of a circle with radius {} is {:.0f} meters square.'.format(radius, area))#使用 {:.0f} 格式化输出整数
print('The area of circle with a radius %d is %.2f.' %(radius, area))#使用 %d 和 %.2f 格式化输出浮点数

#新式字符串格式化 (str.format)
a = 8
b = 6

print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b)) # 限制保留两位小数
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))

#字符串插值 / f-Strings (Python 3.6+)
a = 4
b = 3
print(f'{a} + {b} = {a +b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')