'''
闭包函数构成条件一共有三步：① 有嵌套 ② 有引用 ③ 有返回
def outer():
    num = 100  # 局部变量
    print(num)

outer()  # 执行outer函数
print(num)  # 尝试访问函数内部的局部变量 => 直接报错，因为函数执行完毕后，其内部变量会消失

闭包三步走：① 有嵌套 ② 有引用 ③ 有返回
闭包的作用：保留函数内部的局部变量不会随着函数的执行结束而消失，而是一直主留在计算机内存中
'''


# 1、有嵌套，外层函数嵌套了一个内层函数
def outer():
    num = 100  # 局部变量

    def inner():
        # 2、有引用，内层函数引用了外层函数中的局部变量
        print(num)

    # 3、有返回，外层函数的返回值是内层函数在内存中的地址 => 返回内层函数的名称
    return inner


# 4、调用outer()函数
func = outer()  # 把outer()函数返回值，赋值给某个变量
func()  # 找到inner函数并执行其内部的代码，弹出100
func()  # 再次调用func()，依然可以正常访问outer函数内部的局部变量100
