'''
编写一个函数，有一个参数str1，输入信息如‘1.2.3.4.5’，使用函数对其进行处理，要求最终的返回结果为'5-4-3-2-1'
'''
# 1、定义一个函数，如func，有一个str1参数
def func1(str1):
    # 3、对字符串进行处理
    # 第一步：使用split切割
    list1 = str1.split('.')
    # 第二步：使用join进行拼接
    newstr = '-'.join(list1)
    # 第三步：使用切片翻转字符串
    return newstr[::-1]

# 2、调用func函数，传递数据1.2.3.4.5
print(func1('1.2.3.4.5'))  # 5-4-3-2-1

# ------------------------------------------------------------------------------------------
def func2(str1):
    # 第一步：直接翻转字符串
    str1 = str1[::-1]
    # 第二步：使用replace()方法实现.点号替换
    return str1.replace('.', '-')

print(func2('1.2.3.4.5'))
