#!/usr/bin/env python
# coding: utf-8

# In[12]:


import csv
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException


# In[13]:


options = Options()

options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'

driver = webdriver.Firefox(executable_path=r'C:\Users\COM01\Documents\Pliwlom\DSI 314\geckodriver.exe', options=options)

driver.get('https://www.wongnai.com')


# In[14]:


def get_url(search_term):
    template = 'https://www.wongnai.com/recipes?q=%E0%B9%80%E0%B8%A1%E0%B8%99%E0%B8%B9%E0%B8%AD%E0%B8%B2%E0%B8%AB%E0%B8%B2%E0%B8%A3%E0%B9%84%E0%B8%97%E0%B8%A2%E0%B8%A2%E0%B8%AD%E0%B8%94%E0%B8%AE%E0%B8%B4%E0%B8%95&sort.type=1'
    search_term = search_term.replace(' ' , '+')
    return template.format(search_term)


# In[15]:


url = get_url('สูตรอาหารยอดนิยม')
print(url)


# In[16]:


driver.get(url)


# In[17]:


soup = BeautifulSoup(driver.page_source,'html.parser')


# In[18]:


results = soup.find_all('div',{'class':'sc-5qrr3t-0 jnqsRQ'})


# In[19]:


len(results)


# In[20]:


results[0].find('h2',{'class':'sc-5qrr3t-6 klzfDm'}).get_text()


# In[21]:


results[0].find('p',{'class':'sc-6u9vr3-0 fLZVAW sc-5qrr3t-9 jkgRbR'}).get_text()


# In[23]:


product_name = []
product_viewer = []
recipe_by = []

website = 'https://www.wongnai.com/recipes?q=%E0%B9%80%E0%B8%A1%E0%B8%99%E0%B8%B9%E0%B8%AD%E0%B8%B2%E0%B8%AB%E0%B8%B2%E0%B8%A3%E0%B9%84%E0%B8%97%E0%B8%A2%E0%B8%A2%E0%B8%AD%E0%B8%94%E0%B8%AE%E0%B8%B4%E0%B8%95&sort.type=1' 
driver.get(website)

while True:
    try:
        btn = driver.find_element_by_css_selector(".sc-AxiKw").click()
    except NoSuchElementException:
        break
            
    soup = BeautifulSoup(driver.page_source,'html.parser')
    results = soup.find_all('div',{'class':'sc-5qrr3t-0 jnqsRQ'})
    for result in results:
        try:
            product_name.append(result.find('h2',{'class':'sc-5qrr3t-6 klzfDm'}).get_text())
        except:
            product_name.append('n/a')
        try:
            product_viewer.append(result.find('p',{'class':'sc-6u9vr3-0 fLZVAW sc-5qrr3t-9 jkgRbR'}).get_text())
        except:
            product_viewer.append('n/a')


# In[25]:


Woognai_Cooking = pd.DataFrame({'Name':product_name , 'Viewer':product_viewer})


# In[26]:


Woognai_Cooking


# In[28]:


Woognai_Cooking.to_excel('Woognai_Cooking_all.xlsx',index=False)


# In[ ]:




