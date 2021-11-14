# -*- coding: utf-8 -*-

import csv

import matplotlib.pyplot as plt
import yfinance as yf


class Price:
    def __init__(self):
        with open('shares (2).csv', encoding="utf8") as csv_file:
            r = sorted(csv.DictReader(csv_file, delimiter=','), key=lambda x: x['tickers'])
            tickers = [i['tickers'] for i in r]
            count = [int(i['count']) for i in r]
            self.date = [i['date'] for i in r]

        self.data = yf.download(tickers, start=min(self.date))['Adj Close']

    def get_graf(self):
        for i, name in enumerate(self.data.columns):
            self.data[name][self.date[i]:].plot()
        plt.grid()
        plt.title('График цены акций')
        plt.legend()
        plt.savefig('график.png', dpi=300)
        plt.close()


class PriceIzm:
    def __init__(self):
        with open('shares (2).csv', encoding="utf8") as csv_file:
            r = sorted(csv.DictReader(csv_file, delimiter=','), key=lambda x: x['tickers'])
            tickers = [i['tickers'] for i in r]
            count = [int(i['count']) for i in r]
            self.date = [i['date'] for i in r]

            self.data = yf.download(tickers, start=min(self.date))['Adj Close']

    def get_graf_all(self):
        data_change = self.data.pct_change()
        for i, name in enumerate(data_change.columns):
            data_change[name][self.date[i]:].plot()
            plt.grid()
            plt.title(name)
            plt.savefig(f'график{i}.png', dpi=300)
            plt.close()


# p = PriceIzm()
# p.get_graf_all()
