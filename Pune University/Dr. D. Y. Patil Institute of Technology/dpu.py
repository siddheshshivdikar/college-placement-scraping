#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests
from bs4 import BeautifulSoup
import pandas
r=requests.get("http://engg.dypvp.edu.in/Companies.aspx")
rawsrc=r.content
src=BeautifulSoup(rawsrc,"html.parser")
div=src.find_all("table",{"class","customers"})
for item in div:
    x=item.find_all("td")
l=[]
for i in range(len(x)-1):
    if (i%2!=0):
        d={}
        try:
            d["name of company"]=x[i].getText()
        except:
            d["name of company"]=(None)
        l.append(d)    
df=pandas.DataFrame(l)
df.to_csv("dpucompanies.csv")  
    
    

    
    
    


# In[ ]:




