import pandas as pd
from datetime import datetime
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

def data_preprocessing():
	print('Preprocessing the data')
	data=pd.read_csv('sphist.csv')

	data['Date']=pd.to_datetime(data['Date'])
	data=data.sort_values('Date',ascending=True)

	'''calculating indicators'''
	data['last_5_avg']=data['Close'].rolling(5,min_periods=1).mean()
	data['last_30_avg']=data['Close'].rolling(30,min_periods=1).mean()
	data['last_365_avg']=data['Close'].rolling(365,min_periods=1).mean()

	data[['last_5_avg','last_30_avg','last_365_avg']]=data[['last_5_avg','last_30_avg','last_365_avg']].shift(periods=1,axis=0)
		
	'''data cleaning'''
	data=data[data['Date']>datetime(year=1951,month=1,day=2)]
	data=data.dropna(axis=0)

	'''Generating testing and training data sets'''
	train=data[data['Date']<datetime(year=2013,month=1,day=1)]
	test=data[data['Date']>=datetime(year=2013,month=1,day=1)]
	print('Data Preprocessed')
	return train,test

def model_training(train,test,features,target):
	'''Trains the model, predicts the values for the test data and returns the accuracy'''
	lr=LinearRegression()
	lr.fit(train[features],train[target])
	predicted=lr.predict(test[features])
	error=mean_absolute_error(test[target],predicted)
	diff=test[target]-predicted

	return error

if __name__=='__main__':
	train,test=data_preprocessing()
	error=model_training(train,test,['last_5_avg','last_30_avg','last_365_avg'],'Close')
	print('Mean absolute error:',error)