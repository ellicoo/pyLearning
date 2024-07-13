'''
在计算机内存中，一共分为四大区域：① 堆内存 ② 栈内存 ③ 代码区 ④ 数据区
变量都是引用变量，变量名称 => 栈内存；变量的值 => 数据区中，两者之间是一种引用关系
函数在内存中，如何存储？
函数名称存储在栈内存中，函数体往往存储在代码区中
print(func)  # 打印函数在内存的地址
func()  # 找到函数在内存中的地址，并立即执行其函数体代码
'''
def func():
    num2 = 100
    print(num2)

# 打印func函数在内存中指向的地址
print(func) # 函数名保存的
# 调用func函数
func()