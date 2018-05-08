import numpy as np
from sklearn import preprocessing, cross_validation
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVC
import pandas as pd
import copy
import platform
import sys
from interpolation import interpolate
from normalisation import normalize

forecast_out=-1
df1=pd.read_csv('TCS_qs.csv')
df2=pd.read_csv('NSE.csv')
df1=df1.set_index('Date')
df2=df2.set_index('Date')

company_id="TCS"
df2=interpolate(df2,list(df2))

'''
list2=list(df2)
list2=list2.remove('Date')
print(list2)
'''

df2=normalize(df2,list(df2))
#df2.reset_index()
df2['shift_close']=df2['Close'].shift(-1)
df2.dropna()
df2['shift_close']=df2['shift_close'].astype(float)
df2['Close']=df2['Close'].astype(float)
df2['p_change']=(df2['shift_close']-df2['Close'])/(df2['Close'])	

print(list(df2))

df3 = pd.DataFrame(index=df2.index)
df3['p_change']=df2['p_change']
#df3=df3.set_index('Date')
print(list(df3))

df3.dropna(inplace=True)

df4= df1.merge(df3,how="inner",left_index=True,right_index=True)
df4=df4.sort_index()
df4.to_csv(company_id+'_qs_NSE.csv',encoding='utf-8',sep=',')
print(df4)

