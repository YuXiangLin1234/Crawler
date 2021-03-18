import requests, bs4
import time
import sys
from selenium import webdriver
header = {
"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
"accept-encoding": "gzip, deflate, br",
"accept-language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7",
"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"
}
path = "./chromedriver_88.exe"
option = webdriver.ChromeOptions()
option.add_argument("headless")
browser = webdriver.Chrome(executable_path=path,options=option)

url = "微風小說網"
menuurl = input("What's the menu url of the novel you want to download? ")
print("menuurl: " , menuurl)
#html = requests.get(menuurl,headers=header)
#html.raise_for_status()
#obj = bs4.BeautifulSoup(html.text,"lxml")
#print(html.text)
#pages = obj.find_all("dd")
#print(pages)
#pageurl = pages.find_all("a")
#pageurl = obj.select("dd a")
browser.get(menuurl)
f = open("_menu.txt","w",encoding="utf-8")
pageurl = browser.find_elements_by_css_selector("dd a")
#print(pageurl)
#print(pageurl[0].get_attribute("href"))
for i in (pageurl):
    f.writelines( i.get_attribute("href") + "\n")
f.close()
