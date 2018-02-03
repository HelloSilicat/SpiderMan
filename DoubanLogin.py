from urllib import request
from bs4 import BeautifulSoup
import requests

cookie = {}
raw_cookie = '*************'   # 这个代码不能运行，cookie保密了
for line in raw_cookie.split(';'):   #requests.get方法里面需要的cookies是一个dict类型，所以需要一定的转换
    key,value = line.split("=",1)
    cookie[key] = value

r = requests.get("https://www.douban.com/people/69927545/",cookies = cookie)    
bsObj = BeautifulSoup(r.text,"lxml")  # 顺便爬一下用户的签名
print(bsObj.find("span",{"id":"intro_display"}).text)

