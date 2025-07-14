


print('上传代码到github - 20250714')

num = {x: x ** 2 for x in range(10)}
print(num)

d = {x: x**2 for x in range(4)}
print(d)


'''
lst = [x**2 for x in range(4)]
print(lst)

# 类比，上面和下面这段代码实现结果一样，上面的方式更为简洁
lst = []
for i in range(4):
    lst.append(i ** 2)
print(lst)

for y in range(4):
    print(y,y//2)

lst = [x + y for x in range(10) for y in range(4) if x % 2 == 0 and y // 2 == 1]
lst2 = [x + y for x in range(10) if x % 2 == 0 for y in range(3) if y // 2 == 1]
print(lst)
print(lst2)

for x in range(10):
    if x % 2 == 0:
        for y in range(4):
            if y // 2 == 1:
                print(x + y)


# 三元表达式，
# x是偶数：15>x>5 & x % 2 == 0,
# y是奇数：y<4 & y % 2 == 1

# lst = [x - y if x > 5 and x < 15 else]






for i in range(3):
    score = int(input('input the score:'))
    if score>=90:
        print('Excellent!')
    elif score>=70 and score<90:
        print('Cool')
    elif score>=60 and score<70:
        pass
    else:
        print('Nice')

'''