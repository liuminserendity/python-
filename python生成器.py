# 生成器:在Python中，一边循环一边计算的机制，称为生成器：generator
# 就是当我们想要使用庞大数据，又想让它占用的空间少，那就使用生成器

# 创建生成器表达式:生成器和列表解析类似，但是它使用()而不是[]
"""g = (x for x in range(5))
print(g)   # <generator object <genexpr> at 0x000001DF561DA3C0>
# 取值
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
# print(next(g))   # StopIteration"""

# 生成器函数
"""
当一个函数中包含yield关键字，那么这个函数就不再是一个普通的函数，而是一个generator。
调用函数就是创建了一个生成器对象。其工作原理就是通过重复调用next()或者__next__()方法，
直到捕获一个异常
"""


def yieldTest(number):
    n = 0
    while n < number:
        yield n
        n += 1


res = yieldTest(20)
print(res)  # generator object
print(next(res))  # 0
print(next(res))  # 1
print(next(res))  # 2
"""
yield返回一个值，并且记住这个返回值的位置，下次遇到next()调用时，代码从yield的下一条语句开始执行。
与return的差别是，return也是返回一个值，但是直接结束函数。
"""

"""
迭代器与生成器
● 生成器能做到迭代器能做的所有事
● 而且因为生成器自动创建了iter()和next()方法，生成器显得简洁，而且高效。
"""