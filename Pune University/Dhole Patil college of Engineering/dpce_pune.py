#!/usr/bin/env python
# coding: utf-8

# In[7]:


import requests
from bs4 import BeautifulSoup
import pandas
r=requests.get("https://www.dpespune.com/industry-institute-interaction/a-z-recruiters/")
rawsrc=r.content
src=BeautifulSoup(rawsrc,"html.parser")
div=src.find_all("main",{"class","main"})
for item in div:
    x=item.find_all("li")
l=[]
for i in range(len(x)):
    l.append(x[i].getText())
m=[]
for i in range(len(l)):
    d={}
    try:
        d["name of company"]=l[i]
    except:
        pass
    m.append(d)  
df=pandas.DataFrame(m)
df.to_csv("dpce_pune_companies.csv")
    


# In[ ]:




