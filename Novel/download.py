from selenium import webdriver
import requests, bs4
import time

headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36"
}
path = "./chromedriver_88.exe"
h = {
    'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml, */*',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
}
option = webdriver.ChromeOptions()

option.add_argument("headless")
browser = webdriver.Chrome(executable_path=path,options=option)

name = input("What's the name of the novel you want to download? ")
chapter = int(input("What chapter last download(還沒開始下載那章)?"))
m = open("_menu.txt", "r")
pageurl = m.readlines()
m.close()
for i in (pageurl):
    print(i)
f = open(name+".txt","a",encoding="utf-8")
count = 0
for i in pageurl:
    count += 1
    if count < chapter:
        continue
    # 因為用bs4爬下來的內文是空字串，因此改用selenium
    #if count >=2:
    #    break
    browser.get(i)
    f.writelines(browser.find_element_by_id("content").text + "\n\n\n\n\n")
f.close()
