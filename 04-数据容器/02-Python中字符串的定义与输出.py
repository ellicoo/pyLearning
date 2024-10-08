'''
在Python代码中，我们可以使用单引号或者三引号方式定义字符串。
注意：
在Python中，字符串定义无论使用单引号还是双引号，效果是完全一致的。
如何区分三引号是多行注释，还是字符串的定义呢？
答：如果三引号定义的内容，赋值给其他变量，就代表这是字符串；反之则认为是多行注释
'''
str1 = 'abc'
str2 = 'hello world'
str3 = '''
    锄禾日当午，
    汗滴禾下土。
    谁知盘中餐，
    粒粒皆辛苦。
'''

print(str3)
print(type(str3))