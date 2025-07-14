# 给定时间字符串 t = "2025/02/28-14:35:48"，提取月份和分钟数并计算它们的乘积
t = "2025/02/28-14:35:48"

# 方法一
print(t[5:7], t[-5:-3], int(t[5:7]) * int(t[-5:-3]))

# 方法二
months = int(t.split('/')[1])
min = int(t.split(':')[1])
print(months * min)

# 方法三
months = int(t[t.find('/')+1:t.rfind('/')])
min = int(t[t.find(':')+1:t.rfind(':')])
print(months * min)


# 给定字符串 s = "12a3a4AA5A"，求出'A'字符和'a'字符的数量差
s = '12a3a4AA5A'
sA = s.count('A')
sa = s.count('a')
print(f's: {s} \nsA:{sA} \nsa: {sa} \nA和a数量差: {sA-sa}')



# 已知 lst = [1, 3, 2, 6, 4], 程序实现: 删除lst元素中的中位数（只考虑列表中元素个数为奇数的情况）
lst = [1, 3, 2, 6, 4]
sorted_lst = sorted(lst)  # [1, 2, 3, 4, 6]
median_index = len(sorted_lst) // 2
median_index1 = int(len(sorted_lst)) / 2
print(median_index, median_index1)

lst.remove(sorted_lst[median_index])
print('--==--',lst)



lst = [1, 3, 2, 6, 4]
sort_lst = sorted(lst)
median = sort_lst(int(len(lst) / 2))
lst.remove(median)
print('median: ', median)
print('lst: ', lst)



# 已知 lst = [1, 3, 2, 6, 1, 1, 41], 程序实现: 求lst中最后一个为1的元素的索引
lst = [1, 3, 2, 6, 1, 1, 41]
print('len(lst): ',len(lst))
print('lst[::-1]: ',lst[::-1])
lst.reverse()
print('lst.reverse(): ',lst)
j = 0
for i in range(len(lst)):
    if lst[i] == 1:
        j = i
        # print(j)

print('lst中最后一个为1的元素的索引', j)


# 通过chatGPT学习到：
lst = [1, 3, 2, 6, 1, 1, 41]
print('最后一个为1的索引:', len(lst) - 1 - lst[::-1].index(1))

print(lst[::-1])

"""
编写一个程序, 帮助水果店实现计价功能:
请用户输入水果品种, 水果单价(元/kg)和重量(kg),
计算出需要花费的金额并做格式化输出

例:
用户输入水果品种为: 苹果
输入单价为: 3.98
输入重量为: 2.58
根据用户输入数据计算出总价为: 10.2684

请用三种字符串格式化方式输出如下结果:
您购买了2.58kg的苹果, 单价为3.98元/kg, 您需要支付10.27元!
"""
# %格式化
fruits = input('Please input the name of the fruit you like best: ')
format_print = ''
def choose_fruits(fruits, format_print):
    try:
        unit_price, weights = 0, 0

        if fruits in ('苹果', 'apple'):
            unit_price = 3.98
            weights = 2.58
        elif fruits in ('梨', 'pear'):
            unit_price = 2.98
            weights = 3.12
        else:
            unit_price = 1.11
            weights = 1.11

        total_price = round(unit_price * weights, 2)

        if format_print == '%':
            final_print = ('%% : You just bought %.2f kg of %s, '
                        'their unit price is %.2f Yuan per kg. '
                        'So you need to pay %.2f Yuan')%(weights, fruits, unit_price, total_price)
        elif format_print == 'format':
            final_print = ('format : You just bought {}kg of {}, '
                           'their unit price is {} Yuan per kg. '
                           'So you need to pay {} Yuan').format(weights,fruits, unit_price, total_price)
        elif format_print == 'f-string':
            final_print = (f'f-string : You just bought {weights}kg of {fruits}, '
                           f'their unit price is {unit_price} Yuan per kg. '
                           f'So you need to pay {total_price} Yuan')
        else:
            print('Please review your code!')
        return final_print

    except ValueError:
        return 'The process has crashed, pleaae contact the engineer to check.'

print(choose_fruits(fruits, '%'))

# format格式化
print(choose_fruits(fruits, 'format'))


# f-string格式化
print(choose_fruits(fruits, 'f-string'))



