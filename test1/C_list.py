


# str.find()

s = 'hello worlD'
print(s.find('l'))
print(s.find('l',3))
print(s.find('l',9,10))
print(s.rfind('l'))
print(s.rfind('l', 3,4))
print(s.rindex('l',3,4))

print(s.capitalize())
print(s.title())
print(s.upper())
print(s.lower())
print(s.swapcase())





'''
# str.count() 计数
s = 'hello world'
print(s.count('l'))
print(s.count('l',2))
print(s.count('l',3))
print(s.count('l',3,4))
print(s.count('l',3,9))
print(s.count('l',3,10))
'''




'''
# str.join
s = '-.'
s1 = 'hello world'
s2 = ['1', '2', '3', '4']
s3 = {'张三':'1', '李四':'2'}
s4 = {'王五', '赵六',  'ABC'}
print(s.join(s1))
print(s.join(s2))
print(type(s.join(s2)))
print(s.join(s3))
print(s.join(s4))
'''





'''
# str.split() 分隔，返回一个列表
# 如果开头就符合分隔，会切出一个空字符串
s = 'Line1   \n   Line2  Line3'
print(s.split())
print(type(s.split()))
print(s.split(' '))
print(s.split('L'))
print(s.split('L', 1))

s1 = 'hello,hello,hello'
print(s1.split(' '))
print(s1.split('h'))   # ['', 'ello,', 'ello,', 'ello']
'''


'''
# 判断字符串是否 只包含数字字符，且每个字符必须是 '0' 到 '9'，不能有负号、点、小数、空格等
str1 = '1234'
str2 = '-1234'
str3 = '1.234'
print(str1.isdigit())
print(str2.isdigit())
print(str3.isdigit())
'''


'''
def isNumber(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

print(isNumber(22))
print(isNumber('abc'))
'''




'''
# 判断字符串是否以xx结尾，str.endswith()
str = 'hello world'
print(str.endswith('d'))
print(str.endswith('ld'))
print(str.endswith('lld'))
print(str.endswith('l',1))
print(str.endswith('l',1,3))
print(str.endswith(('or','d')))
'''




'''
# 判断字符串是否以xx开头  str.startswith()
str = 'hello world'
print(str.startswith('h'))  # True
print(str.startswith('H'))  # false
print(str.startswith('e'))  # False
print(str.startswith('e',1))  # True
print(str.startswith('lo',3,6))  # True
print(str.startswith('lo',2,3))  # False
print(str.startswith(('wo','h')))   # True
'''





'''
# 去字符串两边的空格或者其他字符
str = ' \n hello world\n'
print(str)
print(str.strip())
print(str.strip('d'))

str1 = 'oohello world'
print(str1.strip('o'))
print(str1.strip('od'))

str2 = 'www.example.com'
print(str2.strip('cwom'))
'''






'''
# 截取
str1 = 'Line1, Line2, line3'
# 默认字符串中出现的所有符合的都被替换
print(str1.replace('L','p'))
# count = -1默认参数，所有都会替换
print(str1.replace('L','p', -1))
# count = 1，字符串只会替换一次
print(str1.replace('L','p', 1))
'''





'''
# 字符串格式化
name, age, times = 'Tom', 2, 10.8

# f-string格式化
print(f"它说它叫 {name} ，\n今年 {age} 岁，每天睡 {times} 小时")
print(fr"它说它叫 {name} ，\n今年 {age} 岁，每天睡 {times} 小时")

# 字符串格式化
# %.2f : 表示精确到小数点后n位
print("它说它叫%s，今年%d岁，每天睡%.2f小时"%('Tim', 5, 12.5 * 1.012))

# fomat方法格式化：传位置参数，实参按照从左到右的顺序传入占位符{}
print(("它说它叫{}，今年{}岁，每天睡{}小时").format(name, age, times))

# 传关键字参数
print(("它说它叫{a}，今年{b}岁，每天睡{c}小时").format(a = name, c = times, b = age))

# 根据实参的下标传输
print(("它说它叫{2}，今年{0}岁，每天睡{1}小时").format(age, times, name))
'''







"""
# del函数
lst1 = [567, 'hello', 456, [789, 'abc'], 'world', 'coco1', 'coco2', 3.33]
lst2 = lst1
print(lst1)
print(lst2)
print(id(lst1))
print(id(lst2))

del lst1
# print(lst1)
print(lst2)

print()

del lst2[1]
print(lst2)
print(lst2[3])

del lst2[1], lst2[3]
print(lst2)

print(lst2[:3:2])
del lst2[:3:2]
print(lst2)
"""