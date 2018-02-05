# -*- coding: utf-8 -*-
from urllib import request
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import urllib.parse
import json
import re
header={    #请求头部
        'User-Agent':'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
}

datas = {
    'params':	'MWrspkevnmcL5u1Bs75bF9odB/ix2bnXE13xgcZzoP+GLPXeyJ+Cx0aBS+R2aP+C2Ca2pjJ4TCoHcdtZm1K8kFPkQ2aW7L9Q430ni5L8RFMugVKt4AlotubysT+/5CfaY6113edxA9iguduW1kwU0ZakDAWS9tO1qZvz4lQHZ2hQCL3bXZmSOnH35k3ZhLpx',
    'encSecKey': '19c38fd01f8e6dd6ad1c5e3fd196e24ad85c90510707acbfce217c620883dc22edbbf487a53c2b752e0a2c1b34149ef7d40c99ec3447116e4e6bbae1f3d38c1f3e12df7dfcdf3e834d6b74230a235baba43e8f65c45f1e1fe716799a0de46c6e714312063cb3859aaca6243238970ec555b68b440c9d3d39a0d69deecae08ddd'
}

def getList(burl):    # 获取榜单歌曲的名字和id
    hrefList = []
    nameList = []
    req = request.Request(url = burl, headers = header)
    html = request.urlopen(req).read().decode('utf-8')
    html = str(html)
    bsObj = BeautifulSoup(html,"lxml")
    for tr in bsObj.findAll("a",{"href":re.compile("/song\?id=[0-9]*$")}):
       hrefList.append(tr['href'])
       nameList.append(tr.text)
    return hrefList,nameList

def getSong(hrefList,nameList):   # 获取热评信息
    index = 0
    for href in hrefList:
        id = href[9:]
        url = 'http://music.163.com/weapi/v1/resource/comments/R_SO_4_%s?csrf_token=' % id
        postdata=urllib.parse.urlencode(datas).encode('utf8')
        req = request.Request(url = url, headers = header,data = postdata)
        res = request.urlopen(req).read().decode('utf-8')
        json_dict=json.loads(res)      # 获取json对象
        comment=json_dict['hotComments']
        print(index + 1,".《",nameList[index],"》: ")
        iindex = 1
        for  c in comment:
            print(iindex,":",c['content'])
            iindex = iindex + 1
        index = index + 1
        

href,name = getList("http://music.163.com/discover/toplist?id=60198")
getSong(href,name)
