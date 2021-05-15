import time
import driverdata
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium_ai import ElementFinder
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import pandas as pd
import datetime


#path="chromedriverdata.driver.exe"

def mas():

        news_data=open("fetched_news.csv",'a')
        dates=pd.read_csv("date.csv")
        today=datetime.datetime.today()
        if len(str(today.day))!=2:
                day=str("0")+str(today.day)
        else:
            day=str(today.day)

        if len(str(today.month))!=2:
                month=str("0")+str(today.month)
        else:
            month=str(today.month)
        today_date=str(today.year)+'-'+month+'-'+day

        #token_data.write('Name'+','+'Price'+','+'Volume'+','+'Date and Time'+'\n')

        #driver=webdriverdata.driver.Chrome(path)
        #driverdata.driver.maximize_window()

        driverdata.driver.get("https://www.mas.gov.sg/news?date={}T18%3A30%3A00.000Z%2C{}T23%3A59%3A59.000Z&page=1&rows=20".format(dates.iloc[6]['Date'],today_date))
        time.sleep(2)

        main=WebDriverWait(driverdata.driver,20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "mas-search-page__results-list"))
            )
        time.sleep(3)
        news=main.find_elements_by_tag_name("li")
        for i in range(0,len(news)+1):
            try:
                title=news[i].find_element_by_class_name("ola-field-title")
            except:
                #print("No news updated on Occ website")    
                continue
            date=news[i].find_element_by_class_name("mas-search-card__header").text.split(":")[1][1:]
            url=title.find_element_by_tag_name('a')
            
            news_data.write(date+",")
            news_data.write("www.mas.gov.sg/"+",")
            news_data.write(title.text.replace(",","")+",")
            news_data.write(url.get_attribute("href")+",")
            news_data.write("Null"+"\n")
            
            #print(title.text,url.get_attribute("href"),date)

        dates.at[6,'Date']=today_date
        dates.to_csv('date.csv',index=False)
        news_data.close()
        #driverdata.driver.quit()

