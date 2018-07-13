a = input('输入每100毫升血液酒精含量(向下取整):')
if int(a)<20:
    print('不构成饮酒行为')
elif (int(a)>=20) and (int(a)<80):
    print('饮酒驾车')
else:
    print('醉酒驾车')
