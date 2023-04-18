#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install selenium')
get_ipython().system('pip install bs4')
get_ipython().system('pip install pandas')


# In[2]:


import bs4
import pandas as pd
import time
from selenium import webdriver


# In[3]:


driver = webdriver.Chrome(executable_path=r'C:\Users\COM01\Documents\Pliwlom\DSI 314\chromedriver')


# In[4]:


driver.get('https://www.expedia.com/Hotel-Search?adults=2&d1=2022-11-08&d2=2022-11-09&destination=Bangkok%20%28and%20vicinity%29%2C%20Bangkok%20Province%2C%20Thailand&endDate=2022-11-09&latLong=13.7475%2C100.53601&regionId=178236&rooms=1&semdtl=&sort=RECOMMENDED&startDate=2022-11-08&theme=&useRewards=false&userIntent=')


# In[5]:


driver.execute_script("document.body.style.zoom='10%'")


# In[ ]:


data = driver.page_source
soup = bs4.BeautifulSoup(data)
time.sleep(6)


# In[ ]:


all_rest = soup.find_all('div',{'class':"uitk-spacing uitk-spacing-padding-blockend-three uitk-layout-flex-item"})


# In[ ]:


all_rest_list = []
for rest in all_rest:
    all_rest_list.append(rest.text)
all_rest_list


# In[ ]:


all_price = soup.find_all('div',{'class':'uitk-text uitk-type-end uitk-type-200 uitk-text-default-theme'})


# In[ ]:


all_price_list = []
for price in all_price:
    all_price_list.append(price.text)
all_price_list


# In[ ]:


all_rating = soup.find_all('span',{'class':'uitk-text uitk-type-300 uitk-type-bold uitk-text-default-theme'})


# In[ ]:


all_rating_list = []
for rating in all_rating:
    all_rating_list.append(rating.text)
all_rating_list


# In[ ]:


all_service = soup.find_all('div',{'class':'uitk-text truncate uitk-type-200 uitk-text-default-theme'})


# In[ ]:


all_service_list = []
for service in all_service:
        all_service_list.append(service.text) 
all_service_list


# In[ ]:


Expedia_data = pd.DataFrame([all_rest_list,all_price_list,all_rating_list,all_service_list])


# In[ ]:


Expedia_data = Expedia_data.transpose()
Expedia_data.columns = ['rest','price','rating','service']


# In[ ]:


Expedia_data


# In[ ]:


Expedia_data.to_csv('Expedia_csv.csv' , index=False)


# In[ ]:




