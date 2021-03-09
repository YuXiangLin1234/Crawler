from selenium import webdriver
import requests, bs4
import time

headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36"
}
path = "./chromedriver_88.exe"
option = webdriver.ChromeOptions()
option.add_argument("headless")
browser = webdriver.Chrome(executable_path=path,options=option)

url = "https://tw.hjwzw.com/"
name = input("What's the name of the novel you want to download? ")
chapter = int(input("What chapter last download(還沒開始下載那章)?"))
m = open(name + "_menu.txt", "r")
pageurl = m.readlines()
m.close()
for i in (pageurl):
    print(i)
f = open(name+".txt","a",encoding="utf-8")
count = 0
for i in pageurl:
    if "Book/Read" not in i:
        continue
    count += 1
    print(url+i)
    if count < chapter:
        continue
    #html = requests.get(url + i,headers=headers)
    #obj = bs4.BeautifulSoup(html.text,"lxml")
    #f.write(obj.find("h1").text)
    # 因為用bs4爬下來的內文是空字串，因此改用selenium
       # article = obj.find_all("p")
    browser.get(url + i)
    f.write(browser.find_element_by_tag_name("h1").text + "\n")
    article = browser.find_elements_by_tag_name("p")
    for j in article:
        f.write("    " + j.text + "\n\n")
f.close()
