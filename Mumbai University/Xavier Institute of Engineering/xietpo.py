
# coding: utf-8

# In[21]:


import requests
from bs4 import BeautifulSoup
import pandas
r=requests.get("http://www.xietpo.in/")
rawsrc=r.content
src=BeautifulSoup(rawsrc,"html.parser")

div18=src.find_all("table",{"class","table" })[0]
divv18=div.find_all("tr")

l18=[]
for item in divv18:
    d18={}
    try:
        d18["sr no"]=(item.find_all("td")[0].text.replace("\n",""))
    except:
        d18["sr no"]=(None)
    try:
        d18["name of company"]=(item.find_all("td")[1].text.replace("\n",""))
    except:
        d18["name of company"]=(None)
    try:
        d18["number of students"]=(item.find_all("td")[2].text.replace("\n",""))
    except:
        d18["number of students"]=(None)
    l18.append(d18)    
df1=pandas.DataFrame(l18)
df1.to_csv("xietpo18_companies.csv")

div17=src.find_all("table",{"class","table" })[1]
divv17=div17.find_all("tr")

l17=[]
for item in divv17:
    d17={}
    try:
        d17["sr no"]=(item.find_all("td")[0].text.replace("\n",""))
    except:
        d17["sr no"]=(None)
    try:
        d17["name of company"]=(item.find_all("td")[1].text.replace("\n",""))
    except:
        d17["name of company"]=(None)
    try:
        d17["number of students"]=(item.find_all("td")[2].text.replace("\n",""))
    except:
        d17["number of students"]=(None)
    l17.append(d17)    
df2=pandas.DataFrame(l17)
df2.to_csv("xitepo17_companies.csv")

