#!/usr/bin/env python
# coding: utf-8

# In[34]:


import requests
from bs4 import BeautifulSoup
import pandas
r1=requests.get("http://www.srespune.org/2015")
r2=requests.get("http://www.srespune.org/2016")
r3=requests.get("http://www.srespune.org/2017")
rawsrc1=r1.content
rawsrc2=r2.content
rawsrc3=r3.content
src1=BeautifulSoup(rawsrc1,"html.parser")
src2=BeautifulSoup(rawsrc2,"html.parser")
src3=BeautifulSoup(rawsrc3,"html.parser")
div1=src1.find_all("td")
l1=[]
m1=[]
for i in range(len(div1)):
    if(i>4):
        l1.append(div1[i].getText().replace("\n",""))
for i in range(len(l1)):
    if (i%3==0):
        m1.append(l1[i])
m1=list(dict.fromkeys(m1))
div2=src2.find_all("td")
l2=[]
m2=[]
for i in range(len(div2)):
    if(i>4):
        l2.append(div2[i].getText().replace("\n",""))
for i in range(len(l2)):
    if (i%3==0):
        m2.append(l2[i])
m2=list(dict.fromkeys(m2))
div3=src3.find_all("td")
l3=[]
m3=[]
for i in range(len(div3)):
    if(i>4):
        str=div3[i].getText().replace("\n","")
        str=str.replace("\r","")
        str=str.replace("\t","")
        str=str.replace("\xa0","")
        l3.append(str)
for i in range(len(l3)):
    if (i%3==0):
        m3.append(l3[i])
m3=list(dict.fromkeys(m3))
for i in range(len(m2)):
    m1.append(m2[i])
for i in range(len(m3)):
    m1.append(m3[i])
m1=list(dict.fromkeys(m1))
m4=[]
for i in range(len(m1)):
    d={}
    try:
        d["name of company"]=m1[i]
    except:
        pass
    m4.append(d)  
df=pandas.DataFrame(m4)
df.to_csv("sres_pune_companies.csv")






        

    


# In[ ]:




