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
driver.get('https://baan.kaidee.com/c19p8-realestate-land/krabi?locations=%2Fchumphon%2Fp19%2C%2Ftrang%2Fp20%2C%2Fnakhonsithammarat%2Fp27%2C%2Fnarathiwat%2Fp30%2C%2Fpattani%2Fp36%2C%2Fphangnga%2Fp39%2C%2Fphatthalung%2Fp40%2C%2Fphuket%2Fp43%2C%2Fyala%2Fp47%2C%2Franong%2Fp49%2C%2Fsongkhla%2Fp57%2C%2Fsatun%2Fp58%2C%2Fsuratthani%2Fp67')


# In[3]:


driver.execute_script("document.body.style.MozTransform='scale(0.1)';")
driver.execute_script('document.body.style.MozTransformOrigin = "0 0";')


# In[4]:


data = driver.page_source
soup = bs4.BeautifulSoup(data)
time.sleep(6)


# In[5]:


all_Name = soup.find_all('h2',{'class':"_7f17f34f"})


# In[6]:


all_Name_list = []
for Name in all_Name:
    all_Name_list.append(Name.text)
all_Name_list


# In[7]:


all_Size= soup.find_all('span',{'class':"b6a29bc0"})


# In[8]:


all_Size_list = []
for Size in all_Size:
    all_Size_list.append(Size.text)
all_Size_list


# In[9]:


all_Type = soup.find_all('div',{'class':"_9a4e3964"})


# In[10]:


all_Type_list = []
for Type in all_Type:
    all_Type_list.append(Type.text)
all_Type_list


# In[11]:


all_Price = soup.find_all('span',{'class':"f343d9ce"})


# In[12]:


all_Price_list = []
for Price in all_Price:
    all_Price_list.append(Price.text)
all_Price_list


# In[13]:


all_Location = soup.find_all('div',{'class':"_7afabd84"})


# In[14]:


all_Location_list = []
for Location in all_Location:
    all_Location_list.append(Location.text)
all_Location_list


# In[15]:


Land_sale_data = pd.DataFrame([all_Name_list,all_Size_list,all_Type_list, all_Price_list,all_Location_list])


# In[16]:


Land_sale_data = Land_sale_data.transpose()
Land_sale_data.columns = ['Name','Size','Type','Price','Location']


# In[17]:


Land_sale_data


# In[18]:


Land_sale_data.to_excel('Land_sale.xlsx', encoding='utf-8')

