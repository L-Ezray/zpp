import random
a = input('请输入一个整数[1-10]:')
b = random.randint(1,10)
if int(a) == int(b):
    print('胜利')
else:
    print('失败')
