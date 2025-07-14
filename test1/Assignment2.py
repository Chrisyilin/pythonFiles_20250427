"""
实现程序:
用户输入一串小写的英文字母, 求出英文字母有几种？并格式化输出

例如：
输入 agbcppdcdho    输出：其中有 a b c d g h o p 8种英文字母
"""
'''
words1 = input('Please input any words: ')   # aBBCCgbcppdcdho   aabbcc
words = list(x for x in words1 if x.islower())   # aBBCCgbcppdcdho   aabbcc
sets = sorted({x for x in words})
f_sets = ' '.join(sorted({x for x in words}))

print(f'用户当前输入：{words1}， 其中有{f_sets} , {len(sets)} 种小写英文字母')
'''





'''
#  推导式
# 生成 0~4 的平方数
for i in range(1,5):
    print(i, i ** 2)

squras = [x ** 2 for x in range(1,5)]

print(squras)

# 提取偶数
evens = [x for x in range(10) if x % 2 == 0]
evens = [x for x in range(10) if x % 2 == 0]
print('evens: ',evens)
# 提取奇数
odd = [x for x in range(10) if x % 2 == 1]
print('odd: ', odd)
'''



""" 
请用户输入三个不同的整数, 输入时用空格隔开, 利用条件语句判断出这三个整数中的最大值  1 3 2 5 4 7 6
"""
'''
num = input('Pleaae input three different integers: ')
try:
    lst_num = num.split(' ')

except ValueError:
    print('Please check your input~')

lst_num.sort()
print(lst_num)
print(lst_num[-1])
'''




"""
已知字典 d = {'a': 100, (): '9', 8.1: 'b', True: 3+4j}, 计算键和值中所有数字类型的数据之和

即: 100 + 8.1 + True + 3+4j = 112.1+4j
"""
d = {'a': 100, (): '9', 8.1: 'b', True: 3+4j}
lst_d = list()
lst_d.extend(list(d.keys()))
lst_d.extend(list(d.values()))

# lst_d = list(d.keys()) + list(d.values())

print('---===---', lst_d)

num_d = [x for x in lst_d if type(x) in (int, float, bool, complex)]
print('num_d: ', num_d)
sum_num_d = sum(num_d)
exp_num_d = str(x for x in num_d).split()

f_d = ' +'.join(str(num_d).split(','))
print(f'计算: {f_d[1:-1]} = {sum_num_d}')

f1_d = [f'({x})' if isinstance(x, complex) else str(x) for x in num_d]
f2_d = '+'.join(f1_d)
print('f1_d: ', f1_d)
print('f2_d: ', f2_d)



# 构造表达式字符串：注意 complex 类型加括号
expr_parts = [f'({x})' if isinstance(x, complex) else str(x) for x in num_d]
expr_str = ' + '.join(expr_parts)

# 输出
print(f"计算: {expr_str} = {sum_num_d}")





