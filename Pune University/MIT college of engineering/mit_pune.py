#!/usr/bin/env python
# coding: utf-8

# In[9]:


import requests
from bs4 import BeautifulSoup
import pandas
r=requests.get("http://mitcoe.ac.in/career-placements/")
rawsrc=r.content
src=BeautifulSoup(rawsrc,"html.parser")
div=src.find_all("table")
l=[]
for item in div:
    x=item.find_all("td")
for i in range(len(x)-2):
    d={}
    try:
        d["name of company"]=x[i].getText()
    except:
        d["name of company"]=(None)
    l.append(d)
df=pandas.DataFrame(l)
df.to_csv("mit_pune_companies.csv")  
    


# In[ ]:




