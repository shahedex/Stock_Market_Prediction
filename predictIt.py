import pymysql
import re
import pandas as pd
import numpy as np
import math
import datetime

# Machine Learning
from sklearn import preprocessing, model_selection, svm
from sklearn.linear_model import LinearRegression

#Visualization
import matplotlib
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings(action="ignore", module="scipy", message="^internal gelsd")

conn = pymysql.connect(host='localhost', user='root', passwd='hellothere', db='stk')
cur = conn.cursor()

stockMarket="";


dates=[]
ltp=[]
hig = []
low = []
openp = []
closep = []
volume = []
benefit=[]
benefitPrice=[]








def check():
	print("sefsdf")
	# show_plot(dates,prices)
	# predicted_price, coefficient, constant = predict_price(dates,prices,29)

#############Data collect###############

def convertString(s):
	return re.sub('[,]','',s)
def getData(tradeCode):	
	dates.clear()
	ltp.clear()
	hig.clear()
	low.clear()
	openp.clear()
	closep.clear()
	volume.clear()
	# print("okkkkdkk")
	q1 = "select `DATE`,`LTP*`,`HIGH`,`LOW`,`OPENP*`,`CLOSEP*`,`VOLUME` from %s WHERE `TRADING CODE`='%s' ORDER BY `DATE`"
	# print("okkkkdkk")
	try:
		# print("okkkkdkk")
		cur.execute(q1 % (stockMarket ,tradeCode))		
		results = cur.fetchall()
		for row in results:
			dates.append(row[0])
			ltp.append(float(convertString(row[1]))+.000001)
			hig.append(float(convertString(row[2]))+.000001)
			low.append(float(convertString(row[3]))+.000001)
			openp.append(float(convertString(row[4]))+.000001)
			closep.append(float(convertString(row[5]))+.000001)
			volume.append(int(convertString(row[6])))
	except:
		print("Error to fetch dataa")

def generateDf(tradeCode):
	data = {'LTP': ltp,'HIGH': hig, 'LOW':low,'OPENP':openp,'CLOSEP':closep,'VOLUME':volume,'DATE':dates}
	df = pd.DataFrame(data)
	df['DATE'] = pd.to_datetime(df['DATE'])
	df= df.set_index('DATE')
	# print(df)
	#df= df[['CLOSEP','HIGH',  'LOW',  'LTP', 'OPENP','VOLUME']]
	# print("opu")
	# try:
	# 	df['new']=df['HIGH']-df['LOW']
	# except Exception as ex:
	# 	print(ex)
	# print(df['new'])
	# df['HL_PCT'] = values;
	df['HL_PCT'] = (df['HIGH'] - df['LOW'])/(df['LOW']*100)
	df['PCT_CHNG'] = (df['LTP'] - df['OPENP'])/(df['OPENP']*100)
	# print(df)
	df = df[['LTP', 'HL_PCT', 'PCT_CHNG', 'VOLUME']]
	# print(df)
	##########################################learning##########################################
	# Visualization

	# df['LTP'].plot(figsize=(15,6), color="green")
	# plt.legend(loc=4)
	# plt.xlabel('Date')
	# plt.ylabel('Price')
	# plt.show()

	# df['HL_PCT'].plot(figsize=(15,6), color="red")
	# plt.xlabel('Date')
	# plt.ylabel('High Low Percentage')
	# plt.show()

	# df['PCT_CHNG'].plot(figsize=(15,6), color="blue")
	# plt.xlabel('Date')
	# plt.ylabel('Percent Change')
	# plt.show()

	# pick a forecast column
	forecast_col = 'LTP'

	# Chosing 30 days as number of forecast days
	forecast_out = int(1)
	# 	print('length =',len(df), "and forecast_out =", forecast_out)

	# Creating label by shifting 'Adj. Close' according to 'forecast_out'
	df['label'] = df[forecast_col].shift(-forecast_out)
	# print(df.head(2))
	# print('\n')
	# If we look at the tail, it consists of n(=forecast_out) rows with NAN in Label column 
	# print(df.tail(2))
	# Define features Matrix X by excluding the label column which we just created 
	X = np.array(df.drop(['label'], 1))

	# Using a feature in sklearn, preposessing to scale features
	X = preprocessing.scale(X)
	# print(X[1,:])

	# X contains last 'n= forecast_out' rows for which we don't have label data
	# Put those rows in different Matrix X_forecast_out by X_forecast_out = X[end-forecast_out:end]

	X_forecast_out = X[-forecast_out:]
	X = X[:-forecast_out]
	# 	print ("Length of X_forecast_out:", len(X_forecast_out), "& Length of X :", len(X))

	# Similarly Define Label vector y for the data we have prediction for
	# A good test is to make sure length of X and y are identical
	y = np.array(df['label'])
	y = y[:-forecast_out]
	# 	print('Length of y: ',len(y))
	
	###########################regression####################
	# Cross validation (split into test and train data)
	# test_size = 0.2 ==> 20% data is test data
	X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size = 0.2)

	# print('length of X_train and x_test: ', len(X_train), len(X_test))
	# Train
	clf = LinearRegression()
	clf.fit(X_train,y_train)
	# Test
	accuracy = clf.score(X_test, y_test)
	# 	print("Accuracy of Linear Regression: ", accuracy)
	# Predict using our Model
	forecast_prediction = clf.predict(X_forecast_out)
	#print(forecast_prediction)
	if(forecast_prediction[0]>ltp[-1]+.3):
		benefit.append(tradeCode)
		benefitPrice.append(forecast_prediction[0]-(ltp[-1]+.3))

	# # Plotting data
	# df.dropna(inplace=True)
	# df['forecast'] = np.nan
	# last_date = df.iloc[-1].name
	# last_unix = last_date.timestamp()
	# one_day = 86400
	# next_unix = last_unix + one_day

	# for i in forecast_prediction:
	#     next_date = datetime.datetime.fromtimestamp(next_unix)
	#     next_unix += 86400
	#     df.loc[next_date] = [np.nan for _ in range(len(df.columns)-1)]+[i]
	# df['LTP'].plot(figsize=(15,6), color="green")
	# df['forecast'].plot(figsize=(15,6), color="orange")
	# plt.legend(loc=4)
	# plt.xlabel('Date')
	# plt.ylabel('Price')
	# plt.show()
	# wsdf=input("Give the shit: ")




def gen():
	q1 = "select DISTINCT `TRADING CODE` from %s";
	try:
		cur.execute(q1 %stockMarket )
		results = cur.fetchall()		
		for row in results:
			#print(row[0],end='')
			# print("okkkkkk")
			getData(row[0])

			generateDf(row[0])
			# check()
	except:
		print("Error to fetch data")


if __name__ == '__main__':
	value=int(input("Press 1 for DSE and for CSE press anything else: "))
	#value=0
	if(value==1):
		stockMarket="`dsedayendsumm`"
	else:
		stockMarket="`csedayendsumm`"


	gen()
	
	res = {}
	if(value==1):
		query = "SELECT DISTINCT `TRADING CODE` FROM dsedayendsumm"
		ltpquery = "SELECT `LTP*` FROM dsedayendsumm WHERE `TRADING CODE`='%s' ORDER BY `DATE`"
		try:
			cur.execute(query)
			resultsback = cur.fetchall()
			for result in resultsback:
				cur.execute(ltpquery %(result[0]))
				num = cur.fetchone()[0]
				num = num.replace(',','')
				res[result[0]] = float(num)
			cur.execute("DELETE FROM predicted")
		except Exception as e:
			print(e)
	print("Stocks that may return benefit: \n");
	for x,y in zip(benefit,benefitPrice):
		print (x,y)
		if(value==1):
			try:
				cur.execute("INSERT INTO `predicted`(`name`, `value`,`price`) VALUES ('%s',%s,%s)"%(x,y,res[x]))
				conn.commit()
			except KeyError as e:
				print(e)
		else:
			cur.execute("INSERT INTO `csepredicted`(`name`, `value`) VALUES ('%s',%s)"%(x,y))
			conn.commit()
	cur.close()
	conn.close()
	# print(benefit)
	# print(benefitPrice)

	
