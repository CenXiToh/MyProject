#!/usr/bin/env python
# coding: utf-8

# In[1]:


# lay out all the characters that we need
uppercaseletters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowercaseletters = uppercaseletters.lower()
numbers = '1234567890'
symbols = '*&^%$#)\(:;'


# In[ ]:





# In[2]:


# use boolean to select what to include in the password
upper, lower, number, symbol = True, True, True, True


# In[3]:


string = ''


# In[4]:


if upper:
    string += uppercaseletters
    
if lower:
    string += lowercaseletters
    
if number:
    string += numbers
    
if symbol:
    string += symbols


# In[ ]:





# In[5]:


import random


# In[6]:


# decide the length of the password
length = int(input('How many characters do you want your password to have? Please input a whole number: '))


# In[7]:


# create the password
password = ''.join(random.choices(string,k=(length)))
print(password)

