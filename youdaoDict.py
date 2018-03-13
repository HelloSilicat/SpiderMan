from urllib import request
from bs4 import BeautifulSoup
from urllib.error import HTTPError
import requests

root_url = "http://dict.youdao.com/w/eng/"
voc = input("What is your vocabulary?\n>").strip().replace(" ","_")
url = root_url + voc



# get the whole page of the voc
flag = False
while (not flag):
    try:
        flag = True
        soup = BeautifulSoup(request.urlopen(url),"lxml")
    except HTTPError as e:
        print("This vocabulary is missing! Why not change another one?")
        voc = input("What is your vocabulary?\n>").strip().replace(" ","_")
        flag = False

# get the definition of the voc
flag = False
while (not flag):
    try:
        flag = True
        trans_container = soup.find("div",{"class":"trans-container"})
    except HTTPError as e:
        print("ERROR: trans_container is not found!")
        flag = False
Definition = str(trans_container.find("ul").text).replace("\n","  ")

# get the example of the voc
flag = False
while (not flag):
    try:
        flag = True
        examplesToggle = soup.find("div",{"id":"examplesToggle"})
    except HTTPError as e:
        print("ERROR: examplesToggle is not found!")
        flag = False
temp = examplesToggle.find("li").findAll("p")
Example = (str(temp[0].text) + str(temp[1].text)).replace("\n"," ")


print("Definition: ", Definition)
print("Example: ", Example)




