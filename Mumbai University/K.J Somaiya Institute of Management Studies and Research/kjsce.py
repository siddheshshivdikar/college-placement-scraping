
# coding: utf-8

# In[44]:


import requests
from bs4 import BeautifulSoup
import pandas
r=requests.get("https://kjsce.somaiya.edu/kjsce/placement/OUR_RECRUITERS")
rawsrc=r.content
src=BeautifulSoup(rawsrc,"html.parser")
div=src.find_all("table",{"class","displayTable" })
divv=src.find_all("tr")
l=[]
for item in divv:
    d={}
    try:
        d["name of company"]=(item.find_all("span")[2].text.replace("\n",""))
    except:
        d["name of company"]=(None)
    l.append(d)    
df=pandas.DataFrame(l)
df.to_csv("kjsce_companies.csv")    

