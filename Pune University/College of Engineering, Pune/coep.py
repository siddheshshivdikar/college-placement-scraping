
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup
import pandas

r=requests.get("http://www.coep.org.in/placementcell/recruiters")
rawsrc=r.content
src=BeautifulSoup(rawsrc,"html.parser")

all=src.find_all("tr")
l=[]
for item in all:
    d={}
    d["Company Name"]=(item.find_all("td")[1].text.replace("\n",""))
    l.append(d)
l
df=pandas.DataFrame(l)
df
df.to_csv("coep_companies.csv")

