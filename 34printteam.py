print('2017~2018年赛季NBA西部联盟前8名')
team = ['火箭','勇士','开拓者','爵士','鹈鹕','马刺','雷霆','森林狼']
for a,b in enumerate(team):
    if a%2==0:
        print(b,end='\t')
    else:
        print(b)
