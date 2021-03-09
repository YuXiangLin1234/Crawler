from selenium import webdriver
import requests, bs4
import time

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
    menu = obj.find_all("a")
    for i in menu:
        if ("小說名:" + name ) in str(i.get("title")) and "Book/Chapter" in str(i.get("href")):
            menuurl = url + str(i.get("href"))
            break
    html = requests.get(menuurl)
    html.raise_for_status()
    obj = bs4.BeautifulSoup(html.text,"lxml")
    pageurl = obj.select("td a")
    for i in (pageurl):
        print(i["href"])
    f = open(name+".txt","w",encoding="utf-8")
    for i in pageurl:
        if "Book/Read" not in i["href"]:
            continue
        print(url+i["href"])
        obj = bs4.BeautifulSoup(html.text,"lxml")
        browser.get(url + i["href"])
        f.write(browser.find_element_by_tag_name("h1").text)
        article = browser.find_elements_by_tag_name("p")
        for j in article:
            f.write(j.text + "\n\n")
    f.close()
except:
    print("There is no book named it on the website, please change your goal or confirm the name")
