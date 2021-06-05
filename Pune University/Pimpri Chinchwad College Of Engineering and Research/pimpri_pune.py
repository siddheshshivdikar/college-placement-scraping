#!/usr/bin/env python
# coding: utf-8

# In[66]:


import requests
from bs4 import BeautifulSoup
import pandas
r=requests.get("http://www.pccoepune.com/top-placement-engineering-college-in-pune.php")
rawsrc=r.content
src=BeautifulSoup(rawsrc,"html.parser")
div=src.find_all("div",{"class","table-responsive"})
for item in div:
    x=item.find_all("td")
l=[]
m=[]
for i in range(len(x)):
    if (i>=33) :
        l.append(x[i].getText())
for i in range(len(l)):
    if (i%4==0):
        d={}
        try:
            d["name of company"]=l[i]
        except:
            d["name of company"]=(None)
        m.append(d)  
df=pandas.DataFrame(m)
df.to_csv("pimpri_pune_companies.csv")  

    



        

        
           


# In[ ]:




