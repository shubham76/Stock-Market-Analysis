
import numpy as np
from sklearn import preprocessing, cross_validation
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVC
import pandas as pd
import matplotlib.pyplot as plt
#%matplotlib inline

import copy
import platform
import sys
forecast_out=-1
df=pd.read_csv('TCS_qs.csv')
forecast_col = ['Open',  'High',  'Low',  'Close']
df.fillna(value=-99999, inplace=True)
df['ForecastOpen'] = df[forecast_col[0]].shift(forecast_out)
df['ForecastClose'] = df[forecast_col[3]].shift(forecast_out)

#print(df)
df=df[:forecast_out]
X=df[['Open', 'High', 'Low', 'Close', 'open_score', 'close_score','PC_open','PC_close']]
#X=df.drop(['ForecastOpen','ForecastClose','#''],1)
y=df['ForecastOpen']

X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.2,random_state=324)
clf = LinearRegression()
clf.fit(X_train, y_train)
confidence = clf.score(X_test, y_test)


predictions=clf.predict(X_test)
plt.subplot(2,1,1)
plt.scatter(X_test['Open'],y_test,color="black")
plt.plot(X_test['Open'],predictions,color="blue",linewidth=3)
plt.show()

print("Hybrid Method Accuracy for Open Price: ")
print(confidence * 100.0)

'''
plt.scatter(X['Open'],y,color="m",marker="o",s=30)
plt.plot()
plt.show()
'''

z=df['ForecastClose']

X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, z, test_size=0.2,random_state=324)
clf = LinearRegression()
clf.fit(X_train, y_train)
confidence = clf.score(X_test, y_test)
print("Hybrid Method Accuracy for Close Price: ")
print(confidence * 100.0)

plt.subplot(2,1,2)
plt.scatter(X_test.index,y_test,color="black")
plt.plot(X_test.index,predictions,color="red",linewidth=3)
plt.show()
