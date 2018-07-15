while True:
    a = int(input('你的年龄:'))
    b = input('你的专业:')
    c = input('是否为重点大学:')
    if a>=25 and b=='电子信息工程专业':
        print('面试资格获取成功')
        continue
    elif b=='电子信息工程专业' and c=='是':
        print('面试资格获取成功')
        continue
    elif b=='计算机专业' and a<28:
        print('面试资格获取成功')
        continue
    else:
        print('抱歉,您未达到面试要求')
