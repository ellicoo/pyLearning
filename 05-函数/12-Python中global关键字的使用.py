'''
思考一个问题：我们是否可以在局部作用域中修改全局变量？
答：默认是不可以的，但是我们可以通过global关键字，在局部作用域中声明全局变量（引用全局变量）
基本语法：
全局变量num
def func():
    global num  # 声明全局变量（引用全局中的变量num）
    num = 100
'''
# 1、定义一个全局变量
num = 10

# 2、定义一个函数
def func():
    # 声明全局变量
    # global num
    # 基于global声明的全局变量，对其进行修改
    num = 100

# 4、调用func函数
func()
print(num)  # 10（没有修改） 100（已经被修改）