# 写代码的习惯：在代码结束行后面 留1-2行空白








print(int(7.8))
print(int(-7.8))
print(round(-7.8923))
print(round(-7.1923))
print(round(7.1923))
print(round(7.8923))
print(round(-7.8923, 3))
print(round(-7.8929, 3))
print((9))

s = "a\\b\\c"
print(s)   # 返回： a\b\c  是str()类型，面向用户，可读性更高
print([s])  # 返回： ['a\\b\\c']  因为是repr()格式，面向开发者，提供调试信息

path = "/Users/OTS00079/PycharmProjects/pythonFiles_20250427/test1/C1.py"
print(path)

print("")
s0 = 'abcdefgh'
s1 = 'a\tbcdefgh'
s2 = 'ab\tcdefgh'
s3 = 'abc\tdefgh'
s4 = 'abcd\tefgh'
s5 = 'abcde\tfgh'
print(s0)
print(s1)
print(s2)
print(s3)
print(s4)
print(s5)


# '''
# print('\099')
# print(0x41)
# print('\100')
# print(chr(65))
# print('\101')
# print('\102')
#
# for i in range(128):
#     # print(f"{i} ==> {chr(i)}")
#     print(f"{i:3} ==> {chr(i)!r}")
#
# str1 = "今天天气很好，小明问我:'走不走?'"
# str2 = '我回:"走啊"'
# str3 = """今天天气很好，小明问我："走不走？" 我回:'走啊'"""
# str4 = '''今天天气很好，小明问我：'走不走？' 我回:"走啊"'''
# str5 = "今天天气很好，小明问我：\"走不走？\" 我回:'走啊'"
# print(str1)
# print(str2)
# print(str3)
# print(str4)
# print(str5)
# print("---    ---    ---    ---    ---    ---")
#
#
# print("https:\\baidu.com\tng.cn")   # https:\baidu.com	ng.cn
# print(r"https:\\baidu.com\tng.cn")   # https:\\baidu.com\tng.cn
# print(R"https:\\baidu.com\tng.cn")   # https:\\baidu.com\tng.cn
#
# print("a\\b\"c\td\ne")
# '''输出：
# a\b"c	d
# e
# '''
#
# print(str())        # ''     空字符串
# print(str('1234'))  # '1234' 字符串本身
# print(str(1234))    # '1234' 把数字转成字符串
# print(str(''))      # ''     空字符串
# print(str(' '))     # ' '    一个空格字符
#
#
#
#
#
# name_str = 'test BJ'
# print(name_str)   # 输出：test BJ
#
# name_str1 = '''test
# BJ '''
# print(name_str1)
# ''' 输出：test
# BJ
# '''
#
# '''这是一个多行注释器，
# 它会被解释器无视'''
#
# print("---    ---    ---    ---    ---    ---")
# '''

"""
print(complex())   # 0j
print(complex(0))   # 0j
print(complex(3.2, 4))   # (3.2+4j)
print(complex(3.2))   # (3.2+0j)
print(complex('3.2'))   # (3.2+0j)
print(complex(3.2+4))   # (7.2+0j)
print(complex(3.2+4j, 2))   # (3.2+6j)
print(complex('3.2+4j'))   # (3.2+4j)
"""

# print("---    ---    ---    ---    ---    ---")

'''
print(bool(set()))    # False
print(bool())
print(bool(0))
print(bool(0.0))
print(bool(0j))
print(bool(None))
print(bool([]))
print(bool(()))
print(bool({}))
print(bool(''))
print(bool(False))
print(bool(' '))
print(bool('False'))
print(bool(True))
print(bool(1))
print(bool(1.2))
print(bool(1.2))
print(bool(-1.2))
'''

# print("---    ---    ---    ---    ---    ---")


"""
print(float())   # 0.0
print(float(2))   # 2.0
print(float(2.1))   # 2.1
print(float(-2.2))   # -2.2
print(float('3'))   # 3.0
print(float('3.2'))   # 3.2
print(float(True))   # 1.0
print(float(False))   # 0.0
"""

# print("---    ---    ---    ---    ---    ---")

"""
print(int())   # 0
print(int(1))   # 1
print(int(1.8))   # 1
print(int(-1.2))   # -1
print(int('2'))   # 2
print(int(True))   # 1
print(int(False))   # 0
# print(int('2.1'))   # ValueError
"""

# print("---    ---    ---    ---    ---    ---")
"""
none = None
print(type(none))
print(none)

# 复数 complex
num = 3 + 0j
print(type(num))
print("复数num的值为: ",num)

num1 = 3 + 4J
print(type(num1))
print("复数num1的值为: ",num1)

num2 = 1j ** 2
print(num2)
#   结果:  (-1+0j)


print("---    ---    ---    ---    ---    ---")



a = 3 * True - 100 * False
print(a, type(a))
# 3 <class 'int'>

a = 2e1
print(a, type(a))
# 20.0 <class 'float'>

b = 2E1
print(b, type(b))
# <class 'int'>

c = 7
print(c, type(c))
# <class 'int'>


tru = True
fs = False
print(tru, fs)
print(type(tru), type(fs))
tru1 = int(tru)
fs1 = int(fs)
print(type(tru1), tru1, type(fs1),fs1)


your_name = input("Please input your real name: ")
your_age = int(input("As well as your real age: "))
print("Hi, 你好，",your_name, ", 一个", your_age , "岁的同学。")



print("Hello World1", "Hello World2", sep = "-", end="eee")
print()
print("Hello World 1 ", "Hello World 2 ")
print("Hello World 1 ", "Hello World 2 ", sep = " ### ", end = "zzz")



luckynumber = 123

def add(x, y):
     print(x + y)

add(1, 3)

print(add)

f = add

print(f)

myLuckyNumberIs = 1
MyLuckyNumberIs = 1

a = 789
num = a

print(a)
print(num)

a=345

print(a)
print(num)



num = 789

a = num

print('num: ', num)
print('a: ', a)

print('num的内存地址: ', id(num))
print('a的内存地址: ', id(a))

print ('------------------------------------')




abc = 1+2-3*4/5**3
print(abc)
print(1,2,3,4+5,5**6,6-2,3.141592)



a = (1 + 2 + 3 + 4 + 5 + 1 + 2 + 3 + 4 +
5 + 1 + 2 + 3 + 4 + 5 + 1 + 2 + 3 + 4 + 5 +
1 + 2 + 3 + 4 + 5 + 1 + 2 + 3 + 4 + 5 + 1 + 2 + 3 + 4 + 5 )

b = 1 + 2 + 3 + 4 + 5 + 1 + 2 + 3 + 4 + \
5 + 1 + 2 + 3 + 4 + 5 + 1 + 2 + 3 + 4 + 5 + \
1 + 2 + 3 + 4 + 5 + 1 + 2 + 3 + 4 + 5 + 1 + 2 + 3 + 4 + 5


c = [123, 'Hello World!',
     "abc", 456, 789]

print(c)

num = 1
Num = 2

print('num: ', num)
print('Num: ', Num)

"""