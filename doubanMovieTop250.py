from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import time

def getInfo(pageUrl,order):
    global Info
    try:
        bs = BeautifulSoup(urlopen(pageUrl))
    except HTTPError as e:
        print(order,":","Movie Not Found")    # 有些电影页面竟然失踪了（电影名可以在top250页面获取）
        return 
    try:    
        Info[order]["Director"] = bs.find("div",{"id":"info"}).find("span").text   
        Info[order]["RatingNumber"] = bs.find("strong",{"class":"ll rating_num"}).text  # 这里只拿了导演和评分两个信息，其余的可以类推
    except AttributeError as e:
        print(order,"Something Wrong!")
        return
    print(order,":",Info[order]["Name"]," ",Info[order]["Director"],"评分:", Info[order]["RatingNumber"])
    
Info = [{}] * 251
order = 1
baseUrl = "https://movie.douban.com/top250?start=0"
for i in range(0,10):
    pageUrl = baseUrl + str(i * 25)    #观察一下发现，不同页只需要修改baseUrl中的start属性，25是第二页，以此类推
    bsObj = BeautifulSoup(urlopen(pageUrl))
    for movie in bsObj.findAll("div",{"class":"hd"}):
        Info[order]["Name"] = movie.find("span").text
        getInfo(movie.find("a")["href"],order)
        order = order + 1
        time.sleep(3)   # 防止封ip





