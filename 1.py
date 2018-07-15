a = None
print('能量来源如下：')
print('行走捐、生活缴费、共享单车、线下支付、网络购票')
while a != str(0):
    a = input('请输入查询能量来源！退出请输入0：')
    if a == '行走捐':
        print('200g')
        continue
    elif a == '生活缴费':
        print('300g')
        continue
    elif a == '共享单车':
        print('350g')
        continue
    elif a == '线下支付':
        print('380g')
        continue
    elif a == '网络购票':
        print('500g')
        continue
print('已退出')
