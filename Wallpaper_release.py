from selenium import webdriver
import requests
import time
import os

driver = "./chromedriver.exe"
validcategory = False
nobrowser = webdriver.ChromeOptions()
nobrowser.add_argument("headless")
browser = webdriver.Chrome(executable_path=driver)

while validcategory == False:
    category = input("What category do you want to download? ")
    url = "https://wallpapercrafter.com/xfsearch/alt/" + category + "/"
    browser.get(url)
    browser.implicitly_wait(5)
    print("====")
    pages = (browser.find_elements_by_class_name("navigation"))
    
    try:
        if "Ooops, Something Goes Wrong" in browser.find_element_by_tag_name("h2").text:     
            print("Sorry, there is no such a category in this website.")
            print("Please choose another category.")
            continue
    except:
        pass
    try:
        page = pages[0].text.split(" ")
    except:
        page = [1]
    validcategory = True
Dir = category.title()
if os.path.exists(Dir) == False:
    os.mkdir(Dir)
for i in range(1, int(page[-1]) + 1):
    url = "https://wallpapercrafter.com/xfsearch/alt/" + category + "/page/" + str(i)
    browser.get(url)
    print("loading....")
    time.sleep(0.2)
    print("finish!")
    imgs = browser.find_elements_by_tag_name('img')        
    num = 0
    for img in imgs:
        if num == 0:
            num += 1
            continue
        imgurl = img.get_attribute("src")
        print(imgurl)
        print("Downloading...")
        photo = requests.get(imgurl)
        photopath = "./" + Dir + "/" + imgurl[37:]
        if os.path.isfile(photopath) == False:
            with open(os.path.join(Dir,os.path.basename(imgurl)),"wb" ) as file:
                for disk in photo.iter_content(10240):
                    file.write(disk)
            print("Finish!!")
        else:
            print("The photo have existed.")
print("All work are finished.")
