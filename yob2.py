#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import matplotlib.pyplot as plt
import os
pd.set_option('display.max_rows',10)


# In[61]:


# .plot(kind='bar', rot=45, stacked=True)
# return res_df[res_df['Name'] in list_names].groupby(['Year']).sum()
path_dir = 'E:/НЕТОЛОГИЯ_КУРСЫ/Профессия Питон/2ч Продвинутый PYTHON/++2.5Data_analysis1/hw_data_analysis1/names/'
begin_year = 1900
end_year = 2000
list_names = ['Ruth','Robert']


# In[152]:


# 1.	Построить график изменения количества имен Ruth и Robert с 1900 по 2000.

list_df = []
for year in range(begin_year,end_year + 1):
    full_path = os.path.join(path_dir,f"yob{year}.txt")
    df = pd.read_csv(full_path, names=['Name', 'Gender', 'Count'], encoding = 'ISO-8859-1')
    df['Year'] = year
    list_df.append(df)
res_df = pd.concat(list_df)    
res_df


# In[131]:


res = res_df[(res_df['Name']=='Ruth') | (res_df['Name']=='Robert')].groupby(['Name', 'Year']).sum()
# res
res.unstack('Name').plot(kind='area', rot=45, stacked=False)


# In[132]:


# 2.	Построить столбчатую диаграмму по количеству их имен с 1900 по 2000 
# с 5-летними промежутками (1900, 1905, 1910, …, 1995, 2000).

list_df = []
for year in range(begin_year,end_year + 1, 5):
    full_path = os.path.join(path_dir,f"yob{year}.txt")
    df = pd.read_csv(full_path, names=['Name', 'Gender', 'Count'], encoding = 'ISO-8859-1')
    df['Year'] = year
    list_df.append(df)
res_df2 = pd.concat(list_df)    
res_df2


# In[133]:


res = res_df2[['Year','Count']].groupby(['Year']).count()
# res
res.unstack().plot(kind='bar')
# plt.barh(res['Name'],res['Count'])


# In[134]:


# 3.	Построить круговую диаграмму по количеству употреблений для ТОП-10 популярных имен, начинающихся на R, за 1950 год.

year = 1950
full_path = os.path.join(path_dir,f"yob{year}.txt")
df = pd.read_csv(full_path, names=['Name', 'Gender', 'Count'], encoding = 'ISO-8859-1')
df_top10_r = df[df['Name'].str.contains("^R")].groupby(['Name']).sum().sort_values('Count', ascending=0).head(10)
# df_top10_r
# df_top10_r.plot(kind='pie', y='Count')
plt.pie(df_top10_r)


# In[221]:


# 4.	Построить точечную диаграмму по количеству согласных букв в именах и частоте употребления за 100 лет.
# Т.е. необходимо сложить всю статистику с 1900 до 2000,
# сгруппировать по именам, посчитать количество согласных букв в каждом имени
# и вывести на график отношение "Количество согласных букв в имени" : "Количество употреблений".
import seaborn as sns

def consonant(str):
    return len(str) - sum(1 for x in str.lower() if x in 'aeiou')

list_df = []
for year in range(begin_year,end_year + 1):
    full_path = os.path.join(path_dir,f"yob{year}.txt")
    df = pd.read_csv(full_path, names=['Name', 'Gender', 'Count'], encoding = 'ISO-8859-1')
    list_df.append(df)
    
res_df = pd.concat(list_df)    
res_df['Length'] = res_df['Name'].map(consonant)
res = res_df.groupby(['Length']).sum()
# .reset_index(level='Length', drop=True)
# .sort_values('Count', ascending=0)
res


# In[219]:


plt.scatter(res['Count'], res['Length'])


# In[ ]:




