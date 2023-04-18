#!/usr/bin/env python
# coding: utf-8

# # Import Iibrary

# In[1]:


import numpy as np
import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt
import sklearn.cluster as cluster
import sklearn.metrics as metrics
import matplotlib as mpl
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score


# # Load Dataset

# In[2]:


df = pd.read_csv(r"C:\Users\COM01\Downloads\province.csv")
colnames = list(df.columns[1:-1])
df


# In[3]:


df.head()


# # Data Cleaning

# In[4]:


df.isna().sum()


# In[5]:


df.shape


# In[6]:


df.info()


# In[7]:


df.describe()


# # Data Preparation

# In[8]:


df_Short = df[['Number_of_foreign_visitors','Income_from_foreign_visitors']]
df_Short.head()


# In[9]:


attributes = ['Number_of_foreign_visitors','Income_from_foreign_visitors']
plt.rcParams['figure.figsize'] = [10,8]
sns.boxplot(data = df[attributes], orient="v", palette="Set2" ,whis=1.5,saturation=1, width=0.7)
plt.title("Outliers Variable Distribution", fontsize = 14, fontweight = 'bold')
plt.ylabel("Range", fontweight = 'bold')
plt.xlabel("Attributes", fontweight = 'bold')


# In[10]:


df.info()


# In[11]:


Q1 = df.Number_of_foreign_visitors.quantile(0.05)
Q3 = df.Number_of_foreign_visitors.quantile(0.95)
IQR = Q3 - Q1
df = df[(df.Number_of_foreign_visitors >= Q1 - 1.5*IQR) & (df.Number_of_foreign_visitors <= Q3 + 1.5*IQR)]


# In[12]:


Q1 = df.Income_from_foreign_visitors .quantile(0.05)
Q3 = df.Income_from_foreign_visitors .quantile(0.95)
IQR = Q3 - Q1
df = df[(df.Income_from_foreign_visitors  >= Q1 - 1.5*IQR) & (df.Income_from_foreign_visitors  <= Q3 + 1.5*IQR)]


# In[13]:


df


# In[14]:


scaler = MinMaxScaler()

scaler.fit(df[['Number_of_foreign_visitors']])
df['Income_from_foreign_visitors'] = scaler.transform(df[['Number_of_foreign_visitors']])

scaler.fit(df[['Income_from_foreign_visitors']])
df['Number_of_foreign_visitors'] = scaler.transform(df[['Income_from_foreign_visitors']])


# In[15]:


df_new = df[['Number_of_foreign_visitors', 'Income_from_foreign_visitors']]


scaler = StandardScaler()

df_new_scaled = scaler.fit_transform(df_new)
df_new_scaled.shape


# In[16]:


df_new_scaled = pd.DataFrame(df_new_scaled)
df_new_scaled.columns = ['Number_of_foreign_visitors', 'Income_from_foreign_visitors']
df_new_scaled.head()


# # Elbow Method

# In[17]:


kmeans = KMeans(n_clusters=4, max_iter=50)
kmeans.fit(df_new_scaled)


# In[18]:


kmeans.labels_


# In[19]:


kmeans.inertia_


# In[20]:


ssd = []
range_n_clusters = [2, 3, 4, 5, 6, 7, 8]
for num_clusters in range_n_clusters:
    kmeans = KMeans(n_clusters=num_clusters, max_iter=50)
    kmeans.fit(df_new_scaled)
    
    ssd.append(kmeans.inertia_)
    
# plot the SSDs for each n_clusters
plt.plot(ssd)


# # Silhouette Method

# In[21]:


SK = range(2,13)
sil_score = []
for i in SK:
    labels=cluster.KMeans(n_clusters=i,init="k-means++",random_state=200).fit(df_new_scaled).labels_
    score = metrics.silhouette_score(df_new_scaled,labels,metric="euclidean",sample_size=1000,random_state=200)
    sil_score.append(score)
    print ("Silhouette score for k(clusters) = "+str(i)+" is "
           +str(metrics.silhouette_score(df_new_scaled,labels,metric="euclidean",sample_size=1000,random_state=200)))


# In[22]:


sil_centers = pd.DataFrame({'Clusters' : SK, 'Silhouette score' : sil_score})
sil_centers


# In[23]:


sns.lineplot(x = 'Clusters', y = 'Silhouette score', data = sil_centers, marker="+")


# In[24]:


df_shorts = df[['Number_of_foreign_visitors','Number_of_foreign_visitors']]
df_shorts.head()


# In[25]:


SK = range(2,13)
sil_score = []
for i in SK:
    labels=cluster.KMeans(n_clusters=i,init="k-means++",random_state=200).fit(df_shorts).labels_
    score = metrics.silhouette_score(df_shorts,labels,metric="euclidean",sample_size=1000,random_state=200)
    sil_score.append(score)
    print ("Silhouette score for k(clusters) = "+str(i)+" is "
           +str(metrics.silhouette_score(df_shorts,labels,metric="euclidean",sample_size=1000,random_state=200)))


# # K-means Clustering 

# In[26]:


kmeans = cluster.KMeans(n_clusters=2 ,init="k-means++")
kmeans = kmeans.fit(df[['Number_of_foreign_visitors','Income_from_foreign_visitors']])


# In[27]:


df['Clusters'] = kmeans.labels_


# In[28]:


kmeans.labels_


# In[29]:


sns.scatterplot(x="Number_of_foreign_visitors", y="Income_from_foreign_visitors",hue = 'Clusters',  data=df)


# In[30]:


score = silhouette_score(df_shorts, kmeans.labels_, metric='euclidean')
print('Silhouetter Score: %.14f' % score)
print("Inertia: ", kmeans.inertia_)


# # Final Analysic

# In[31]:


df = df.drop(columns = ['Occupancy_rate','Number_of _guests','Total_number_of_visitors','Income _from_visitors','Income_from_Thai_visitors'])


# In[32]:


df


# In[33]:


print(df[df['Clusters'] == 1])


# In[ ]:




