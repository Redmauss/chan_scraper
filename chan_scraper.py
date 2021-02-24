from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import urllib.request
import os
import datetime
process = "on"
while process == "on":
    driver = webdriver.Firefox()
    board = input("Which board do you want to search? ")
    if len(board) < 4:
        board = board.lower()
        driver.get("https://boards.4chan.org/{}/archive".format(board))
    else:
        print("Board can't be longer than 3 characters!")
        board = input("Which board do you want to search? Make to sure to use less than 4 characters ")
    matching_threads = []
    key = input("What do you want to search for? ")
    def threadSearcher():
        for i in driver.find_elements_by_class_name("teaser-col"):
            if key in i.text:
                matching_threads.append(i.text)
                confirm = input("Thread found with title of " + i.text + " do you want to download? Type yes or no ")
                if confirm == "yes":
                    threadSearcher.folderName = i.text
                    locationt = i.find_element_by_xpath(".//following::td/a")
                    locationt.click()
                    return
                elif confirm == "no":
                    continue
                
            elif key == "q":
                driver.quit()
                quit() 
            else:
                print("Searching...")

    threadSearcher()  

    folderName = threadSearcher.folderName.replace(" ","_")
    folderName = folderName.replace("/","")
    folderName = folderName.replace(":","")
    folderName = folderName.replace("?","")
    imagehrefs = []
    for i in driver.find_elements_by_class_name("fileThumb"):
        imagehrefs.append(i.get_attribute("href"))
    print(imagehrefs)
    c = 0
    name = input("What do you want to name the files? ")
    date = datetime.datetime.now()
    date = str(date).replace(" ","")
    date = date.replace(":","_")
    filelocation = input("Where do you want to save the files? Insert full path! ")
    filepath = "{location}{folder}{date}/".format(location = filelocation, folder = folderName, date = date)
    os.mkdir(filepath)
    print(filepath)
    for i in imagehrefs:
        if i[-1] == "m":
            fileType = i[-4:]
        else:
            fileType = i[-3:]
        print("File #" + str(c) + " downloaded with file type " + fileType)
        c += 1
        num = imagehrefs.index(i)
        try:
            urllib.request.urlretrieve(i,"{path}{filename}{count}.{file}".format(count = num,file = fileType, filename = name, path = filepath))
            continue
        except:
            continue
    process = input("Do you want to download another thread? ")

driver.quit()
