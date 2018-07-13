a = input('请输入一个年份:')
if ((int(a)%4==0)and(int(a)%100!=0))or(int(a)%400==0):
    print('闰年')
else:
    print('非闰年')
