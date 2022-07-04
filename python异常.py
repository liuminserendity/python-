# python异常
# 基础形式：try-except
'''
1.try语法块中放置的是可能会出现错误的代码
2.except语法块中存放的是出错之后的执行代码
try:
	print(5/0)
except ZeroDivisionError:
	print("zero can't divide!")
'''


# 增强形式：try-except-else:如果代码A发生了异常，则会走到代码B的逻辑，最后不管有没有发生异常都会走到代码C
"""try:
    代码A
except [exception] as e:
    代码B
else:
    代码C"""
"""
依赖于try代码块成功执行的代码都应放到else代码块中
try:
	result = 5/2
except ZeroDivisionError:
	print("zero can't divide!")
else:
	print(result)
"""

# 捕获所有异常
"""try:
	print(5/0)
except Exception as e:
	print(e)
"""

# try-except-finally:如果代码A发生了异常，则会走到代码B的逻辑，最后不管有没有发生异常都会走到代码C
"""
try:
    代码A
except [exception] as e:
    代码B
finally:
    代码C
"""
