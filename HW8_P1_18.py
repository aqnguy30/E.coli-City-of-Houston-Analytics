#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 14:00:36 2020

@author: anhnguyen
"""
#import libraries
import pandas as pd
import numpy as np
import seaborn as sn
import matplotlib.pyplot as plt

#read-in the data
df = pd.read_excel("Ecoli Data.xlsx")

#check for missing data
df_missing = df.isna()
#number of missing values per feature
missing_values = df_missing.sum()
#percentage of missing values per feature using mean
percent_missing = df_missing.mean()

#check inconsistency for each needed feature
inc_eco = df['E.coli'].value_counts(dropna=False)
#print(inc_eco)
inc_dat = df['Date Collected'].value_counts(dropna=False)
#print(inc_dat)

#drop missing values in 'E.coli' column since they has very small impact
df['E.coli'].dropna(how='all')

#modify date to the correct format
df['Date Collected'] = pd.to_datetime(df['Date Collected'])
#compute and display average amount of E.coli per year in Houston waterways 
df1 = df.groupby(df['Date Collected'].dt.year)['E.coli'].mean().reset_index()
print("Average amount of E.coli per year in Houston waterways:")
print(df1)
#plot the bar graph
ax1 = df1.plot.bar(x='Date Collected', y='E.coli', rot=0, title='Bar graph of x-axis: years and y-axis: E.coli amount')
#for p in ax.patches:
#    ax.annotate(str(p.get_height()), (p.get_x() * 1.005, p.get_height() * 1.005))

#compute and display average amount of E.coli per month in Houston waterways
df2 = df.groupby(df['Date Collected'].dt.month)['E.coli'].mean().reset_index()
print("Average amount of E.coli per month in numeric in Houston waterways:")
print(df2)
#plot the bar graph by numeric month
ax2 = df2.plot.bar(x='Date Collected', y='E.coli', rot=0, title='Bar graph of x-axis: numeric months and y-axis: E.coli amount')

#2nd method to compute and display average amount of E.coli per month in Houston waterways
df['month'] = pd.DatetimeIndex(df['Date Collected']).month
date_01 = df.loc[df['month'] == 1]
date_02 = df.loc[df['month'] == 2]
date_03 = df.loc[df['month'] == 3]
date_04 = df.loc[df['month'] == 4]
date_05 = df.loc[df['month'] == 5]
date_06 = df.loc[df['month'] == 6]
date_07 = df.loc[df['month'] == 7]
date_08 = df.loc[df['month'] == 8]
date_09 = df.loc[df['month'] == 9]
date_10 = df.loc[df['month'] == 10]
date_11= df.loc[df['month'] == 11]
date_12= df.loc[df['month'] == 12]
mean_01= date_01['E.coli'].mean()
mean_02= date_02['E.coli'].mean()
mean_03= date_03['E.coli'].mean()
mean_04= date_04['E.coli'].mean()
mean_05= date_05['E.coli'].mean()
mean_06= date_06['E.coli'].mean()
mean_07= date_07['E.coli'].mean()
mean_08= date_08['E.coli'].mean()
mean_09= date_09['E.coli'].mean()
mean_10= date_10['E.coli'].mean()
mean_11= date_11['E.coli'].mean()
mean_12= date_12['E.coli'].mean()
#display the result
print('The average amount of E.coli per month in Houston waterways from January to December, respectively:', round(mean_01, 3), round(mean_02,3), round(mean_03,3), round(mean_04,3), round(mean_05,3), round(mean_06,3), round(mean_07,3), round(mean_08, 3), round(mean_09,3), round(mean_10,3), round(mean_11,3), round(mean_12,3))
#create x and y of the bar graph by normal month
x = ('Jan',"Feb", "Mar", 'Ap', 'May', 'June','July','Aug','Sep','Oct','Nov','Dec')
y = [mean_01,mean_02,mean_03,mean_04,mean_05,mean_06,mean_07,mean_08,mean_09,mean_10,mean_11,mean_12]
#plot the bar graph by normal month
plt.figure()
plt.bar(x,y)
plt.title("Bar graph of x-axis: normal months and y-axis: E.coli amount")
plt.show()

#initilize a new data frame as selecting only E.coli and chemical factors 
df3 = df[['E.coli','Dissolved Oxygen','PH','Specific Conductance','Salinity','Ammonia Nitrogen','Nitrate Nitrogen','Nitrogen','Phosphorous','Chloride','Sulfate']]     
#check for missing values and inconsistency for each feature       
df3_missing = df3.isna()
missing_values1 = df3_missing.sum()
#fill missing values by feature mean (we cannot drop all because they impact the majority of rows) 
df3.fillna(df3.mean())
#compute and display correlation matrix of df3
corr = df3.corr()
print('Correlation matrix between E.coli and chemical factors:') 
print(corr)
#compute and display correlations between E.coli and chemical factors 
corr1 = df3.corr()['E.coli']
print('Correlations between E.coli and chemical factors:') 
print(corr1)
#plot heatmap of the correlation matrix as extra
plt.figure()
sn.heatmap(corr, annot=True)
plt.show()