#!/usr/bin/env python
# coding: utf-8

# In[5]:


import requests
from bs4 import BeautifulSoup
import pandas
r=requests.get("https://tsec.edu/placement-statistics-2/")
rawsrc=r.content
src=BeautifulSoup(rawsrc,"html.parser")


div=src.find_all("div",{"class","vc_cta3_content-container"})
l=[]

for item in div:
    d={}
    d["Name of the company"]=(item.find("h4").text)
    l.append(d)
    
df=pandas.DataFrame(l)

df.to_csv("tsec_companies.csv")


# In[4]:


df


# In[37]:


src=BeautifulSoup(rawsrc,"html.parser")
src


# In[ ]:




