# -*- coding: utf-8 -*-
# coding: utf-8

#import driverdata
import pandas as pd
import requests
from bs4 import BeautifulSoup
import json


#news=pd.read_csv("fetched_news.csv",encoding='cp1252')
news=pd.read_csv("fetched_news.csv")
index=len(news.index)

for i in range(0,index):
#for i in range(31,36):
    if news.at[i,"Description"]=="Null":
        if news.at[i,"Website"]=="www.sebi.gov.in/":
            try:
                r=requests.get(news.at[i,"URL"]).text
                soup = BeautifulSoup(r,features='html.parser',from_encoding="latin-1")
                iframexx = soup.find_all('iframe')
                print(iframexx[0].get_text())
                description=iframexx[0].get_text().replace(",",'')
                description=description.replace(u'—', '-')
                description=description.replace('’', "'")
                description=description.replace("'", "'")
                description=description.replace('â€', "'")
                description=description.replace(u'â€', "'")
                description=description.replace('Â', "")
                description=description.replace(u'Â', u"")
                description=description.replace('â\x80\x94', '-')
                description=description.replace("â\x80\x99","")
                description=description.replace("â\x80\x9cA ",'"')
                description=description.replace("â\x80\x9d",'"')
                description=description.replace("â\x80\x9c",'"')
                description=description.replace("\xa0",'')
                #description=description.encode('cp1252')
                #description=description.decode('utf-8')
                news.at[i,"Description"]=description.encode().decode('utf8')
            except:
                print(news.at[i,"URL"],"Description not available")
                news.at[i,"Description"]="Description not available"
            
        elif news.at[i,"Website"]=="www.occ.gov":
            try:
                r=requests.get(news.at[i,"URL"]).text
                soup = BeautifulSoup(r,from_encoding="cp1252")
                content_area=soup.find(id="main-content")
                content=content_area.find(class_="occ-grid9-12 ctcol issuance-ct")
                first_para=content.find("p").get_text()
                print(first_para.replace(",",""))
                description=first_para.replace(",","")
                description=description.replace(u'—', '-')
                description=description.replace('â€', "'")
                description=description.replace('’', "'")
                description=description.replace("'", "'")
                description=description.replace("â\x80\x99","")
                description=description.replace(u'Â', "")
                description=description.replace('Â', "")
                description=description.replace('â\x80\x94', '-')
                description=description.replace("â\x80\x9cA ",'"')
                description=description.replace("â\x80\x9d",'"')
                description=description.replace("â\x80\x9c",'"')
                description=description.replace("\xa0",'')
                #description=description.encode('cp1252')
                #description=description.decode('utf-8')
                news.at[i,"Description"]=description

            except Exception as e:
                #print(e)
                print(news.at[i,"URL"],"Description not available")
                news.at[i,"Description"]="Description not available"
        elif news.at[i,"Website"]=="www.fincen.gov":
            try:
                r=requests.get(news.at[i,"URL"]).text
                #soup = BeautifulSoup(r, from_encoding="iso-8859-8")
                soup = BeautifulSoup(r, from_encoding="latin-1")
                first_para=soup.find("p").get_text()
                print(first_para.replace(",",""))
                description=first_para.replace(",","")
                description=description.replace("'", "")
                description=description.replace('’', "")
                description=description.replace(u'—', '-')
                description=description.replace('â€', "'")
                description=description.replace(u'Â', u"")
                description=description.replace('Â', "")
                description=description.replace('â\x80\x94', '-')
                description=description.replace("â\x80\x99","")
                description=description.replace("â\x80\x9cA ",'"')
                description=description.replace("â\x80\x9d",'"')
                description=description.replace("â\x80\x9c",'"')
                description=description.replace("\xa0",'')
                #description=description.encode('cp1252')
                #description=description.decode('utf-8')
                news.at[i,"Description"]=description

            except Exception as e:
                #print(e)
                print(news.at[i,'URL'],"Description not available")
                news.at[i,"Description"]="Description not available"
        
        elif news.at[i,"Website"]=="www.sec.gov":
            try:
                r=requests.get(news.at[i,"URL"]).text
                soup = BeautifulSoup(r, from_encoding="cp1252")
                content_area=soup.find(class_ ="article-body").text
                content_area=content_area.split('\n')
                description=content_area[0]+content_area[1]
                description=description.replace(",","")
                description=description.replace("'", "'")
                description=description.replace('’', "'")
                description=description.replace(u'—', '-')
                description=description.replace('–', '-')
                description=description.replace('â€', "'")
                description=description.replace(u'Â', u"")
                description=description.replace('Â', "")
                description=description.replace('“', '"')
                description=description.replace('”', '"')
                description=description.replace('â\x80\x94', '-')
                description=description.replace("â\x80\x99","")
                description=description.replace("â\x80\x9cA ",'"')
                description=description.replace("â\x80\x9d",'"')
                description=description.replace("â\x80\x9c",'"')
                description=description.replace("\xa0",'')
                
                news.at[i,"Description"]=description
            except:
                news.at[i,"Description"]="description not available"
news.to_csv("fetched_news.csv",index=False)
