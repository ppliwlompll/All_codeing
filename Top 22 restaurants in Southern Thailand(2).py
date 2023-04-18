#!/usr/bin/env python
# coding: utf-8

# In[1]:


import bs4
import pandas as pd
import requests
import selenium
from bs4 import BeautifulSoup
from selenium import webdriver 
from selenium.webdriver.firefox.options import Options
import time


# In[2]:


options = Options()
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
driver = webdriver.Firefox(executable_path=r'C:\Users\COM01\Documents\Pliwlom\DSI 314\geckodriver.exe', options=options)
driver.get('https://www.wongnai.com/listings/dont-miss-restaurants-in-southern-of-thailand')


# In[3]:


driver.execute_script("document.body.style.MozTransform='scale(0.1)';")
driver.execute_script('document.body.style.MozTransformOrigin = "0 0";')


# In[4]:


data = driver.page_source
soup = bs4.BeautifulSoup(data)
time.sleep(6)


# In[5]:


all_Name = soup.find_all('h3',{'class':"sc-3bgfff-2 fPFiZe bd36 bd24-mWeb"})


# In[6]:


all_Name_list = []
for Name in all_Name:
    all_Name_list.append(Name.text)
all_Name_list


# In[7]:


all_Rating = soup.find_all('div',{'class':"BaseGap-sc-1wadqs8 gpdArF"})


# In[8]:


all_Rating_list = []
for Rating in all_Rating:
    all_Rating_list.append(Rating.text)
all_Rating_list


# In[9]:


all_Review = soup.find_all('span',{'class':"sc-1uyabda-0 iQqWsz rg14-mWeb rg16 text-gray-550 font-highlight"})


# In[10]:


all_Review_list = []
for Review in all_Review:
    all_Review_list.append(Review.text)
all_Review_list


# In[11]:


all_Typefood = soup.find_all('span',{'class':"bbsi3i-0 kifiY"})


# In[18]:


all_Typefood_list = []
for Typefood in all_Typefood:
    all_Typefood_list.append(Typefood.text)
all_Typefood_list


# In[36]:


Wongnai_data = pd.DataFrame([all_Name_list,all_Rating_list,all_Review_list, all_Typefood_list])


# In[37]:


Wongnai_data = Wongnai_data.transpose()
Wongnai_data.columns = ['Name','Rating','Review','Typefood']


# In[38]:


Wongnai_data


# In[39]:


Wongnai_data.to_excel('Wongnai_lisiting.xlsx', encoding='utf-8')


# In[ ]:




