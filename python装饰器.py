import threading
import time

# 1.普通写法：函数主要功能（输出奇数）与辅助功能（记录时间）耦合在一起，不方便修改，容易出Bug
"""
def print_odds():
    start = time.time()
    for i in range(1, 1000000):
        if i % 2 == 1:
            print(i)
    print("函数执行时间：", time.time() - start)


print_odds()
"""

# 2.函数优化:分离函数主要功能与辅助功能
"""
def count_time(func):
    start_time = time.time()
    func()
    print("函数运行时间：", time.time() - start_time)


def count_time(func):
    start_time = time.time()
    func()
    print("函数运行时间：", time.time() - start_time)


def print_odds():
    for i in range(1, 100000):
        if i % 2 == 1:
            print(i)


count_time(print_odds)


count_time(print_odds)
"""

# 3.闭包函数:一个其参数和返回值都是函数的函数，面向切面编程（AOP）
"""
def print_odds():
    for i in range(1, 100000):
        if i % 2 == 1:
            print(i)


def count_time_wrapper(func):
    def improve_func():
        start_time = time.time()
        func()
        print("函数运行时间：", time.time() - start_time)

    return improve_func


print_odds = count_time_wrapper(print_odds)
print_odds()
"""

# 函数装饰器:函数装饰器的语法糖
# 装饰器用来第一次被调用时给函数增强
"""
def count_time_wrapper(func):
    def improve_func():
        start_time = time.time()
        func()
        print("函数运行时间：", time.time() - start_time)

    return improve_func

# @后面跟装饰函数名
@count_time_wrapper   # 装饰器
def print_odds():
    for i in range(1, 100000):
        if i % 2 == 1:
            print(i)


# 装饰器等价于第一次调用函数时执行下列语句
# print_odds = count_time_wrapper(print_odds)
print_odds()
# __name__ --> 返回函数或类的函数名
print(print_odds.__name__)  # improve_func
"""

# 有参数和返回值的函数装饰器
"""
1.对于含有返回值的函数，调用闭包增强后，不能成功返回，但是成功增强了辅助功能
2.对于含有参数的函数，调用闭包增强后，不能成功接收参数
"""

"""
def count_time_wrapper(func):
    # 增强函数应该把接收到的所有参数发送给原函数
    def improve_func(*args,**kwargs):
        start_time = time.time()
        res = func(*args,**kwargs)
        print("函数运行时间：", time.time() - start_time)
        return res   # 增强函数的返回值就是原函数的返回值

    return improve_func


# @后面跟装饰函数名
@count_time_wrapper  # 装饰器
def print_odds(lim):
    for i in range(1, lim):
        if i % 2 == 1:
            print(i)
    return "刘敏"


# 装饰器等价于第一次调用函数时执行下列语句
# print_odds = count_time_wrapper(print_odds)
# print_odds(100)
print(print_odds(10000))
"""

# 两个装饰器:按装饰器自上而下位置，顺序的执行
"""
def wrapper1(func1):
    print('set func1')

    def improved_func1():
        print("call func1")
        func1()

    return improved_func1


def wrapper2(func2):
    print('set func2')

    def improved_func2():
        print("call func2")
        func2()

    return improved_func2


@wrapper1
@wrapper2
def original_func():
    pass


original_func()
print(original_func.__name__)   # improved_func1
print("-----------")
original_func()
print(original_func.__name__)  # improved_func1

# 输出
set func2
set func1
call func1
call func2
-----------
call func1
call func2
"""