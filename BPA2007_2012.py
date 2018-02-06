# -*- coding: utf-8 -*-
"""
Created on Fri Feb 02 11:51:10 2018

@author: jehill17
"""

"this code is to create demand predictions for BPA"

import matplotlib.pyplot as plt
import pandas as pd 
from pandas.plotting import autocorrelation_plot
import numpy as np
import scipy.stats as stats

# load data, specify sheet and number of rows to skip
df_data1 = pd.read_excel('TotalWindLoad_5Min_07.xls',usecols=[2,3,5])
df_data1b = pd.read_excel('TotalWindLoad_5Min_07.xls',usecols=[10,11,13])
df_data2 = pd.read_excel('TotalWindLoad_5Min_08.xls', skiprows=16, usecols=[2,4,6])
df_data2b = pd.read_excel('TotalWindLoad_5Min_08.xls', skiprows=16, usecols=[11,13,15])
df_data3 = pd.read_excel('TotalWindLoad_5Min_09.xls', skiprows=16,usecols=[3,4,6])
df_data3b = pd.read_excel('TotalWindLoad_5Min_09.xls', skiprows=16,usecols=[12,13,15])
df_data4 = pd.read_excel('TotalWindLoad_5Min_10.xls', skiprows=16,usecols=[3,4,6])
df_data4b = pd.read_excel('TotalWindLoad_5Min_10.xls', skiprows=16,usecols=[12,13,15])
df_data5 = pd.read_excel('TotalWindLoad_5Min_11.xls', skiprows=18,usecols=[2,3,5])
df_data5b = pd.read_excel('TotalWindLoad_5Min_11.xls', sheetname=1, skiprows=18,usecols=[2,3,5])
df_data6 = pd.read_excel('TotalWindLoad_5Min_12.xls', skiprows=18,usecols=[2,3,5])
df_data6b = pd.read_excel('TotalWindLoad_5Min_12.xls', sheetname=1, skiprows=18,usecols=[2,3,5])

#label column names
df_data1.columns = ['wind07a','demand07a','thermal07a']
df_data1b.columns = ['wind07b','demand07b','thermal07b']
df_data2.columns = ['wind08a','demand08a','thermal08a']
df_data2b.columns = ['wind08b','demand08b','thermal08b']
df_data3.columns = ['wind09a','demand09a','thermal09a']
df_data3b.columns = ['wind09b','demand09b','thermal09b']
df_data4.columns = ['wind10a','demand10a','thermal10a']
df_data4b.columns = ['wind10b','demand10b','thermal10b']
df_data5.columns = ['wind11a','demand11a','thermal11a']
df_data5b.columns = ['wind11b','demand11b','thermal11b'] #the 2011 & 2012 spreadsheets were divided into 2 sheets - jan-jun and jul-dec
df_data6.columns = ['wind12a','demand12a','thermal12a']
df_data6b.columns = ['wind12b','demand12b','thermal12b']

#convert all to float64, for some reason 'thermal' is type object

data2007 = df_data1.convert_objects(convert_numeric=True)
data2007b = df_data1b.convert_objects(convert_numeric=True)
data2008 = df_data2.convert_objects(convert_numeric=True)
data2008b = df_data2b.convert_objects(convert_numeric=True)
data2009 = df_data3.convert_objects(convert_numeric=True)
data2009b = df_data3b.convert_objects(convert_numeric=True)
data2010 = df_data4.convert_objects(convert_numeric=True)
data2010b = df_data4b.convert_objects(convert_numeric=True)


##remove NaN values
#data2007 = data2007.dropna()
#data2007b = data2007b.dropna()
#data2008 = data2008.dropna()
#data2008 = data2008b.dropna()
#data2009 = data2009.dropna()
#data2009 = data2009b.dropna()
#data2010 = data2010.dropna()
#data2010b = data2010b.dropna()
#data2011 = df_data5.dropna()
#data2011b = df_data5b.dropna()
#data2012 = df_data6.dropna()
#data2012b = df_data6b.dropna()
#convert each dataframe to Matrix
data2007 = data2007.as_matrix()
data2007b = data2007b.as_matrix()
data2008 = data2008.as_matrix()
data2008 = data2008b.as_matrix()
data2009 = data2009.as_matrix()
data2009 = data2009b.as_matrix()
data2010 = data2010.as_matrix()
data2010b = data2010b.as_matrix()
data2011 = df_data5.as_matrix()
data2011b = df_data5b.as_matrix()
data2012 = df_data6.as_matrix()
data2012b = df_data6b.as_matrix()
#
#combine all years
allyears = np.vstack((data2007,data2007b,data2008,data2008b,data2009,data2009b,data2010,data2010b,data2011,data2011b,data2012,data2012b))

#separate into categories
wind = allyears[:,0]
demand = allyears[:,1]
thermal = allyears[:,2]

#aggregate 5-min intervals into hourly data
#wind first



n = int(len(wind)/12)


##aggregating 5-min data into hourly data
#hourly_wind = np.mean(wind.reshape(-1,12),1)
#
#plt.figure()
###plt.plot(hourly_wind)
#
#hourly_demand = np.mean(demand.reshape(-1,12),1)
#
#hourly_thermal = np.mean(thermal.reshape(-1,12),1)

windhourly = []

for i in range(0,n):
    
    value = np.mean(wind[i*12:(i+1)*12])
    windhourly.append(value)
    
    
demandhourly = []

for i in range(0,n):
    
    value = np.mean(demand[i*12:(i+1)*12])
    demandhourly.append(value)
    
thermalhourly = []

for i in range(0,n):
    
    value = np.mean(thermal[i*12:(i+1)*12])
    thermalhourly.append(value)
    




##average hourly profile

avg_hourly = np.zeros(())






    
    
    
        
        

##    
##    
##    
##    
##
##
##
##
##
##
##
