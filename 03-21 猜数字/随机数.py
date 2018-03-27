import random
i = 1
a = random.randint(0,10)
b = int(input("请输入一个0到10的整数"))
while a != b:
    if b < 0 or b > 10:
        print("输入错误请重新输入")
        i += 1
        b = int(input("请输入一个0到10的整数"))
    elif a > b:
        print("你输入的数比该数小")
        i += 1
        b = int(input("请输入一个0到10的整数"))
    elif a < b:
        print("你输入的数比该数大")
        i += 1
        b = int(input("请输入一个0到10的整数"))
else:
    print("恭喜你猜中了！")
    print(i)

