#!/usr/bin/env python
# coding: utf-8

# In[80]:


import pandas as pd


# In[81]:


df=pd.read_csv("Bus_dataset.csv")


# In[82]:


#df.head()


# In[83]:


#df.tail()


# In[84]:


#df.isnull().sum()


# In[85]:


#df.columns


# In[101]:


bus_stand_name=input("Enter bus stand name:- ")
user_time_zone=input("Enter Your Time:- ").replace(":","")
start_time=[]
for i in df.index:
    a=df.loc[i,"Bus Stand Names"]
    if a==bus_stand_name:
        start_time.append(df.iloc[i])


# In[102]:


temp=[]
for i in start_time:
    for j in range(1,len(i)):
        temp.append(i[j])
start_time=temp


# In[103]:


print("Bus Timings are:- ")
for i in temp:
    a=i
    if int(a.replace(":",""))>=int(user_time_zone):
        print(i)


# In[104]:


Select_time=input("Enter Your bus starting time:- ").split(":")
Ending_stop=input("Enter Your Destination Bus Stop:- ")

end_time=[]
for i in df.index:
    a=df.loc[i,"Bus Stand Names"]
    if a==Ending_stop:
        end_time.append(df.iloc[i])
    
temp=[]
for i in end_time:
    for j in range(1,len(i)):
        temp.append(i[j])
end_time=temp


# In[108]:


col_val=start_time.index(":".join(Select_time))
start=start_time[col_val].split(":")
end=end_time[col_val].split(":")
est_time=[]
for i in range(2):
    est_time.append(int(end[i])-int(start[i]))
print(est_time[0],"hrs and ",est_time[1],"min")


# In[ ]:




