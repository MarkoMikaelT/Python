#Program scrapes Duunitori for set keywords and returns "the best job for you" :p
#ie. the job which description has the most "keyStrings"
#creates or updates "democsv.csv" file on end  

from datetime import datetime
from bs4 import BeautifulSoup as bs
import requests
import functools as ft
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import csv

import json
from pymongo import MongoClient

#timer for run time
start_time = time.time()

#Run with Firefox
""" from webdriver_manager.firefox import GeckoDriverManager
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install()) """

#Run with Chrome
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())

credPath = "./noExport/cred.json"

def Main():
    #set how many pages are gone through | Each page has 20 jobs -> (1 + runCount)*20 = jobs scraped
    runCount = 9
    k = 0
    pageCount = 0

    #KEYWORDS TO FIND
    persistentSearchCount = {"python": 0, "javascript": 0, "java": 0,
                            "c++": 0, "sql": 0, "flutter": 0, "kotlin": 0,
                            "php": 0, "c#": 0, "html": 0, "css": 0,
                            "typescript": 0, "rust": 0, "swift": 0, "nosql": 0}
    keyString = persistentSearchCount.keys()

    searchCount = {}

    while k  <= runCount:

        html_text = requests.get('https://duunitori.fi/tyopaikat?haku=Tieto-%20ja%20tietoliikennetekniikka%20(ala)&order_by=date_posted&sivu=' + str(k)).text
        soppa = bs(html_text, 'html.parser')

        jobs = soppa.find_all('a', class_="job-box__hover gtm-search-result")

        for link in jobs:
            urlJob = link.get('href')
            print('https://duunitori.fi' + urlJob)
            driver.get('https://duunitori.fi' + urlJob)
            driver.implicitly_wait(1)
            jobPost = driver.find_element(By.CLASS_NAME, 'description-box').text.lower()

            repls = ('\n', ''), ('<br>', '')
            jobPost = ft.reduce(lambda a, kv: a.replace(*kv), repls, jobPost)

            #print(jobPost)
            for key in keyString:
                searchCount[key] = jobPost.count(key)
                persistentSearchCount[key] += searchCount[key]
            
            searchCount.clear()
            pageCount += 1
            
        k += 1

    print(persistentSearchCount)
    driver.quit()
    print("Process finished --- %s seconds ---" % (time.time() - start_time))

    AddToCSV(persistentSearchCount, keyString, pageCount)
    ExportToMongo(persistentSearchCount)

def AddToCSV(data: dict, keyString: dict, pages):
    data.update({"checkedPages": pages})
    data.update({"runTime": datetime.today().strftime("%d/%m/%Y|%H:%M:%S")})
    with open("democsv.csv", "a") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = keyString)
        writer.writeheader()
        writer.writerows([data]) 
    print(data)

def ExportToMongo(data: dict):
    file = open(credPath)
    creds = json.load(file)

    clusterConn = f"mongodb+srv://{creds['name']}:{creds['pass']}@scrapecluster.bvokbsk.mongodb.net/ScrapedData?retryWrites=true&w=majority"
    client = MongoClient(clusterConn)
    db = client.ScrapedData.Scrape1

    db.insert_one(data)

Main()
