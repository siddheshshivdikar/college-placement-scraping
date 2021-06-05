#!/usr/bin/env python
# coding: utf-8

# In[32]:


import requests
from bs4 import BeautifulSoup
import pandas
r=requests.get("http://jaihind.edu.in/jcoe/placements/students-recruited.php")
rawsrc=r.content
src=BeautifulSoup(rawsrc,"html.parser")
div=src.find_all("td")
l=[]
m=[]
for i in range(len(div)-38):
    if(i>1):
        l.append(div[i].getText())
for i in range(len(l)):
    if(i%5==0):
        m.append(l[i])
m=list(dict.fromkeys(m))
n=[]
for i in range(len(m)):
    d={}
    try:
        d["name of company"]=m[i]
    except:
        pass
    n.append(d)  
df=pandas.DataFrame(n)
df.to_csv("jaihind_pune_companies.csv")


            


# In[ ]:




