#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Solution:
    
    def test(self, digits):
        phone_map = {'2':'abc','3':'def','4':'ghi','5':'jkl',
                     '6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
              
         # if digit is an empty string, return empty list
        if digits == "":
            return []
        
        # Start with the first input digit
        # If the first input digit is 2, it will return a list of a,b,c
        numbers = list(phone_map[digits[0]])
            
        # And this is for the input digit after the first one
        # Create a double for loop
        for x in digits[1:]:
            numbers = [old + new for old in numbers for new in list(phone_map[x])]
            
        return numbers


# In[2]:


s=Solution()


# In[3]:


x = '98'


# In[4]:


s.test(x)

