#!/usr/bin/env python
# coding: utf-8

# In[37]:


import requests
from bs4 import BeautifulSoup
import pandas
r=requests.get("http://www.vit.edu/index.php/placements/recruiting-companies")
rawsrc=r.content
src=BeautifulSoup(rawsrc,"html.parser")
div=src.find_all("p")
l=[]
for i in range(len(div)-5):
    if (i<51):
        l.append(div[i].getText())
    elif (i>51 and i<114):
        l.append(div[i].getText())
    elif (i==115):
        l.append(div[i].getText())
    elif (i>116 and i<186):
        l.append(div[i].getText())
    elif (i>186 and i<247):
        l.append(div[i].getText())
l= list(dict.fromkeys(l))
m=[]
for i in range(len(l)):
    d={}
    try:
        d["name of company"]=l[i]
    except:
        d["name of company"]=(None)
    m.append(d)  
df=pandas.DataFrame(m)
df.to_csv("vishwakarma_pune_companies.csv")


# In[ ]:




