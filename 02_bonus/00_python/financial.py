#!/usr/bin/env python3

import sys
import requests
from bs4 import BeautifulSoup
import time

thicker_symbol = sys.argv[1].lower()
data_set = sys.argv[2]
url = 'https://finance.yahoo.com/quote/' + thicker_symbol + '/financials?p=' + thicker_symbol
r = requests.get(url)
if r.status_code == 200:
    soup = BeautifulSoup(r.text, 'html.parser')
    data=[]
    for items in soup.find_all("div", attrs={'data-test' : 'fin-row'}):
#     for items in soup.find_all("div", attrs={'class' : 'rw-expnded'}):
        for spans in items.find_all("span"):
            data.append(spans.text)

# print(data)
#     data.remove('Gross Profit')
    data=tuple(data)
    if data_set in data:
        index = data.index(data_set)
        print(data[index:(index+5)])
    else:
        raise Exception('KeyError: no %s in the keys'%data_set)
    time.sleep(5)
else:
    raise Exception("URL error: %d"%r.status_code)