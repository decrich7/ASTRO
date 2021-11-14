# -*- coding: utf-8 -*-
# import csv
#
# import yfinance as yf
#
# with open('shares.csv', encoding="utf8") as csv_file:
#     r = {i['tickers']: int(i['count']) for i in csv.DictReader(csv_file, delimiter=',')}
# data = yf.download(list(r.keys()), period='3mo')
# dict1 = {}
# closeData = data.Close
# dCloseData = closeData.pct_change()
# dohMean = dCloseData.mean()
# average_daily_profit = dict(dohMean)
# a = dict(closeData.last('1D'))
# for key, val in r.items():
#     dict1[key] = [{'Всего куплено на': round(float(str(a[key]).split()[2]) * val, 5)},
#                   {"Цена сегодня": round(float(str(a[key]).split()[2]), 5)},
#                   {'Cредняя доходность': round(float(average_daily_profit[key]), 5)}]
#                   # {'Средняя годовая доходность': dohMean * 365},
#                   # {'Дивидентная доходность за 3 месяца': dohMean * 365 / closeData.last('1D') * 100}]
# print(dict1)

# средняя дневная доходность
# import csv
#
# import numpy as np
# import yfinance as yf
#
# with open('shares.csv', encoding="utf8") as csv_file:
#     r = {i['tickers']: int(i['count']) for i in csv.DictReader(csv_file, delimiter=',')}
#
# data = yf.download(list(r.keys()), period='12mo')
# closeData = data.Close
# print(closeData.last('1D'))  # цена сегодня
# dCloseData = closeData.pct_change()
# dohMean = dCloseData.mean()
# print(dohMean * 365)  # средняя годовая доходность
# print(dohMean * 365 / closeData.last('1D') * 100)  # дивидентная доходность
import csv

import matplotlib.pyplot as plt
import yfinance as yf

with open('shares (2).csv', encoding="utf8") as csv_file:
    r = sorted(csv.DictReader(csv_file, delimiter=','), key=lambda x: x['tickers'])
    tickers = [i['tickers'] for i in r]
    count = [int(i['count']) for i in r]
    date = [i['date'] for i in r]

data = yf.download(tickers, start=min(date))['Adj Close']

for i, name in enumerate(data.columns):
    data[name][date[i]:].plot()

plt.grid()
plt.title('График цены акций')
plt.legend()
plt.savefig('график.png', dpi=300)
