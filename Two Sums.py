#!/usr/bin/env python
# coding: utf-8

# In[16]:


def twosum(x):
    list = {}
    
    for i in range(len(x)):
        num = x[i]
        complement = target - num
        
        if num in list:
            return[list[num],i] 
        else:
            list[complement] = i
        


# In[17]:


target = 9


# In[18]:


x = [2,2,6,3]


# In[19]:


twosum(x)


# In[ ]:




