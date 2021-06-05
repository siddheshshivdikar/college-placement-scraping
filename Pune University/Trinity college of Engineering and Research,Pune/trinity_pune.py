#!/usr/bin/env python
# coding: utf-8

# In[47]:


import requests
from bs4 import BeautifulSoup
import pandas
r=requests.get("http://www.kjei.edu.in/tcoer/placement/placement_activities.html#")
rawsrc=r.content
src=BeautifulSoup(rawsrc,"html.parser")
div=src.find_all("td")
l1=[]
l2=[]
l3=[]
l4=[]
m=[]
for i in range(len(div)):
    if(i>1 and i<=74):
        l1.append(div[i].getText())
    if(i>91 and i<=401):
        l2.append(div[i].getText())
    if(i>403 and i<=470):
        l3.append(div[i].getText())
    if(i>475 and i<=605):
        l4.append(div[i].getText())
for i in range(len(l1)):
    if(i%3==0):
        m.append(l1[i].replace("\xa0",""))
for i in range(len(l2)):
    if(i%3==0):
        m.append(l2[i].replace("\xa0",""))
for i in range(len(l3)):
    if(i%3==0):
        m.append(l3[i].replace("\xa0",""))
for i in range(len(l4)):
    if(i%3==0):
        m.append(l4[i].replace("\xa0",""))
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
df.to_csv("trinity_pune_companies.csv")



    


# In[ ]:




