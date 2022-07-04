import numpy as np
import random

print(np.arange(1, 100, 2))
print(np.array([1, 2, 3, 4, 5, 6, 7, 8, 9]))
# 死循环
while True:
    num = random.randint(0,100)
    if int(num) == 100:
        print("输出成功:",num)
        break
