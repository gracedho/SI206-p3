from bs4 import BeautifulSoup
import requests
import unittest
import sqlite3
import json
import os
import matplotlib.pyplot as plt
import seaborn as sns

#SI206 Final Project
#Names: Grace Ho, Aaron Huang


#Gather the data and save it to a single database :)
def setUpDatabase(db_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+db_name)
    cur = conn.cursor()
    return cur, conn

#return the data in a dictionary or json

def coingecko(currency):
    resp = requests.get('https://api.coingecko.com/api/v3/simple/price', params = { 
        "ids" : 'bitcoin',
        "vs_currencies" : currency 
        })
    data = resp.json()
    print(data)
    return data

#bitcoin = id
#vs currency = usd
#returns in a nested dict

def rates(base, symbol):
    #use string manip to put in code for currency 
    resp = requests.get('https://api.ratesapi.io/api/latest', params = {
       "base" : base,
       "symbols" : symbol

    })
    data = resp.json()
    print(data)
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

#probably gonna have to create multiple tables and then join the data

#Process the data
#Calculate from database.(20) Do at least one database join to select data.(20) Write out calculated data to a file as text.(10)

def calculate():
    pass

#Visualize data


#Maybe use matplotlib?
def matplot(data):
    x = []
    y = []
    for key in data:
        x.append(key)
        y.append(data[key])
    x_pos = [i for i, _ in enumerate(x)]
    plt.bar(x_pos, y, color ='red')
    plt.xlabel('x axis label')
    plt.ylabel('y axis label')
    plt.title('title')
    plt.xticks(x_pos, x)
    plt.show()
    pass

#Testing:
data = marketdata("usd")
coingecko("usd")
rates("USD", "GBP")

database(data)

# def main():
#     conn.close()
#     pass