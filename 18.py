帐号 = '456456456'
密码 = '123123'
money = 100
a = input('请输入帐号:')
b = input('请输入密码:')
if (a==帐号)and(b==密码):
    print('开始取钱')
    c = input('请输入取钱金额:')
    if float(c)<=100:
        print('您本次取钱金额为%s,'%c,'您的余额为',100-float(c))
    else:
        print('没钱取毛线')
else:
    print('非法账户')

