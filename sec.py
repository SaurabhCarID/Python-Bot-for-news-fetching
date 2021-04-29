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
#driver=webdriverdata.driver.Chrome(path)
#driverdata.driver.maximize_window()
def sec():
        try:
                today=datetime.datetime.today()
                if len(str(today.day))!=2:
                        day=str("0")+str(today.day)
                else:
                    day=str(today.day)

                if len(str(today.month))!=2:
                        month=str("0")+str(today.month)
                else:
                    month=str(today.month)
                today_date=month+' '+day+' '+str(today.year)


                news_data=open("fetched_news.csv",'a')
                date=pd.read_csv("date.csv")
                todays=date.iloc[3]['Date'].split('-')
                todays_no=0
                for ele in range(0, len(todays)):
                    todays_no = todays_no + int(todays[ele])
                 


                driverdata.driver.get("https://www.sec.gov/news/pressreleases?aId=&combine=&year={}&month={}".format(today.year,month))
                time.sleep(2)
                table=driverdata.driver.find_element_by_id("DataTables_Table_0_wrapper")
                row=table.find_elements_by_class_name("pr-list-page-row")
                count=0
                for r in row:
                    releas=r.find_elements_by_class_name("views-field")[2].text
                    if count==0:
                            date.at[3,'Date']=releas
                            count+=1
                    release=releas.split('-')
                    release_no=0
                    for ele in range(0, len(release)):
                        release_no = release_no + int(release[ele])
                    if release_no>todays_no:
                        dates=r.find_elements_by_class_name("views-field")[0].text.replace(",",'')
                        news_data.write(dates+",")
                        #print(dates)
                        head=r.find_elements_by_class_name("views-field")[1]
                        
                        heading=head.text.replace(",",'')
                        #print(heading)
                        news_data.write("www.sec.gov"+",")
                        news_data.write(heading+",")
                        link=head.find_element_by_tag_name('a').get_attribute("href")
                        #print(link)
                        news_data.write(link+",")
                        news_data.write("Null"+"\n")


                date.to_csv('date.csv',index=False)
                news_data.close()
        except:
                pass
                

#driverdata.driver.quit()
