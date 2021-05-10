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
def bafin():
    try:

        news_data=open("fetched_news.csv",'a')
        date=pd.read_csv("date.csv")
         


        driverdata.driver.get("https://www.bafin.de/EN/PublikationenDaten/Aktuelles/aktuelles_node_en.html")
        WebDriverWait(driverdata.driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, "c-banner__button.js-close-banner"))).click()
        time.sleep(2)
        table=driverdata.driver.find_element_by_class_name("textualData.links")
        row=table.find_elements_by_tag_name("tr")

        count=0
        pre_date=date.iloc[5]['Date'].split('.')
        for r in row[1:]:
            dates=r.find_elements_by_tag_name("td")[0]
            cur_date=dates.text.split(".")
            
            if datetime.datetime(int(cur_date[2]),int(cur_date[1]),int(cur_date[0]))>datetime.datetime(int(pre_date[2]),int(pre_date[1]),int(pre_date[0])):
                dat=r.find_elements_by_tag_name("td")[1]
                data=dat.text.replace("­","")
                data=data.replace(",",";")
                link=dat.find_element_by_tag_name('a').get_attribute("href")
                #print(dates.text,data)
                #print(link)
                
                if count==0:
                        date.at[5,'Date']=dates.text
                        count+=1
                news_data.write(cur_date[0]+"."+cur_date[1]+"."+cur_date[2]+",")
                news_data.write("https://www.bafin.de"+",")
                data=data.replace(",","")
                data=data.replace("'", "'")
                data=data.replace('’', "'")
                data=data.replace(u'—', '-')
                data=data.replace('–', '-')
                data=data.replace('â€', "'")
                data=data.replace(u'Â', u"")
                data=data.replace('Â', "")
                data=data.replace('“', '"')
                data=data.replace('”', '"')
                data=data.replace('â\x80\x94', '-')
                data=data.replace("â\x80\x99","")
                data=data.replace("â\x80\x9cA ",'"')
                data=data.replace("â\x80\x9d",'"')
                data=data.replace("â\x80\x9c",'"')
                data=data.replace("\xa0",'')
                data=data.replace("´","'")
                news_data.write(data+",")
                news_data.write(link+",")
                news_data.write("Null"+"\n")



        news_data.close()
        date.to_csv('date.csv',index=False)
    except:
        pass
            
                    

#driverdata.driver.quit()
