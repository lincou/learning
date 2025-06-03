# # #列表
# # Python 中有四种集合数据类型：
# # List：有序且可变的集合。允许重复的成员。
# # Tuple：有序且不可变的集合。允许重复的成员。
# # Set：无序、不可索引且不可变的集合，但我们可以向集合中添加新项。不允许重复的成员。
# # Dictionary：无序、可变且可索引的集合。不允许重复的成员。
# # 列表是不同数据类型的集合，有序且可修改（可变）。列表可以为空，也可以包含不同数据类型的项。
# lst=[1,2,3,4,5]
# first_item, second_item, third_item,*rest_items = lst
# print(first_item)

# fruits = ['banana', 'orange', 'mango', 'lemon']
# all_fruits = fruits[0:4] # 返回所有项
# #与上面返回值相同
# all_fruits = fruits[0:] # 如果不指定结束索引，将返回从开始到最后一项的所有项
# orange_and_mango = fruits[1:3] # 不包含第一项
# orange_mango_lemon = fruits[1:]
# orange_and_lemon = fruits[::2] # 我们使用了第三个参数，步长。 每两项取一条 - ['banana', 'mango']

# n = 0
# name = ['tim', 'charlie', 'susan', 'cathy']
# while n<4:
#     print('Hello',name[n].title())
#     n+=1
# data = {"name": "Alice", "age": 25}
# print(f"{data=}")

# #修改、添加、删除列表元素
# name.append('mike')
# print(f"{name=}")
# name.insert(2,'lincou')
# #不能写成 print(f"{name.title()}") 因为name是一个列表，不是字符串
# #如果需要给name列表中的每个字符串的首字母大写，可以使用列表推导式
# print(f"{[name.title() for name in name]}")

# pizzas=['cheese','pepperoni','mushrooms']
# for pizza in pizzas:
#     print(f"I like {pizza} pizza.")
# print("I really love pizza!")

squares = [] 
for value in range(1,11): 
     square=value**2
     squares.append(square) 
print(squares)

#列表解析
squares = [value**2 for value in range(1,11)]
print(squares)

num=[]
numbers =range(3,30)
for number in numbers:
     if number%3==0:
          num.append(number)
print(num)

num3=[]
numbers3=range(1,11)
for number in numbers3:
     num3.append(number**3)
print(num3)

num4=[number**3 for number in range(1,11)]
print(num4) 