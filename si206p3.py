import requests
import unittest
import sqlite3
import json
import os
import matplotlib.pyplot as plt
import seaborn as sns

#SI206 Final Project
#Names: Grace Ho, Aaron Huang


#Gather the data and save it to a single database 
def setUpDatabase(db_name):
	path = os.path.dirname(os.path.abspath(__file__))
	conn = sqlite3.connect(path+'/'+db_name)
	cur = conn.cursor()
	return cur, conn

def coingecko(currency):
	resp = requests.get('https://api.coingecko.com/api/v3/simple/price', params = { 
		"ids" : 'bitcoin',
		"vs_currencies" : currency 
		})
	data = resp.json()
	return data


def rates(base, symbol):
	resp = requests.get('https://api.ratesapi.io/api/latest', params = {
	   "base" : base,
	   "symbols" : symbol

	})
	data = resp.json()
	return data

def marketdata(currency):
	resp = requests.get('https://api.coingecko.com/api/v3/coins/bitcoin/market_chart', params = {
		'vs_currency' : currency,
		'days' : '7'
	})
	data = resp.json()
	d = {}
	for key in data:
		for num, item in enumerate(data[key]):
			lst = []
			if num in d:
				lst = d[num]
			lst.append(item[1])
			d[num] = lst
	return d
	
	
def database(data):
	cur, conn = setUpDatabase('bitcoin.db')
	#create table
	cur.execute("DROP TABLE IF EXISTS bitcoin")
	cur.execute("CREATE TABLE bitcoin ('day' INTEGER PRIMARY KEY, 'prices' REAL, 'market_cap' REAL, 'total_volume' REAL)")
	#insert data into table
	for item in data:
		day = item
		prices = data[item][0]
		market_cap = data[item][1]
		total_volume = data[item][2]
		cur.execute('INSERT INTO bitcoin (day, prices, market_cap, total_volume) VALUES({}, {}, {}, {})'.format(day, prices, market_cap, total_volume))
	conn.commit()

#Process the data
#Calculate from database.(20) Do at least one database join to select data.(20) Write out calculated data to a file as text.(10)

def calculate():
	cur, conn = setUpDatabase('bitcoin.db')
	avg = cur.execute('SELECT total_volume FROM bitcoin').fetchall()
	averages = []
	count = 0
	total = 0
	for num in avg:
		if count >= 7:
			averages.append(float(total / 7))
			count = 0
			total = 0
		total += num[0]
		count +=1 
	conn.commit()
	return averages

def profits():
	cur, conn = setUpDatabase('bitcoin.db')
	avg = cur.execute('SELECT prices FROM bitcoin').fetchall()
	averages = []
	count = 0
	total = 0
	for num in avg:
		if count >= 7:
			averages.append(float(total / 7))
			count = 0
			total = 0
		total += num[0]
		count +=1 
	conn.commit()
	return averages

#Visualize data
def line():
	y = calculate()
	x = range(len(y))
	x_pos = [i for i, _ in enumerate(x)]
	plt.plot(y, color = 'b')
	plt.xlabel('Week Numbers')
	plt.ylabel('24hr Volume Averages')
	plt.title('Weekly Averages of 24hr Trading Volumes')
	plt.xticks(x_pos, x)
	plt.show()
	


def bar():
	y = profits()
	x = range(len(y))
	x_pos = [i for i, _ in enumerate(x)]
	plt.bar(x_pos, y, color ='purple')
	plt.xlabel('Week Numbers')
	plt.ylabel('Average Price of Bitcoin')
	plt.title('Weekly Average Price of Bitcoin')
	plt.xticks(x_pos, x)
	plt.show()




data = marketdata("usd")
coingecko("ngn")
coingecko('usd')
rates("USD", "RUB")
database(data)
bar()
line()
print("The conversion rate of Nigerian Naira to Bitcoin is ")
print(coingecko('ngn')['bitcoin']['ngn'])
print("Nairas for 1 Bitcoin")
print()
print("The conversion rate of Bitcoin to American Dollars is 1 Bitcoin for ")
print(coingecko('usd')['bitcoin']['usd'])
print("American Dollars")
print()
print("The conversion rate of American Dollars to Russian Rubles is 1 American Dollar for")
print(rates('USD', 'RUB')['rates']['RUB'])
print("Russian Rubles")
print()
print("5,710,000,000 billion Nigerian Naira is equal to ")
print(str(5710000000/(coingecko('ngn')['bitcoin']['ngn'])))
print("Bitcoins")
print()
print(str(5710000000/(coingecko('ngn')['bitcoin']['ngn'])))
print("Bitcoins is equal to ")
print(str((5710000000/(coingecko('ngn')['bitcoin']['ngn']))*(coingecko('usd')['bitcoin']['usd'])))
print("American Dollars")
print()
print(str((5710000000/(coingecko('ngn')['bitcoin']['ngn']))*(coingecko('usd')['bitcoin']['usd'])))
print("American Dollars is equal to ")
print(str((5710000000/(coingecko('ngn')['bitcoin']['ngn']))*(coingecko('usd')['bitcoin']['usd'])*(rates('USD', 'RUB')['rates']['RUB'])))
print("Russian Rubles")
print()
print("The amount owed to me is ")
print(str((5710000000/(coingecko('ngn')['bitcoin']['ngn']))*(coingecko('usd')['bitcoin']['usd'])*(0.2)))
print("American Dollars")
print()
print("The amount paid to the Russian Space Authorities is")
print(str((5710000000/(coingecko('ngn')['bitcoin']['ngn']))*(coingecko('usd')['bitcoin']['usd'])*(rates('USD', 'RUB')['rates']['RUB'])*(0.2)))
print("Russian Rubles")


