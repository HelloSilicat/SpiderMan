from urllib import request
from bs4 import BeautifulSoup

header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '  
                                           'AppleWebKit/537.36 (KHTML, like Gecko) '  
                                               'Ubuntu Chromium/44.0.2403.89 '  
                                               'Chrome/44.0.2403.89 '  
                                               'Safari/537.36'}  
def getIP(baseUrl,page):    # 现在提供代理ip的网站上简单爬取可用的ip
    IP = []
    for i in range(1,page + 1):
        url = baseUrl + str(i)
        req = request.Request(url=url, headers=header)  
        r = request.urlopen(req)  
        bsObj = BeautifulSoup(r,"lxml",from_encoding='utf-8').find("table",{"id":"ip_list"})
        tr = bsObj.findAll("tr")[1:]
        for t in tr:
            td = t.findAll("td")
            IP.append("{0}:{1}".format(td[1].text, td[2].text))
    return IP

def test(proxy):   # 这里提供了一个检测代理ip的过程，稍加修改便可用于其他爬虫程序的使用
    print(proxy)
    header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '
                                           'AppleWebKit/537.36 (KHTML, like Gecko) '
                                           'Ubuntu Chromium/44.0.2403.89 '
                                           'Chrome/44.0.2403.89 '
                                           'Safari/537.36'}
    try:
        proxy_handler = request.ProxyHandler({'http': proxy})
        opener = request.build_opener(proxy_handler)
        request.install_opener(opener)
        req = request.Request(url="https://www.baidu.com/", headers=header)
        request.urlopen(req)
    except Exception as e:
        print ("failed")
    else:
        print ("successful")
    return None

IP = getIP("http://www.xicidaili.com/nt/",1)
for i in range(1,5):
    test(IP[i])


