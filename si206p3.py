from bs4 import BeautifulSoup
import requests
import unittest
import sqlite3
import json
import os
import matplotlib.pyplot as plt

#SI206 Final Project
#Names: Grace Ho, Aaron Huang


#Gather the data and save it to a single database
def setUpDatabase(db_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+db_name)
    cur = conn.cursor()
    return cur, conn

#return the data in a dictionary or json
def grab_data(url):
    resp = requests.get(url)
    soup = BeautifulSoup(resp.content, 'html.parser')
    pass

def database(data):
    pass

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
# data = grab_data("")
# database(data)
# viz(data)

# def main():
#     conn.close()
#     pass
