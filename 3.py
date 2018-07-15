a = None
while True:
    a = int(input('请输入一个数字:'))
    if a == 0:
        continue
    elif a > 0 and a < 100:
        print('命运给予我们的不是失望之酒,而是机会之杯'*a)
    elif a >= 100:
        break
