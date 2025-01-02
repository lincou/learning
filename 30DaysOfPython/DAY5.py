# #列表
# Python 中有四种集合数据类型：
# List：有序且可变的集合。允许重复的成员。
# Tuple：有序且不可变的集合。允许重复的成员。
# Set：无序、不可索引且不可变的集合，但我们可以向集合中添加新项。不允许重复的成员。
# Dictionary：无序、可变且可索引的集合。不允许重复的成员。
# 列表是不同数据类型的集合，有序且可修改（可变）。列表可以为空，也可以包含不同数据类型的项。
lst=[1,2,3,4,5]
first_item, second_item, third_item,*rest_items = lst
print(first_item)

fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[0:4] # 返回所有项
#与上面返回值相同
all_fruits = fruits[0:] # 如果不指定结束索引，将返回从开始到最后一项的所有项
orange_and_mango = fruits[1:3] # 不包含第一项
orange_mango_lemon = fruits[1:]
orange_and_lemon = fruits[::2] # 我们使用了第三个参数，步长。 每两项取一条 - ['banana', 'mango']