#!/usr/bin/env python
# coding: utf-8

# In[33]:


import requests
from bs4 import BeautifulSoup
import pandas
r=requests.get("http://www.gcoeara.ac.in/training-placement-record.php")
rawsrc=r.content
src=BeautifulSoup(rawsrc,"html.parser")
div=src.find_all("td")
l=[]
m=[]
for i in range(len(div)):
    if (i>=6) :
        l.append(div[i].getText())
for i in range(len(l)-14):
    if (i%6==0):
        d={}
        try:
            d["name of company"]=l[i]
        except:
            d["name of company"]=(None)
        m.append(d)  
df=pandas.DataFrame(m)
df.to_csv("government_pune_companies.csv")


# In[ ]:




