'''
在Python代码中，变量的名称不能随意定义，要遵循一定的命名规则：
① 变量名称只能由字母、数字或者下划线组成
② 不能由数字开头（只能由字母或下划线开头）
③ 严格区分大小写
A=10
print(a)
④ 不能使用Python内置保留关键字

例1：请问123abc是一个正常的Python变量么？答：不是
例2：请问abc_123是一个正常的Python变量么？答：是
例3：请问_=10，这个定义是否会报错？答：不会报错
例4：请求abc-123=10是一个正常的Python变量么？答：不是
'''
help('keywords')