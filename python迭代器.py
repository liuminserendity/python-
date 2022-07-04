# 迭代器
"""
1.可迭代对象:可以用for循环遍历的对象都是可迭代对象。
● str,list,tuple,dict,set等都是可迭代对象。
● generator，包括生成器和带yield的生成器函数

2.判断是否可迭代：使用 isinstance("对象",Iterable) 判断一个对象是否是 Iterable 对象
from collections import Iterable,Iterator

3.迭代器对象
● 有内置的__next__()方法的对象，执行该方法可以不依赖索引取值
● 有内置的__iter__()方法的对象，执行迭代器的__iter__()方法得到的依然是迭代器本身

4.可迭代对象不一定是迭代器

5.iter()方法:将可迭代的对象(Iterable)，转为迭代器(Iterator)

6.注意:
1.迭代器不可以通过下标取值，而是使用__next__()或者next()。但是只要超出范围则直接报错StopIteration
2.next()只能顺延调用，不能往前

7.可迭代对象与迭代器区别
● 可用于for循环的都是可迭代类型
● 作用于next()都是迭代器类型
● list、dict、str等都是可迭代的但不是迭代器,因为next()函数无法调用它们。可以通过iter()函数将它们转为迭代器
● python的for循环本质就是通过不断调用next()函数实现的
"""
from collections.abc import Iterable, Iterator

str1 = "sefefr"
print(isinstance(str1, Iterable))
print(isinstance(str1,Iterator))

# 创建迭代器
str_iter = iter(str1)
print(next(str_iter))
print(next(str_iter))
print(next(str_iter))
print(next(str_iter))
print(next(str_iter))
print(next(str_iter))
print(next(str_iter))   # 超出范围:StopIteration


