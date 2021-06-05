#!/usr/bin/env python
# coding: utf-8

# In[18]:


import requests
from bs4 import BeautifulSoup
import pandas
r=requests.get("https://www.aitpune.com/Placements.aspx")
rawsrc=r.content
src=BeautifulSoup(rawsrc,"html.parser")
div=src.find_all("table",{"class","table-hover"})
for item in div:
    x=item.find_all("td")
l=[]
for i in range(len(x)-1):
    d={}
    try:
        d["name of company"]=x[i].getText().replace("\t","")
    except:
        d["name of company"]=(None)
    l.append(d)  
df=pandas.DataFrame(l)
df.to_csv("ait_pune_companies.csv")      
    


# In[ ]:




