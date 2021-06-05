#!/usr/bin/env python
# coding: utf-8

# In[15]:


import requests
from bs4 import BeautifulSoup
import pandas
r=requests.get("https://indiraicem.ac.in/placement/")
rawsrc=r.content
src=BeautifulSoup(rawsrc,"html.parser")
div=src.find_all("td")
l=[]
m=[]
for i in range(len(div)):
    if(i<=103):
        l.append(div[i].getText().replace("\xa0",""))
    if(i>=105 and i<143):
        l.append(div[i].getText().replace("\xa0",""))
for i in range(len(l)):
    d={}
    try:
        d["name of company"]=l[i]
    except:
        pass
    m.append(d)  
df=pandas.DataFrame(m)
df.to_csv("indira_pune_companies.csv")  
    
        


# In[ ]:




