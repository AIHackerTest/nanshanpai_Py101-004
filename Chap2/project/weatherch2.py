import requests
from sys import exit

list1 = []
list2 = []

u_rl = "https://api.seniverse.com/v3/weather/now.json?key=kelsy6uu0gufudjz&location=beijing&language=zh-Hans&unit=c"
dailyurl = "https://api.seniverse.com/v3/weather/daily.json?key=kelsy6uu0gufudjz&location=beijing&language=zh-Hans&unit=c&start=0&days=5"
lifeurl = "https://api.seniverse.com/v3/life/suggestion.json?key=kelsy6uu0gufudjz&location=shanghai&language=zh-Hans"

def weathernow(city):
    
    url = "https://api.seniverse.com/v3/weather/now.json?key=kelsy6uu0gufudjz&" + "location=%s&language=zh-Hans&unit=c" % city
    urllife = "https://api.seniverse.com/v3/life/suggestion.json?key=kelsy6uu0gufudjz&location=%s&language=zh-Hans" % city
    try:
        r = requests.get(url)
        r.status_code
        dict2 = r.json()['results']
        citycloud = dict2[0]['now']['text']
        citytem = dict2[0]['now']['temperature']
        cityming = dict2[0]['location']['name']
        citytime = dict2[0]['last_update'].replace('T',' ')[:10]
        list1.append('%s,%s,%s,%s' % (cityming, citycloud, citytem, citytime))
        rlife = requests.get(urllife)
        dict3 = rlife.json()['results']
        citysport = dict3[0]['suggestion']['sport']['brief']
        citydress = dict3[0]['suggestion']['dressing']['brief']
        citylife = dict3[0]['location']['name']
    
        list2.append('%s,%s,%s' % (citylife,citydress,citysport))

        print("你查询的城市:%s 天气状况: %s 温度%s摄氏度" % (city, citycloud, citytem))
        print("-------------------------------------------")
        print("更新时间是: %s" % citytime)
        print("-------------------------------------------")
        print("你查询的城市:%s 生活指数: 穿衣 %s 运动 %s" % (citylife, citydress, citysport))
    except KeyError:
         print("没有你要查询的城市")    
    
        
def h_istory():
            
    for i in list1:
         a,b,c,d = i.split(',')
         print("你查询的历史城市: %s 天气状况: %s 温度: %s摄氏度 更新时间是: %s" %(a, b, c, d))
    for i in list2:
         x,y,z = i.split(',')
         print("你查询历史城市: %s   穿衣指数: %s 运动指数: %s" % (x,y,z))
         
def h_elp():
    print("""
    输入城市名,查询该城市的天气
    输入 help,获得帮助文档
    输入history,获得查询历史
    输入 quit,退出天气查询系统
""")
def _main_():
    print("程序使用数据来自心知天气")
    while True:
        city = input('请输入你要查询的城市名称:')

        if city == 'quit':
             exit(0)
        elif city == 'help':
            h_elp()
        elif city == 'history':
            h_istory()
        else:
            weathernow(city)
            
_main_()
