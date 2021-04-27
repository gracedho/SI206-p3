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


#Gather the data and save it to a single database
def setUpDatabase(db_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+db_name)
    cur = conn.cursor()
    return cur, conn

#return the data in a dictionary or json

def coingecko():
    currency = input("Enter a currency code:")
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

def coindesk(code):
    #use string manip to put in code for currency 
    #resp = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json', params = {
    #    "code" : ""
    #})
    pass 

#json: https://www.coingecko.com/api/documentations/v3/swagger.json
#json: https://api.coindesk.com/v1/bpi/currentprice/<CODE>.json

def database(data):
    cur, conn = setUpDatabase('')
    #create table
    cur.execute("DROP TABLE IF EXISTS ")
    cur.execute("CREATE TABLE ()")
    #insert data into table
    cur.execute('INSERT INTO')
    pass

#probably gonna have to create multiple tables and then join the data

#Process the data
#Calculate from database.(20) Do at least one database join to select data.(20) Write out calculated data to a file as text.(10)

def calculate():
    pass

#Visualize data

def viz(data):
    pass

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
coingecko()
# database(data)
# viz(data)

# def main():
#     conn.close()
#     pass