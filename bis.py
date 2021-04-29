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
#driver=webdriverdata.driver.Chrome(path)
#driverdata.driver.maximize_window()
def bis():
    news_data=open("fetched_news.csv",'a')
    dates=pd.read_csv("date.csv")
    today=dates.iloc[4]['Date'].split(' ')
    news_data=open("fetched_news.csv",'a')


    todaies=datetime.datetime.today()
    todaies.day

    #driver=webdriverdata.driver.Chrome(path)
    #driverdata.driver.maximize_window()

    driverdata.driver.get("https://www.bis.org/press/pressrels.htm")
    time.sleep(2)
    driverdata.driver.find_element_by_id("from_filter_pressrels").click()
    time.sleep(1)
    calender=driverdata.driver.find_element_by_id("ui-datepicker-div")
    month=calender.find_element_by_class_name("ui-datepicker-month")
    selected_from_month = Select(month)
    selected_from_month.select_by_visible_text(today[1])
    day=calender.find_element_by_class_name("ui-datepicker-calendar")
    date=day.find_elements_by_tag_name('a')
    for d in date:
        if d.text==today[0]:
            d.click()
            break

    time.sleep(2)
    try:
        news_block=driverdata.driver.find_element_by_id("pressrels_list")
        news_block=news_block.find_element_by_class_name("documentList")
        news=news_block=news_block.find_elements_by_class_name("item")
        count=0
        for n in news:
                date=n.find_element_by_class_name("item_date").text
                if count==0:
                    dat=date.split()
                    dat[0]=str(todaies.day)
                    a=" "
                    a=a.join(dat)
                    dates.at[4,'Date']=a
                    count+=1
                news_data.write(date.replace(",",'')+",")
                news_data.write("https://www.bis.org/"+",")
                heading=n.find_element_by_class_name("title")
                news_data.write(heading.text.replace(',','')+",")
                link=heading.find_element_by_tag_name('a').get_attribute("href")
                news_data.write(link+",")
                news_data.write("Null"+"\n")
    except:
        print("No new news is updated on bis website")

    dates.to_csv('date.csv',index=False)
    news_data.close()
#driverdata.driver.quit()
