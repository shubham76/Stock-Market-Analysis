import numpy as np
import pandas as pd
from sklearn import preprocessing, cross_validation, svm
from sklearn.linear_model import LinearRegression


df=pd.read_csv('TCS_qs.csv')
forecast_out=-1
forecast_col = ['Open', 'High', 'Low', 'Close']
df['ForecastOpen'] = df['Open']

X = np.array(df[['open_score']])
#X = X[:forecast_out]
df.dropna(inplace=True)

y = np.array(df[['ForecastOpen']])
#y=y[:forecast_out]
print len(y)
print len(X)
X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.2,random_state=11)

clf = LinearRegression()
clf.fit(X_train, y_train)
confidence = clf.score(X_test, y_test)*-1
print("Sentimental Method Accuracy for Open Price: ")
print(confidence * 100.0)


X = np.array(df[['close_score']])
y = np.array(df[['Close']])
df.dropna(inplace=True)

print len(y)
print len(X)
X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.2,random_state=15)

clf = LinearRegression()
clf.fit(X_train, y_train)
confidence = clf.score(X_test, y_test)*-1
print("Sentimental Method Accuracy for Close Price: ")
print(confidence * 100.0)

