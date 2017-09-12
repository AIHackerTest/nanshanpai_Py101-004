from sys import exit

def xian():
    print("欢迎你来到古城西安")
    while True:
        print("你想去哪一个景点旅行，兵马俑，法门寺,钟鼓楼")
        jingdian = input("景点>")
        print("你觉得 %r 景点的名票价格大概是多少" % jingdian)
        jiage = input("门票>")
        if jingdian == "兵马俑" and jiage >= '150':
            print("OK 开始你的 %r 之旅吧！" % jingdian)
        elif jingdian == "钟鼓楼" and jiage >= '50':
            print("ok 开始你的 %r 之旅吧！" % jingdian)
        elif jingdian == "法门寺" and jiage >= '100':
            print("ok 开始你的 %r 法门寺之旅吧！" % jingdian)
        else:
            print("请重新输入选择景点和金额")
            print("你可以换一个城市看看")
            print("谢谢 你下次再见")
            vistcity()
    
def beijing():
    print("欢迎你来到首都北京旅行")
    jingdian = ['故宫', '长城', '圆明园']
    jing_dian = input("请选择你的景点")
    if jing_dian in jingdian:
        print(" %r 是一个著名的景点。。。。。。." % jing_dian)
    pass

def shanghai():
    pass
    

def vistcity():
    print("你最想去国内的哪一个城市旅行，西安，北京，上海")
    city = input(">")
    if city == "北京":
        beijing()
    elif city == "上海":
        shanghai()
    elif city == "西安":
        xian()
    else:
        print("你想去一个不同的城市，我们暂时不能提供服务")
        exit(0)
		
		
vistcity()