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
html = requests.get(url+"List/"+name)
obj = bs4.BeautifulSoup(html.text,"lxml")
menuurl = ""
try:
    otherpattern = obj.find("span", class_="wd10")
    if otherpattern != None:
        book = otherpattern.find("a")
    if book.text == name:
        html = requests.get(url + book["href"])
        obj = bs4.BeautifulSoup(html.text, "lxml")
    print("ok")    

    menu = obj.find_all("a")
    for i in menu:
        TITLE = i.get("title")
        HREF = i.get("href")
        print(TITLE)
        print(type(TITLE))
        print(HREF)
        print(type(HREF))
        print("====")    
        if type(TITLE) == None or type(HREF) == None:
            continue
        if ("小說名:" + name ) in str(TITLE) and "Book/Chapter" in str(HREF):
            menuurl = url + str(HREF)
            break
except:
    print("There are some books are not designed template on website\n ")
    menuurl  =input("Please enter the menuurl directly: ")

print("menuurl: " , menuurl)
html = requests.get(menuurl)
html.raise_for_status()
obj = bs4.BeautifulSoup(html.text,"lxml")
#pages = obj.find_all("td")
#pageurl = pages.find_all("a")
pageurl = obj.select("td a")
f = open(name+"_menu.txt","w",encoding="utf-8")
for i in (pageurl):
    f.writelines( i["href"] + "\n")
f.close()
