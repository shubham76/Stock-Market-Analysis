import numpy as np
from sklearn import preprocessing, cross_validation
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
import pandas as pd
import copy
import platform
import sys
forecast_out=-1
df1=pd.read_csv('TCS_qs_NSE.csv')

df1=df1.set_index('Date')

def status_calc(stock, nse, outperformance=0.001):
	return stock - nse >= outperformance


X=df1.drop(['shift_close','p_change'],1)
y=status_calc(df1['PC_close'],df1['p_change'],0.001)

X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.2,random_state=324)
clf=SVC(kernel="rbf")
#clf=RandomForestClassifier(n_estimators=100, random_state=0)
clf.fit(X_train, y_train)
confidence = clf.score(X_test, y_test)
print("Hybrid Method Accuracy for SVM close Price: ")
print(confidence * 100.0)



