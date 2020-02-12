#!/usr/bin/env python
# coding: utf-8

# In[24]:


import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
#importing matplotlib and seaborn libraries for visualization
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns
sns.set_style("darkgrid")
import plotly.express as px


# In[5]:


#reading csv here
corona_data = pd.read_csv("Datasets/corona-virus/2019_nCoV_data.csv")


# In[2]:


#showing data in the form of pandas DataFrame
corona_data


# In[72]:


#checking for the null values
corona_data.isnull().sum()


# In[73]:


#replacing null values
corona_data = corona_data.fillna({'Province/State':'Qinghai'})


# In[6]:


#we dont need Sno and Last Update so we are dropping those columns

corona_data.drop('Sno',inplace=True,axis=1)
corona_data.drop('Last Update',inplace=True,axis=1)


# In[8]:


#printing the information about the Dataframe 
corona_data.info()


# In[9]:


#describing the statistical measures of the Dataset
corona_data.describe()


# In[74]:


Confirmed_cases=corona_data['Confirmed'].sum()
print(Confirmed_cases)


# In[75]:


death_cases=corona_data['Deaths'].sum()
print(death_cases)


# In[76]:


recovery_cases=corona_data['Recovered'].sum()
print(recovery_cases)


# In[11]:


#Changing datetime into date
corona_data.Date=corona_data.Date.apply(pd.to_datetime)
corona_data.Date=corona_data["Date"].dt.strftime('%m/%d/%Y')

corona_data.head()


# In[16]:


#grouping the data with respect to date for better understanding

corona_data_datewise = corona_data.groupby(["Date"],as_index=False)['Confirmed','Deaths','Recovered'].sum()


# In[17]:


corona_data_datewise


# In[19]:


#Adding number of days to explore the epidemic with respect to time
corona_data_datewise['Days']=np.arange(1,len(corona_data_datewise)+1)
corona_data_datewise


# In[23]:


#visualization of the corona virus deaths across the world during days 
fig=px.line(corona_data_datewise,x="Days",y="Deaths",range_y=[1,1100])
fig.show()


# With the Passage of days we can see that deaths are also increasing

# In[77]:


#plotting the relationship between Confirmed,deaths and recovered cases

plt.figure(figsize=(20,10))
plt.yticks(fontsize=20)
plt.xticks(fontsize=20)
plt.xlabel("Days",fontsize=20)
plt.ylabel("Corona Cases",fontsize=20)
plt.plot(corona_data_datewise.Days,corona_data_datewise.Confirmed,marker='o',markersize=10,color='blue',linewidth=4)
plt.plot(corona_data_datewise.Days,corona_data_datewise.Recovered,marker='o',markersize=10,color='green',linewidth=4)
plt.plot(corona_data_datewise.Days,corona_data_datewise.Deaths,marker='o',markersize=10,color='red',linewidth=4)
plt.title("Corona Virus trend",fontsize=20)
plt.legend(labels=['Confirmed','Recovered','Dead'],fontsize=15)
plt.show()


# In[33]:


#lets group the data country wise and see the effect on each country
corona_data_country = corona_data.groupby('Country',as_index=False)["Confirmed","Deaths","Recovered"].sum()
corona_data_country


# In[64]:


#Filtering data based on date
virus_data_latest=corona_data[(corona_data["Date"]==corona_data["Date"].max())]
virus_data_latest


# In[44]:


#Visualisation of death cases across countries using a line plot
fig=px.line(corona_data_country,x="Country",y="Deaths",range_y=[1,8000])
fig.show()


# In[45]:


#Visualisation of death cases across countries using a line plot
fig=px.bar(corona_data_country,x="Country",y="Deaths")
fig.show()


# As we can see China has the most cases so lets go into details of china

# In[52]:


virus_province = corona_data.groupby(['Province/State']).agg({'Confirmed': 'sum',
                                                'Deaths': 'sum',
                                                'Recovered': 'sum',
                                                }).reset_index()
virus_province


# In[67]:


#lets get  the information by filtering virus_data_latest
virus_data_china=virus_data_latest[virus_data_latest.Country=="Mainland China"].groupby("Province/State",as_index=False)["Confirmed","Deaths","Recovered"].sum()
virus_data_china


# In[81]:


fig = px.bar(virus_data_china, y = 'Province/State', x = 'Confirmed',orientation = 'h', width = 800, height = 600,color='Province/State'  )
fig.show()


# In[82]:


fig = px.bar(virus_data_china, y = 'Province/State', x = 'Deaths',orientation = 'h', width = 800, height = 600,color='Province/State'  )
fig.show()


# In[80]:


fig = px.bar(virus_data_china, y = 'Province/State', x = 'Recovered',orientation = 'h', width = 800, height = 600,color='Province/State' )
fig.show()


# In[78]:


#lets get data based on hubei from main data frame
virus_Hubei=corona_data[corona_data["Province/State"]=="Hubei"]
virus_Hubei


# In[79]:


#deaths in hubei day to day
fig=px.bar(virus_Hubei,x="Date",y="Deaths",color="Deaths")
fig.show()


# In[ ]:




