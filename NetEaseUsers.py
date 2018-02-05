from urllib import request
from bs4 import BeautifulSoup
import re
import requests
import json
import urllib.parse

header={    
        'User-Agent':'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}
datas = {
    'uid': '107948356',
    'type': '0',
    'params': 'omVn+M+0MLjIZemA9918G3f5KdkNonc9V858JCrRutQEUSoFW9d5+RjfEooWwEkm4L0FduF4tveH9frjgEPfBVcIKeMI+CMJQr9F9Rj/J370mfSjFzTH3M8R8EUUO1JmECbzdtXEaDQ9LJILWDBR8FE9zINdgO2F4FF8YYwclm35Og06qR7SXleDG0ZInf3MUWotx/i/7JodxnfsS9nzrw==',
    'encSecKey': '5eea474d42a3dbaa409d73a1fa71594616c770cc0e38f701f233c410001d604ef868df63441359098d9055ba8abf16e8a1523c3ac56023c1c4a43f9282a8fa5902b60fc3224605304586571a64fea107b1392a75595cfdbbae461427b449a14b91a5d932aad5c8269eb7aecead13d2aa6980630e48929b47a3a40962694443bb'
}

def getUserInfo(id):
    user = {}
    url = "http://music.163.com/user/home?id=" + id
    req = request.Request(url = url, headers = header)
    html = str(request.urlopen(req).read().decode('utf-8'))
    soup = BeautifulSoup(html,"lxml")
    user["name"] = soup.find("h2",{"id":"j-name-wrap"}).find("span").text  # 获取昵称
    user["level"] = soup.find("span",{"class":"lev u-lev u-icn2 u-icn2-lev"}).text  # 获取等级
    if soup.find("h2",{"id":"j-name-wrap"}).findAll("i")[1]["class"][-1][-1] == '1':   # 获取性别
        user["sex"] = "boy"
    else:
        user["sex"] = "girl"

    url = 'http://music.163.com/weapi/user/getfollows/%s?csrf_token=' % id   # post方式获取关注列表
    response = requests.post(url, headers=header, data=datas).content
    json_text= json.loads(response.decode("utf-8"))
    follows = json_text['follow']
    #print(json_text)
    IDs = []
    for ID in follows:
        #print(ID)
        IDs.append({'ID':ID['userId'],'name':ID['nickname']})
    user['follow'] = IDs
    print("Name: ",user['name'])
    print('Sex:' ,user['sex'])
    print("Level:" ,user['level'])
    print("He/She follows:")
    for ID in user['follow']:
        print(ID['name']," ",ID['ID'])

getUserInfo("136702185")
