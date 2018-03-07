from urllib.request import urlopen
from bs4 import BeautifulSoup
import os
from urllib.error import HTTPError

header={    
        'User-Agent':'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

root_url = "http://www.en8848.com.cn"
def getUrl(url):
    item_url = []
    bsObj = BeautifulSoup(urlopen(url),"lxml").findAll("div",{"class":"yd-book-item yd-book-item-pull-left"})
    for book in bsObj:
        item_url.append([book.find("a")["href"],book.find("a").text.replace("\n",""),book.find("div",{"class":"author-container"}).find("dd").text.replace("\n","")])
    return item_url

def getInfo(url,name,author):
    bsObj = BeautifulSoup(urlopen(url),"lxml").find("div",{"class":"m-volume"})
    c = 0
    if (not os.path.exists(name)):
        os.mkdir(name)
    else:
        print("%s exists already.\n"%(name))
        return
    if (name == "SENSE AND SENSIBILITY" or name == "The Jester"):
        return
    print(name)
    for chap in bsObj.findAll("li"):
        c = c + 1
        link = root_url + chap.find("a")["href"]
        text = BeautifulSoup(urlopen(link),"lxml").find("div",{"class":"m-introbox"}).text
        filename = name+"\\"+name+"_chapter"+str(c)+".txt"
        f = open(filename,"w",encoding="utf-8")
        f.write(text)
        f.close()
        print(name+"_chapter"+str(c)," finished!")
    f = open(name+"\\info.txt","w",encoding="utf-8")
    f.write("Name:%s\nAuthor:%s\n"%(name,author))
    
item_url = getUrl("http://www.en8848.com.cn/fiction/nonfiction/autobiography/")
flag = True
for item in item_url:
    if (flag):
        getInfo(root_url + item[0],item[1].replace(":"," ").strip(),item[2].strip())
    if (item[1].strip() == "The Jester"):
        flag = True

