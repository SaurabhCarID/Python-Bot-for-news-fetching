import time
import driverdata
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium_ai import ElementFinder
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import datetime


#path="chromedriverdata.driver.exe"
def sebi():

    today=datetime.datetime.today()
    if len(str(today.day))!=2:
            day=str("0")+str(today.day)
    else:
        day=str(today.day)

    if len(str(today.month))!=2:
            month=str("0")+str(today.month)
    else:
        month=str(today.month)
    today_date=day+'-'+month+'-'+str(today.year)

    news_data=open("fetched_news.csv",'a')
    date=pd.read_csv("date.csv")
    #token_data.write('Name'+','+'Price'+','+'Volume'+','+'Date and Time'+'\n')

    #driver=webdriverdata.driver.Chrome(path)
    #driverdata.driver.maximize_window()

    driverdata.driver.get("https://www.sebi.gov.in/sebiweb/home/HomeAction.do?doListing=yes&sid=6&ssid=23&smid=0")
    time.sleep(2)
    dates=driverdata.driver.find_element_by_id("2")
    dates.find_element_by_id("fromDate").send_keys(date.iloc[2]['Date'])
    dates.find_element_by_id("toDate").send_keys(today_date)
    time.sleep(1)
    driverdata.driver.find_element_by_class_name("go-search.go_search").click()
    time.sleep(2)
    try:
        table=driverdata.driver.find_element_by_id("sample_1")
        news=table.find_elements_by_class_name("odd")

        for n in news:
            date_release=n.find_elements_by_tag_name('td')[0]
            #print(date_release.text)
            news_f=n.find_elements_by_tag_name('td')[1]
            link=news_f.find_element_by_tag_name('a')
            link=link.get_attribute("href")
            news_data.write(date_release.text.replace(",","")+",")
            news_data.write("www.sebi.gov.in/"+",")
            news_data.write(news_f.text.replace(",","")+",")
            news_data.write(link+",")
            news_data.write("Null"+"\n")

    except:
        print("No new news is updated on Sec website")



    date.at[2,'Date']=today_date
    date.to_csv('date.csv',index=False)
    news_data.close()
#driverdata.driver.quit()
  
