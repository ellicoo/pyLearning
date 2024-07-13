'''
案例：生成一个列表，结构如下：[(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3)]
观察规律：
第一次循环
(1, 1)
(1, 2)
(1, 3)
第二次循环
(2, 1)
(2, 2)
(2, 3)
---------------------------------------
特点：元组左边的相对来说比较固定，要么为1，要么为2
转换为for循环嵌套，外层循环1次，内层循环3次
'''
# 原生代码
list1 = []
for i in range(1, 3):  # 1 2
    for j in range(1, 4):  # 1 2 3
        list1.append((i, j))
print(list1)

# 推导式代码
list2 = [(i, j) for i in range(1, 3) for j in range(1, 4)]
print(list2)

# 尝试操作
# list3 = [(i, j) for i, j in range(1, 3)]  # TypeError: cannot unpack non-iterable int object
# print(list3)
