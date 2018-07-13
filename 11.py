a = input('今有物不知其数,三三之数剩二，五五之数剩三，七七之数剩二，问几何?请打出你的答案:')
if (int(a)%3==2)and(int(a)%5==3)and(int(a)%7==2):
    print('正确')
else:
    print('输入有误')
