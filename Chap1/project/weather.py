from sys import exit
import os
import time



d = {}
newl = []
filepath = os.path.join(os.getcwd(), 'weather_info.txt')
filename = open(filepath, 'r') 

for fileline in filename:
       
    x,y = fileline.strip().split(',')
    d[x] = y
    
        
print("欢迎查询城市天气，请输入你要查询的城市")
while True:
    
    city = input(">")
        
    newl.append(city)
            
    if city in d:
       time_today = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
       print("今天是 %r" % time_today)
       print("你查询的城市%s天气状况: %s" % (city,d[city]))
    elif city == 'history':
        print("你查询的历史记录:")
        for in_city in newl:
            if in_city in d:
            
                print("城市: %s  天气: %s" % (in_city,d[in_city]))
    elif city == 'quit':
	
        exit(0)	
    elif city == 'help':
        print("查询天气请输入城市名称")
        print("查询历史记录请输入history")
        print("输入help看帮助文件")
        print("退出请输入quit")
    else:
        print("没有查询到你输入的城市,请重新输入")