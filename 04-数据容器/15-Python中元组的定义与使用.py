'''
元组的特点：基于小括号实现定义，一旦定义成功后，则其内部的元素就不能修改和删除了
作用：保护数据

基本语法：
元组变量 = (元素1, 元素2, 元素3, ...)

元素和列表类似，也可以实现大批量数据的存储，其内部的每一个元素也有与之对应的索引下标，唯一区别：元组一旦定义成功，就不能修改和删除了
'''
# 1、定义一个元组类型的数据（单元素元组）
tuple1 = (10,)  # 注意：单元素元组，结尾必须保留一个逗号
# 2、定义一个元组类型的数据（多元素元组）
tuple2 = (10, 10, 20, 30)
# 3、打印输出元组与元组的数据类型
print(type(tuple1))
print(type(tuple2))
# 4、尝试修改元组 => 查看是否报错
print(tuple2[0])
print(tuple2[1])
print(tuple2[2])

tuple2[2] = 100  # 直接报错：'tuple' object does not support item assignment
