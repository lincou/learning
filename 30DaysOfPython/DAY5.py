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

# furits = ['banana', 'orange', 'mango', 'lemon']
# all_fruits = furits[0:4] # 返回所有项
# #与上面返回值相同
# all_fruits = furits[0:] # 如果不指定结束索引，将返回从开始到最后一项的所有项
# orange_and_mango = furits[1:3] # 不包含第一项
# orange_mango_lemon = furits[1:]
# orange_and_lemon = furits[::2] # 我们使用了第三个参数，步长。 每两项取一条 - ['banana', 'mango']

# n = 0
# name = ['tim', 'charlie', 'susan', 'cathy']
# while n<4:
#     print('Hello',name[n].title())
#     n+=1
# data = {"name": "Alice", "age": 25}
# print(f"{data=}")
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

# words = ["hello world", "python programming"] 
# uppercase_words = [word.title() for word in words]
# print(uppercase_words)

# last_name = name.pop()
# print(f"{name=}")
# print(f"{last_name} is a bad man")

# name = ['tim', 'charlie', 'susan', 'cathy']
# name[2]='mike'
# print(name)
# name.remove('charlie')
# print(name)
# name.insert(0,'lincou')
# print(name)
# name.append('Zero')
# print(name)
# while len(name)>2:
#     last_name = name.pop()
#     print(f"{last_name}, I am sorry to tell you that you don't in this list.")
# del name[0]
# del name[0]

# # print(name)
# name.reverse()
# print(name)
# name.sort(reverse=True)
# print(name)

# To_travell = ['Paris', 'New York', 'Tokyo', 'London', 'Sydney']
# print(sorted(To_travell))
# print(sorted(To_travell, reverse=True))
# print(To_travell)
# To_travell.reverse()
# print(To_travell)
# To_travell.reverse()
# print(To_travell)
# To_travell.sort()
# print(To_travell)
# To_travell.sort(reverse=True)
# print(To_travell)

# players = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank']
# print(players[0:3])
# for player in players[0:3]:
#     print(player)

# #列表复制
# furits = ['banana', 'orange', 'mango', 'lemon']
# furits_copy = furits[:]
# print(f"The first three items in the list are: {furits[0:3]}")
# print(f"The item from the middle of the list are: {furits[1:4]}")

# furits.append('apple')
# furits_copy.append('pear')
# print(furits)
# print(furits_copy)

# users = ['Alice', 'Bob', 'Charlie']#users为空返回值为false，否则为true
# if not users: 
#         print('We need to find some users!')  
# else:
#     for user in users:
#         if user=='admin':
#             print('hello admin, would you like see a status report') 
#         else:
#             print(f'hello {user} nice to meet you')

# alien_0 = {'color': 'green', 'points': 5}
# point_value = alien_0.get('points2', 'No point value assigned.')
# print(point_value)

#函数
# def greet_user(username):
#     """显示简单的问候语"""
#     print(f"Hello, {username.title()}!")

# greet_user('jane')

# def favorite_book(book):
#     """显示用户的最爱书籍"""
#     print(f"Your favorite book is {book.title()}.")

# favorite_book('The Hunger Games')

# def make_shirt(size, message="I love Python."):
#     """制作一件衬衫"""
#     print(f"You have ordered a {size.upper()} shirt. {message.title()}")

# make_shirt('large')
# make_shirt('middle')

# def describe_city(city, country='China'):
#     """描述城市所在国家"""
#     print(f"{city.title()} is in {country.title()}.")

# describe_city('Tokyo', 'Japan')

# def get_formatted_name(first_name, last_name): 
#     """返回整洁的姓名"""
#     full_name = f"{first_name} {last_name}" 
#     return full_name.title() 

# musician = get_formatted_name('jimi', 'hendrix') 
# print(musician) 
# print(get_formatted_name('jimi', 'hendrix')) 

# def build_person(first_name, last_name, age=None): 
#     """返回一个字典，其中包含有关一个人的信息。""" 
#     person = {'first': first_name, 'last': last_name} 
#     if age: 
#         person['age'] = age 
#     return person 
 
# musician = build_person('jimi', 'hendrix', age=27) 
# print(musician) 

class Restaurant:
    def __init__(x, name, cuisine_type,number_served=0):
        x.name = name
        x.cuisine_type = cuisine_type
        x.number_served = number_served
    def describe_restaurant(x):
        print(f"The name of the restaurant is {x.name.title()} and the cuisine type is {x.cuisine_type.title()}")
    def open_restaurant(x):
        print(f"{x.name.title()} is open now!")
    def set_number_served(x,set_number_served):
        x.number_served = set_number_served

    def increment_number_served(x, increment_number_served):
        x.number_served += increment_number_served
    
class User:
    def __init__(x, first_name, last_name, age):
        x.first_name = first_name
        x.last_name = last_name
        x.age = age
        x.login_attempts = 0 

    def reset_login_attempts(x):
        x.login_attempts = 0

    def increment_login_attempts(x):
        x.login_attempts += 1

    def describe_user(x):
        print(f"The user's name is {x.first_name.title()} {x.last_name.title()} and the age is {x.age}")
    def greet_user(x):
        print(f"Hello, {x.first_name.title()} {x.last_name.title()}!")


user1 = User('jane', 'doe', 25)
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print(user1.login_attempts)
user1.reset_login_attempts()
print(user1.login_attempts)
print(f"\n")

restaurant = Restaurant('la casa del diablo', 'Mexican')
print(restaurant.name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.set_number_served(100)
print(restaurant.number_served)
restaurant.increment_number_served(50)
print(restaurant.number_served)