import quandl
import math
import numpy as np
from sklearn import preprocessing, cross_validation, svm
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt

def normalize(dataframe, cols_to_interpolate):
	
	print(dataframe.shape)
	#dataframe.drop(['2017-03-21','2017-03-22'])
	#dataframe.drop([80:82])

	'''
	plt.figure(2)
	plt.title('Normalized data')
	plt.subplot(2, 1, 1)
	plt.plot(dataframe)
	'''
	dataframe.fillna(dataframe.mean(),inplace=True)
	#dataframe.resample('D')
	cols=list(dataframe)
	for col in cols:
        	preprocessing.normalize(dataframe, axis=0, norm='l2', copy=False)

	print(dataframe.shape)

	'''
	plt.subplot(2,1,2)
	plt.plot(dataframe)

	plt.show()
	''' 
	return dataframe
