#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Solution:
    
    def test(self,height):
        left = 0
        right = len(height)-1
        largest = 0
        prev_left = 0
        prev_right = 0
    
        while left != right:
            
            if height[left] < prev_left:
                left += 1
                continue
            if height[right] < prev_right:
                right -= 1
                continue
                
            current_area = min(height[left],height[right])*(right-left)
            if current_area > largest:
                largest = current_area
            
            if height[left]<height[right]:
                prev_left = height[left]
                left += 1
            
            else:
                prev_right = height[right]
                right -= 1
        
        return largest    
  


# In[2]:


s=Solution()


# In[3]:


height = [1,8,6,2,5,4,8,3,7]


# In[4]:


s.test(height)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[5]:


# It can also be done without having class


# In[1]:


def test(height):
   left = 0
   right = len(height)-1
   largest = 0
   prev_left = 0
   prev_right = 0
   
   while left != right:
           
       if height[left] < prev_left:
           left += 1
           continue
       if height[right] < prev_right:
           right -= 1
           continue
               
       current_area = min(height[left],height[right])*(right-left)
       if current_area > largest:
           largest = current_area
           
       if height[left]<height[right]:
           prev_left = height[left]
           left += 1
           
       else:
           prev_right = height[right]
           right -= 1
       
   return largest   


# In[2]:


height = [1,8,6,2,5,4,8,3,7]


# In[3]:


test(height)


# In[ ]:




