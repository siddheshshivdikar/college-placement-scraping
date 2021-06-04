#!/usr/bin/env python
# coding: utf-8

# In[19]:


import requests
from bs4 import BeautifulSoup
import pandas
r=requests.get("http://www.sigce.edu.in/tpo.asp#undefined8")
rawsrc=r.content
src=BeautifulSoup(rawsrc,"html.parser")


# In[64]:


div=src.find_all("table")[4]
divv=div.find_all("tr")
l=[]
for item in divv:
    d={}
    try:
        d["Name of the company"]=(item.find_all("td")[1].text.replace("\t","").replace("\r","").replace("\n",""))
    except:
        pass
    l.append(d)
df=pandas.DataFrame(l)
df.to_csv("sigce_companies.csv")


# In[63]:





# In[ ]:




