#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd


# In[4]:


import matplotlib.pyplot as plt


# In[5]:


dataset=pd.read_csv("C:\\Users\\Super\\OneDrive\\Documents\\Iris Data.csv")


# In[6]:


dataset


# In[10]:


x=dataset.SepalLengthCm


# In[11]:


y=dataset.SepalWidthCm


# In[12]:


plt.scatter(x,y)
plt.grid()

