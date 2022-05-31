#Program scrapes Duunitori for set keywords and returns "the best job for you" :p
#ie. the job which description has the most "keyStrings"

import re
from bs4 import BeautifulSoup as bs
import requests
import functools as ft
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import csv


#timer for run time
start_time = time.time()

#Run with Firefox
""" from webdriver_manager.firefox import GeckoDriverManager
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install()) """

#Run with Chrome
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())


def Main():
    #set how many pages are gone through | Each page has 20 jobs -> runCount*20 = jobs scraped
    runCount = 2
    k = 0
    totaltotalCount = 0
    prevTotalCount = 0
    mostKeywords = []

    #KEYWORDS TO FIND
    persistentSearchCount = {"python": 0, "php": 0, "c#": 0, "sql": 0, " rust": 0}
    keyString = persistentSearchCount.keys()
    #Found numbers
    salaries = []

    searchCount = {}
    totalCount = 0
    

    while k  <= runCount:
            
        html_text = requests.get('https://duunitori.fi/tyopaikat?haku=Tieto-%20ja%20tietoliikennetekniikka%20(ala)&order_by=date_posted&sivu=' + str(k)).text
        soppa = bs(html_text, 'html.parser')

        jobs = soppa.find_all('a', class_="job-box__hover gtm-search-result")

        for link in jobs:
            urlJob = link.get('href')
            print('https://duunitori.fi' + urlJob)
            driver.get('https://duunitori.fi' + urlJob)
            driver.implicitly_wait(0.5)
            jobPost = driver.find_element(By.CLASS_NAME, 'description-box').text.lower()

            repls = ('\n', ''), ('<br>', '')
            jobPost = ft.reduce(lambda a, kv: a.replace(*kv), repls, jobPost)

            #print(jobPost)
            for key in keyString:
                searchCount[key] = jobPost.count(key)
                persistentSearchCount[key] += searchCount[key]
            
            #if all in searchCount empty skip
            if any(searchCount.values()) :
                #basic salary finder
                if "palkka" in keyString:
                    if(searchCount["palkka"] > 0):
                        salaries = re.findall('[0-9]+', jobPost)
                        #sort out least likely salary numbers
                        salaries = list(filter(lambda a: 3 < len(a) < 6, salaries))

                print("Possible salaries-> " + str(salaries))
                print("KEYWORDS: ")
                print(searchCount)

                for count in searchCount.values():
                    totalCount += count
                print("TOTAL COUNT = " + str(totalCount))

                totaltotalCount += totalCount
                print("___________END____________")

                if totalCount >= prevTotalCount:
                    jobLink = 'https://duunitori.fi' + urlJob
                    if totalCount == prevTotalCount:
                        list(mostKeywords).append(jobLink)
                    else:
                        mostKeywords = jobLink
                        prevTotalCount = totalCount

            #empty for next job
            totalCount = 0
            salaries.clear()
            searchCount.clear()
            
        k += 1

    driver.quit()
    print("_____BEST job for you :)____ \n" + str(mostKeywords) + "\n________________________")
    print("OVERALL COUNT = " + str(totaltotalCount))
    print("Process finished --- %s seconds ---" % (time.time() - start_time))

    AddToCSV(persistentSearchCount, keyString)

def AddToCSV(data: dict, keyString: dict):
    with open("democsv.csv", "a") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = keyString)
        writer.writeheader()
        writer.writerows([data]) 
    print(data)

Main()
