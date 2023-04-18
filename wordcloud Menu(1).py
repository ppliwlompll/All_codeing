#!/usr/bin/env python
# coding: utf-8

# # Import Library

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from sklearn.feature_extraction.text import TfidfVectorizer
from wordcloud import STOPWORDS
from pythainlp.tokenize import word_tokenize
from pythainlp.corpus import thai_stopwords


# # Loading dataset

# In[3]:


w = pd.read_csv(r'C:\Users\COM01\Downloads\Woognai_Cooking_all.csv')
w


# # Worldcould

# In[4]:


w['Viewer'] = w['Viewer'].str.replace("ครั้ง","")
w['Viewer'] = w['Viewer'].str.replace("อ่าน","")
w['Viewer'] = w['Viewer'].str.replace("k","00")
w['Viewer'] = w['Viewer'].str.replace("\.","")
w


# In[5]:


w.dtypes


# In[6]:


w['Viewer'] = w['Viewer'].astype(float)


# In[7]:


w.dtypes


# In[8]:


pd.set_option('display.max_colwidth', None)


# In[9]:


text = " ".join(i for i in w.Name)


# In[10]:


text = ''
for row in w.Name:
    text = text + row.lower() + ''


# In[11]:


path = r"C:\Users\COM01\Downloads\THSarabunNew.ttf"


# In[28]:


w['Sentiment'] = np.where(w['Viewer'] >= 1500 , 'Positive','Negative')


# In[29]:


wordcloud = WordCloud(font_path=path,
                      stopwords=thai_stopwords(),
                      background_color="white",
                      min_font_size=1,
                      width=1024,
                      height=768, 
                      max_words=500,
                      collocations=False,
                      regexp=r"[ก-๙a-zA-Z']+",
                      margin=2
                      ).generate(text)


# In[30]:


plt.figure(figsize=(15,10))
plt.imshow(wordcloud)
plt.axis('off')
plt.tight_layout(pad=0)
plt.show()


# # Positive and Negative Score

# In[31]:


w


# In[32]:


negative = w[w['Viewer'] <= 1500]
positive = w[w['Viewer'] > 1500]

negative_str = negative.Name.str.cat()
positive_str = positive.Name.str.cat()


# In[33]:


wordcloud_negative = WordCloud(font_path=path,
                      stopwords=thai_stopwords(),
                      background_color="white",
                      min_font_size=1,
                      width=1024,
                      height=768, 
                      max_words=400,
                      collocations=False,
                      regexp=r"[ก-๙a-zA-Z']+",
                      margin=2
                      ).generate(negative_str)
wordcloud_positive= WordCloud(font_path=path,
                      stopwords=thai_stopwords(),
                      background_color="white",
                      min_font_size=1,
                      width=1024,
                      height=768, 
                      max_words=400,
                      collocations=False,
                      regexp=r"[ก-๙a-zA-Z']+",
                      margin=2
                      ).generate(positive_str)


# # Visualization

# In[34]:


plt.figure(figsize=(15,10))
plt.imshow(wordcloud_negative)
plt.axis('off')
plt.tight_layout(pad=0)
plt.show()


# In[35]:


plt.figure(figsize=(15,10))
plt.imshow(wordcloud_positive)
plt.axis('off')
plt.tight_layout(pad=0)
plt.show()


# In[ ]:




