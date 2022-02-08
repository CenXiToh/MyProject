#!/usr/bin/env python
# coding: utf-8

# In[1]:


# To determine the relationship between weight loss and calories burned 


# In[2]:


import pandas as pd


# In[3]:


# import the weight dataframe 

df1 = pd.read_csv('C:\\Users\\cenxi\\OneDrive\\Documents\\Google Data Analytics\\Case Study Bellabeat\\Fitabase Data 4.12.16-5.12.16\\weightLogInfo_merged.csv')


# In[4]:


# Check the shape

df1.shape


# In[5]:


# Check the first row

df1.head(1)


# In[6]:


# Check the data type

df1.dtypes


# In[7]:


# Separate the date and time in the Date column because time is not needed

df1.Date = pd.to_datetime(df1['Date'])
df1 = df1.assign(Date=df1.Date.dt.date, Time=df1.Date.dt.time)


# In[8]:


# Check the columns again

df1.head(1)


# In[9]:


# Remove unwanted columns

df1 = df1.drop(['Fat','IsManualReport','LogId','Time'],axis=1)


# In[10]:


# Check the date type again

df1.dtypes


# In[11]:


# Change the date to datetime format 
df1.Date = pd.to_datetime(df1['Date'])


# In[12]:


df1.dtypes


# In[13]:


# Confirm the columes again before sorting

df1.head(1)


# In[14]:


#Sort the data to check which Id has the most complete data

sorted_df1 = df1.pivot(index='Id',columns='Date')['WeightKg']


# In[15]:


sorted_df1


# In[16]:


# ID 6962181067 has the most complete data so his/her data will be used for analysis

df1 = df1.loc[df1['Id'] == 6962181067]


# In[17]:


# Check the shape again

df1.shape


# In[18]:


# Now import the calories dataframe 

df2 = pd.read_csv('C:\\Users\\cenxi\\OneDrive\\Documents\\Google Data Analytics\\Case Study Bellabeat\\Fitabase Data 4.12.16-5.12.16\\dailyCalories_merged.csv')


# In[19]:


# Check the shape

df2.shape


# In[20]:


# Check the data type

df2.dtypes


# In[21]:


# Check the first column

df2.head(1)


# In[22]:


# Convert the column 'ActivityDay' to datetime format

df2.ActivityDay = pd.to_datetime(df2['ActivityDay'])


# In[23]:


# Filter ID 6962181067

df2 = df2.loc[df2['Id'] == 6962181067]


# In[24]:


# Check the shape again

df2.shape


# In[25]:


#This is to avoid Python getting confused before changing the column name 'ActivityDay' to 'Date'

pd.options.mode.chained_assignment = None


# In[26]:


df2.rename(columns = {'ActivityDay' : 'Date'}, inplace = True)


# In[27]:


# Check if the column name has changed

df2.head(1)


# In[28]:


# Now merge the two dataframes together

df1_df2 = pd.merge(df1,df2, on = ['Id','Date'], how = 'inner')


# In[29]:


# Check the data

df1_df2.head(5)


# In[30]:


df1_df2.shape


# In[31]:


# Plot graphs to visualise the data

df1_df2 = df1_df2.loc[df1_df2['Id'] == 6962181067]
df1_df2.plot(x='Date',y='WeightKg')
df1_df2.plot(x='Date',y='Calories')


# In[32]:


# Check the statistics

df1_df2[['Calories','WeightKg']].describe()


# In[ ]:





# In[33]:


df3 = pd.read_csv('C:\\Users\\cenxi\\OneDrive\\Documents\\Google Data Analytics\\Case Study Bellabeat\\Fitabase Data 4.12.16-5.12.16\\minuteMETsNarrow_merged.csv')


# In[34]:


df3.shape


# In[35]:


df3.head(1)


# In[36]:


df3 = df3.loc[df3['Id'] == 6962181067]


# In[37]:


df3.shape


# In[38]:


df3.ActivityMinute = pd.to_datetime(df3['ActivityMinute'])


# In[39]:


df3.dtypes


# In[40]:


df3 = df3.assign(Date=df3.ActivityMinute.dt.date, Time=df3.ActivityMinute.dt.time)


# In[41]:


df3.head(1)


# In[42]:


sorted_df3 = df3.pivot(index='Date',columns='Time')['METs']


# In[43]:


sorted_df3


# In[44]:


sorted_df3['median_METs'] = sorted_df3.median(axis=1)


# In[45]:


sorted_df3


# In[46]:


df3_new = sorted_df3.loc[:, sorted_df3.columns.intersection(['Date','median_METs'])]


# In[47]:


df3_new


# In[48]:


df3_new.shape


# In[49]:


df1_df2_df3 = pd.merge(df1_df2,df3_new, on = ['Date'], how = 'inner')


# In[50]:


df1_df2_df3


# In[51]:


# (MET Value of Activity) x (Body Weight in kg) x (Time in hours) = Calories Burned


# In[52]:


df1_df2_df3['ActiveHours'] = df1_df2_df3['Calories']/(df1_df2_df3['WeightKg']*df1_df2_df3['median_METs'])


# In[53]:


df1_df2_df3


# In[54]:


df1_df2_df3.describe()


# In[ ]:





# In[ ]:





# In[ ]:





# In[55]:


df4 = pd.read_csv('C:\\Users\\cenxi\\OneDrive\\Documents\\Google Data Analytics\\Case Study Bellabeat\\Fitabase Data 4.12.16-5.12.16\\dailyIntensities_merged.csv')


# In[56]:


df4.head(1)


# In[57]:


df4 = df4.loc[df4['Id'] == 6962181067]


# In[58]:


df4 = df4.drop(['SedentaryActiveDistance','LightActiveDistance','ModeratelyActiveDistance','VeryActiveDistance'],axis=1)


# In[59]:


df4['TotalActiveHours'] = (df4['LightlyActiveMinutes']+df4['FairlyActiveMinutes']+df4['VeryActiveMinutes'])/60


# In[60]:


df4.head()


# In[61]:


df4.rename(columns = {'ActivityDay' : 'Date'}, inplace = True)


# In[62]:


df4 = df4.loc[:, df4.columns.intersection(['Date','TotalActiveHours'])]


# In[63]:


df4.head()


# In[64]:


df4.dtypes


# In[65]:


df4.Date = pd.to_datetime(df4['Date'])


# In[66]:


all_df = pd.merge(df1_df2_df3,df4, on = ['Date'], how = 'inner')


# In[67]:


all_df


# In[68]:


all_df.plot(x='Date',y=['ActiveHours','TotalActiveHours'])


# In[69]:


all_df.describe()


# In[ ]:




