
# coding: utf-8

# In[28]:


import requests
from bs4 import BeautifulSoup
import pandas

r=requests.get("https://pce.ac.in/")
rawsrc=r.content

src=BeautifulSoup(rawsrc,"html.parser")
l=[]
for img in src.find_all("img",{"class":"lshowcase-boxhighlight"}):
    d={}
    d['name of company']=(img.get('alt'))
    l.append(d)
df=pandas.DataFrame(l)
df.to_csv("pce_companies.csv")

