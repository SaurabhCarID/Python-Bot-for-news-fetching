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
def occ():
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
        today_date=month+'/'+day+'/'+str(today.year)
        news_data=open("fetched_news.csv",'a')
        #token_data.write('Name'+','+'Price'+','+'Volume'+','+'Date and Time'+'\n')

        #driver=webdriverdata.driver.Chrome(path)
        #driverdata.driver.maximize_window()

        driverdata.driver.get("https://www.occ.gov/news-events/newsroom/index.html")
        time.sleep(2)
        date_filter=driverdata.driver.find_element_by_id("daterange")
        webdriver.ActionChains(driverdata.driver).move_to_element(date_filter )
        date_filter=Select(driverdata.driver.find_element_by_id("daterange"))
        date_filter.select_by_visible_text('Select a date range')
        time.sleep(1)
        driverdata.driver.find_element_by_id("dateFrom").send_keys(dates.iloc[1]['Date'].replace("-","/"))
        driverdata.driver.find_element_by_id("dateTo").send_keys(today_date)
        driverdata.driver.find_element_by_class_name("fltrapplybtn2").click()

        main=WebDriverWait(driverdata.driver,20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "newsresults"))
            )
        time.sleep(3)
        news=main.find_elements_by_tag_name("li")
        for i in range(0,len(news)+1):
            try:
                title=news[i].find_element_by_class_name("title")
            except:
                #print("No news updated on Occ website")    
                continue
            date=news[i].find_element_by_class_name("floatrt.floatlt").text
            url=title.find_element_by_tag_name('a')
            news_data.write(date.replace(",","")+",")
            news_data.write("www.occ.gov"+",")
            news_data.write(title.text.replace(",","")+",")
            news_data.write(url.get_attribute("href")+",")
            news_data.write("Null"+"\n")
            #print(title.text,url.get_attribute("href"),date)

        dates.at[1,'Date']=today_date
        dates.to_csv('date.csv',index=False)
        news_data.close()
        #driverdata.driver.quit()

