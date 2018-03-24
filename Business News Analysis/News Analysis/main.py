import quandl
import math
import numpy as np
from sklearn import preprocessing, cross_validation, svm
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt

from interpolation import interpolate
from normalisation import normalize


df=quandl.get('WIKI/GOOGL', api_key='pYaKjEHyu4Tje_VTzHu6',start_date='2016-12-22',end_date='2018-03-23')

df=interpolate(df,list(df))
df=normalize(df,list(df))

result=df.corr(method='pearson',min_periods=1)

print(result)

result=df.cov()
print(result)
