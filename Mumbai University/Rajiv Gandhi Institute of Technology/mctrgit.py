
# coding: utf-8

# In[24]:


import requests
from bs4 import BeautifulSoup
import pandas
r=requests.get("http://www.mctrgit.ac.in/TrainingPlacement.php")
rawsrc=r.content
src=BeautifulSoup(rawsrc,"html.parser")
div=src.find_all("table")[10]

divv=div.find_all("tr")     
l=[]
for item in divv:
    d={}
    try:
        d["name of company"]=(item.find_all("td")[0].text.replace("•","").replace("\n",""))
    except:
        d["name of company"]=(None)
    l.append(d)  
for item in divv:
    d={}
    try:
        d["name of company"]=(item.find_all("td")[1].text.replace("•","").replace("\n",""))
    except:
        d["name of company"]=(None)
    l.append(d)
for item in divv:
    d={}
    try:
        d["name of company"]=(item.find_all("td")[2].text.replace("•","").replace("\n",""))
    except:
        d["name of company"]=(None)
    l.append(d)    
df=pandas.DataFrame(l)
df.to_csv("mctrgit_companies.csv")

