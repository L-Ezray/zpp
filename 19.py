a = input('请输入身高:')
b = input('请输入身价:')
c = input('请输入颜值分:')
if (float(a)>180)and(float(b)>1000000)and(float(c)>99):
    print('高富帅')
elif (float(b)>1000000)and(float(c)>99):
    print('富帅')
elif (float(a)<160)and(float(b)<100)and(float(c)<60):
    print('矮挫穷')
else:
    print('普通人')
