#!/usr/bin/env python
# coding: utf-8

# ## Task3_Exploratory Data Analysis/Exploratory Data Analysis_SimpleSuperStore_Data.ipynb

# In[1]:


# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


#data loading
data=pd.read_csv('SampleSuperstore.csv')
data


# In[3]:


# Check the first five rows of the dataset
data.head()


# In[4]:


# Check the last five rows of the dataset
data.tail()


# In[5]:


# Check the number of rows and columns in the dataset
data.shape


# In[6]:


# Check the data types of the columns
data.dtypes


# In[7]:


# Check for missing values in the dataset
data.isnull().sum()


# In[8]:


# Check the statistical summary of the dataset
data.describe()


# In[9]:


# Check the correlation between the columns
data.corr()


# In[10]:


# Visualize the correlation matrix using a heatmap
sns.heatmap(data.corr(), annot=True, cmap='coolwarm')


# In[11]:


# Visualize the distribution of each column using histograms
data.hist(bins=30, figsize=(20,15))


# In[12]:


# Visualize the total sales and profit of each category using a bar plot
plt.figure(figsize=(12,6))
plt.title('Total Sales and Profit of Each Category')
sns.barplot(x='Category', y='Sales', data=data, estimator=sum, ci=None, color='b')
sns.barplot(x='Category', y='Profit', data=data, estimator=sum, ci=None, color='r')
plt.show()


# In[13]:


# Visualize the total sales and profit of each sub-category using a bar plot
plt.figure(figsize=(20,8))
plt.title('Total Sales and Profit of Each Sub-Category')
sns.barplot(x='Sub-Category', y='Sales', data=data, estimator=sum, ci=None, color='b')
sns.barplot(x='Sub-Category', y='Profit', data=data, estimator=sum, ci=None, color='r')
plt.show()


# In[14]:


# Visualize the total sales and profit of each state using a bar plot
plt.figure(figsize=(20,8))
plt.title('Total Sales and Profit of Each State')
sns.barplot(x='State', y='Sales', data=data, estimator=sum, ci=None, color='b')
sns.barplot(x='State', y='Profit', data=data, estimator=sum, ci=None, color='r')
plt.xticks(rotation=90)
plt.show()


# In[15]:


# Visualize the total sales and profit of each region using a bar plot
plt.figure(figsize=(10,6))
plt.title('Total Sales and Profit of Each Region')
sns.barplot(x='Region', y='Sales', data=data, estimator=sum, ci=None, color='b')
sns.barplot(x='Region', y='Profit', data=data, estimator=sum, ci=None, color='r')
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




