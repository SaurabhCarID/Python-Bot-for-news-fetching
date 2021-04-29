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
def fincen():
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
        news_data=open("fetched_news.csv",'a')
        date=pd.read_csv("date.csv")
        #token_data.write('Name'+','+'Price'+','+'Volume'+','+'Date and Time'+'\n')

        #driver=webdriverdata.driver.Chrome(path)
        #driverdata.driver.maximize_window()

        driverdata.driver.get("https://www.fincen.gov/news-room?field_date_from_date={}&field_date_to_date={}".format(date.iloc[0]['Date'],today_date))
        time.sleep(2)

        try:
                data=driverdata.driver.find_element_by_class_name("views-col")
                datas=data.find_elements_by_class_name("views-row")
                for d in datas:
                        date_release=d.find_element_by_class_name("views-field-field-date-release")
                        title=d.find_element_by_class_name("views-field-title-1")
                        link=title.find_elements_by_tag_name('a')
                        link=link[0].get_attribute("href")
                        #print(date_release.text,title.text,link)
                        news_data.write(date_release.text+",")
                        news_data.write("www.fincen.gov"+",")
                        news_data.write(title.text+",")
                        news_data.write(link+",")
                        news_data.write("Null"+"\n")
        except:
                print("No news update on Fincen website")
                
        date.at[0,'Date']=today_date
        date.to_csv('date.csv',index=False)
        news_data.close()
#driverdata.driver.quit()

