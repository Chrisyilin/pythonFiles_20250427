import numpy as np

def f(arr):
    return arr * 10


res = f(np.random.randint(1, 10, size=(2, 3)))
print(res)




print("执行第1行啦")
print(2 / 1)
print("执行第3行啦")
a = 123
print(a)


# 定义函数func
def func(left, right):
    print("执行第9行啦")
    print("执行第10行啦", left + right)
    print("执行第11行啦", left - right)
    print("执行第12行啦", left * right, left / right)

print(func)  # 会输出函数的内存地址
print("执行第15行啦")
func(3, 4)

a = 124
print(a)

print("十进制：", 101)
print("二进制：", 0b101)
print("八进制：", 0o101)
print("十六进制： ", 0x101)














print("------------------------------------------------------")


"""
定义 f(x) = 3x + 1

"""
#
# def f(x):
#     return 3*x + 1
#
#
# x = int(input("Which number is your like best? Please input: "))
# print(f(x))


print("------------------------------------------------------")

"""

定义 f(x, h, k) = 3x + 2h - k + 4

求 f(1, 2, 3)
求 f(2, 1, 3)
求 f(3, 2, 1)

# def which means define.

z是一个可选参数
"""

def f3(x, h, k, z = None):
    if z is None:
        # return 3 * x + 2 * h - k + 4
        # 返回空
        return z
    else:
        return 3 * x + 2 * h - k + 4 + z

x1, h1, k1, z1 = 1, 2, 3, 1
x2, h2, k2 = 2, 1, 3
x3, h3, k3 = 3, 2, 1

print("x1, h1, k1, z1: ", f3(x1, h1, k1, z1))
print("x2, h2, k2: ", f3(x2, h2, k2))
print("x3, h3, k3: ", f3(x3, h3, k3))

import builtins

print("🐱😁")



print("------------------------------------------------------")









