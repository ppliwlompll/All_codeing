#!/usr/bin/env python
# coding: utf-8

# In[9]:


pip install xlwt


# In[10]:


pip install pandas-explode


# In[11]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
import random
import json
from scholarly import scholarly
import requests
from bs4 import BeautifulSoup
import re
import csv
import pandas as pd


# In[12]:


chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)


# In[13]:


driver = webdriver.Chrome(r"C:\Users\COM01\Downloads\chromedriver_win32 (1)\chromedriver.exe", chrome_options=chrome_options)
driver.get('https://id.elsevier.com/as/authorization.oauth2?platSite=SC%2Fscopus&ui_locales=en-US&scope=openid+profile+email+els_auth_info+els_analytics_info+urn%3Acom%3Aelsevier%3Aidp%3Apolicy%3Aproduct%3Aindv_identity&response_type=code&redirect_uri=https%3A%2F%2Fwww.scopus.com%2Fauthredirect.uri%3FtxGid%3D9a61dba451cc228daa0169ce70312254&state=userLogin%7CtxId%3D55A652A039C8CA86B02E36650AF69927.i-0dcf1575680fbeb33%3A5&authType=SINGLE_SIGN_IN&prompt=login&client_id=SCOPUS')
# log-in by self


# In[14]:


# read csv file 
# list scopus id into list_id
data_all = pd.read_csv(r"C:\Users\COM01\Downloads\5065-6330.csv",encoding='latin1')
list_id = ["56667622500", "57222758601"]


# In[15]:


scholar = []
for id in list_id:
    driver.get(f'https://www.scopus.com/authid/detail.uri?authorId={id}')
    time.sleep(3)
    
    button = driver.find_element(By.XPATH, '//*[@id="documents-panel"]/div[2]/div/div[2]/div/els-results-layout/div[1]/ul/li[1]/div/div[1]/els-collapsible-panel-v2/div/button')
    button.click()
    
    li_elements = driver.find_elements(By.XPATH, '//*[@id="documents-panel"]/div[2]/div/div[2]/div/els-results-layout/div[1]/ul/li')

    for li in li_elements:
        button = li.find_element(By.XPATH, './/div/div/els-collapsible-panel-v2/div/button')
        button.click()
        

    author_name = driver.find_element(By.XPATH, '//h1[@data-testid="author-profile-name"]').text
    author_id = id 
    num_doc = driver.find_element(By.XPATH, '(//*/span[@data-testid="unclickable-count"])[2]').text
    titile_date = driver.find_element(By.XPATH, '//*[@id="documents-panel"]/div[2]/div/div[2]/div/els-results-layout/div[1]/ul/li[1]/div/div[1]/div[3]/span').text
    
    # show 200 result
    
    try:
        driver.find_element(By.XPATH, '//*[@id="documents-panel"]/div[2]/div/div[2]/div/els-results-layout/els-paginator/nav/els-select/div/label/select/option[5]').click()
        time.sleep(3)
    except:
        pass
    
    research_list = []
    researchs = driver.find_elements(By.XPATH, "//*/els-results-layout//h4")
    for i in range(len(researchs)):
        research_list.append(researchs[i].text)
    
    abs_list = []
    abs = driver.find_elements(By.XPATH, '//*/els-results-layout//els-collapsible-panel-v2/section')
    for i in range(len(abs)):
        abs_list.append(abs[i].text)
    
    print(author_name, "Number of Documents :", num_doc)
    

    scopus = dict()
    scopus['author_id']  = author_id
    scopus['author_name'] = author_name
    scopus['documents_number'] = num_doc
    scopus['date'] = titile_date
    scopus['documents'] = list()
    for i in range(int(num_doc.split(" ")[0])):
        temp_dict = dict()
        temp_dict['title'] = research_list[i]
        
        try : 
            temp_dict['abstraction'] = abs_list[i]
        except :
            abstraction.append('n/a')
            
        scopus['documents'].append(temp_dict)

    scholar.append(scopus)


# In[16]:


scholar


# In[36]:


df1 = pd.DataFrame(scholar, columns = ['author_id', 'author_name', 'documents_number', 'documents'])


# In[37]:


df1


# In[38]:


df1['documents'][0]


# In[39]:


type(df1['documents'][0])


# In[40]:


df1['documents'][0][1]


# In[41]:


df1=df1.explode('documents')
df1


# In[42]:


df1['main_title']=df1['documents'].apply(lambda v:v)
df1


# In[43]:


df1['main_abstract']=df1['main_title'].apply(lambda v:v)
df1


# In[44]:


df1['main_title'].apply(lambda v: v['title'])


# In[45]:


df1['Title']=df1['main_title'].apply(lambda v:v['title'])
df1


# In[46]:


df1['main_abstract'].apply(lambda v: v['abstraction'])


# In[47]:


df1['Abstraction']=df1['main_abstract'].apply(lambda v:v['abstraction'])
df1


# In[48]:


df1.drop(['documents' , 'main_title' , 'main_abstract' , 'documents_number'], axis=1)


# In[49]:


df1.to_excel('resercher_all.xls',index=False)

