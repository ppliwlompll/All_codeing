#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from sklearn.feature_extraction.text import TfidfVectorizer
from wordcloud import STOPWORDS
from pythainlp.tokenize import word_tokenize
from pythainlp.corpus import thai_stopwords


# In[2]:


w = pd.read_csv(r'C:\Users\COM01\Downloads\web2.csv')
w


# In[3]:


pd.set_option('display.max_colwidth', None)


# In[4]:


text = " ".join(i for i in w.Content)


# In[5]:


text = ''
for row in w.Content:
    text = text + row.lower() + ''


# In[6]:


path = r"C:\Users\COM01\Downloads\THSarabunNew.ttf"


# In[7]:


wt = word_tokenize(text, engine='newmm')
wt


# In[8]:


wordcloud = WordCloud(font_path=path,
                      stopwords=thai_stopwords(),
                      background_color="white",
                      min_font_size=1,
                      width=1024,
                      height=768, 
                      max_words=400,
                      collocations=False,
                      regexp=r"[ก-๙a-zA-Z']+",
                      margin=2
                      ).generate(" ".join(wt))


# In[9]:


plt.figure(figsize=(15,10))
plt.imshow(wordcloud)
plt.axis('off')
plt.tight_layout(pad=0)
plt.show()


# In[ ]:




