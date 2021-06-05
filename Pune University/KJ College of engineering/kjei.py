#!/usr/bin/env python
# coding: utf-8

# In[98]:


import requests
from bs4 import BeautifulSoup
import pandas
r=requests.get("http://www.kjei.edu.in/kjcoemr/placement/placement_activities.html")
rawsrc=r.content
src=BeautifulSoup(rawsrc,"html.parser")
div_1718=src.find_all("table")[0]
for item in div_1718:
    try:
        divv_1718=(item.find_all("tr"))
    except:
        pass
l_1718=[]
for item in divv_1718:
    d_1718={}
    try:
        d_1718['Student name']=item.find_all("td")[1].text
    except:
        pass
    try:
        d_1718['Company name']=item.find_all("td")[2].text
    except:
        pass
    try:
        d_1718['Student name']=item.find_all("td")[4].text
    except:
        pass
    try:
        d_1718['Company name']=item.find_all("td")[5].text
    except:
        pass
    l_1718.append(d_1718)
df_1718=pandas.DataFrame(l_1718)
df.to_csv("kjei_1718_companies.csv")

div_1617=src.find_all("table")[1]
for item in div_1617:
    try:
        divv_1617=(item.find_all("tr"))
    except:
        pass
l_1617=[]
for item in divv_1617:
    d_1617={}
    try:
        d_1617['Student name']=item.find_all("td")[1].text
    except:
        pass
    try:
        d_1617['Company name']=item.find_all("td")[2].text
    except:
        pass
    try:
        d_1617['Student name']=item.find_all("td")[4].text
    except:
        pass
    try:
        d_1617['Company name']=item.find_all("td")[5].text
    except:
        pass
    l_1617.append(d_1617)
df_1617=pandas.DataFrame(l_1617)
df.to_csv("kjei_1617_companies.csv")

div_1516=src.find_all("table")[2]
for item in div_1516:
    try:
        divv_1516=(item.find_all("tr"))
    except:
        pass
l_1516=[]
for item in divv_1516:
    d_1516={}
    try:
        d_1516['Student name']=item.find_all("td")[1].text
    except:
        pass
    try:
        d_1516['Company name']=item.find_all("td")[2].text
    except:
        pass
    try:
        d_1516['Student name']=item.find_all("td")[4].text
    except:
        pass
    try:
        d_1516['Company name']=item.find_all("td")[5].text
    except:
        pass
    l_1516.append(d_1516)
df_1516=pandas.DataFrame(l_1516)
df.to_csv("kjei_1516_companies.csv")

div_1415=src.find_all("table")[3]
for item in div_1415:
    try:
        divv_1415=(item.find_all("tr"))
    except:
        pass
l_1415=[]
for item in divv_1415:
    d_1415={}
    try:
        d_1415['Student name']=item.find_all("td")[1].text
    except:
        pass
    try:
        d_1415['Company name']=item.find_all("td")[2].text
    except:
        pass
    try:
        d_1415['Student name']=item.find_all("td")[4].text
    except:
        pass
    try:
        d_1415['Company name']=item.find_all("td")[5].text
    except:
        pass
    l_1415.append(d_1415)
df_1415=pandas.DataFrame(l_1415)
df.to_csv("kjei_1415_companies.csv")

div_1314=src.find_all("table")[4]
for item in div_1314:
    try:
        divv_1314=(item.find_all("tr"))
    except:
        pass
l_1314=[]
for item in divv_1314:
    d_1314={}
    try:
        d_1314['Student name']=item.find_all("td")[1].text
    except:
        pass
    try:
        d_1314['Company name']=item.find_all("td")[2].text
    except:
        pass
    try:
        d_1314['Student name']=item.find_all("td")[4].text
    except:
        pass
    try:
        d_1314['Company name']=item.find_all("td")[5].text
    except:
        pass
    l_1314.append(d_1314)
df_1314=pandas.DataFrame(l_1314)
df.to_csv("kjei_1314_companies.csv")


# In[99]:


df_1314


# In[ ]:




