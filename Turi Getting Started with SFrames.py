#!/usr/bin/env python
# coding: utf-8

# # Fire up Turi Create
# 
# We always start with this line before using any part of Turi Create

# In[1]:


import turicreate


# # Load a tabular data set

# In[2]:


sf = turicreate.SFrame('people-example.csv')


# # SFrame basics

# In[3]:


sf #we can view first few lines of table


# In[4]:


sf.tail()  # view end of the table


# # Turi Create visualization

# In[5]:


# .show() visualizes any data structure in Turi Create
sf.show()


# In[6]:


sf['age'].show()


# # Inspect columns of dataset

# In[7]:


sf['Country']


# In[8]:


sf['age']


# Some simple columnar operations

# In[9]:


sf['age'].mean()


# In[10]:


sf['age'].max()


# # Create new columns in our SFrame

# In[11]:


sf


# In[12]:


sf['Full Name'] = sf['First Name'] + ' ' + sf['Last Name']


# In[13]:


sf


# In[14]:


sf['age'] * sf['age']


# # Use the apply function to do a advance transformation of our data

# In[15]:


sf['Country']


# In[16]:


sf['Country'].show()


# In[17]:


def transform_country(country):
    if country == 'USA':
        return 'United States'
    else:
        return country


# In[18]:


transform_country('Brazil')


# In[19]:


transform_country('Brasil')


# In[20]:


transform_country('USA')


# In[21]:


sf['Country'].apply(transform_country)


# In[22]:


sf['Country'] = sf['Country'].apply(transform_country)


# In[23]:


sf


# In[ ]:




