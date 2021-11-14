# -*- coding: utf-8 -*-
# import csv
#
# import matplotlib.pyplot as plt
# import yfinance as yf
#
# with open('shares.csv', encoding="utf8") as csv_file:
#     r = sorted(csv.DictReader(csv_file, delimiter=','), key=lambda x: x['tickers'])
#     tickers = [i['tickers'] for i in r]
#     count = [int(i['count']) for i in r]
#     date = [i['date'] for i in r]
#
# data = yf.download(tickers, start=min(date))['Adj Close']
#
# for i, name in enumerate(data.columns):
#     data[name][date[i]:].plot()
#
# plt.grid()
# plt.title('Shares')
# plt.legend()
# plt.show()
import csv

import yfinance as yf
from pypfopt import expected_returns, risk_models, EfficientFrontier, get_latest_prices, \
    DiscreteAllocation


class Rec:
    def __init__(self, risk):
        d = {'Консервативный': 0.001, 'Умеренный': 0.05, 'Рискованный': 0.1}
        self.val = d[risk]

        with open('shares.csv', encoding="utf-8") as csv_file:
            r = sorted(csv.DictReader(csv_file, delimiter=','), key=lambda x: x['tickers'])
            self.names = {i['tickers']: i['name'] for i in r}
            self.tickers = [i['tickers'] for i in r]
            self.count = [int(i['count']) for i in r]
            self.brokers = {
                i: list(map(lambda x: x['tickers'], filter(lambda x: x['broker'] == i, r)))
                for i in sorted(set(map(lambda x: x['broker'], r)))}

        self.data = yf.download(self.tickers, period='1Y')['Adj Close']
        latest_prices = get_latest_prices(self.data)
        s = sum(latest_prices * self.count)

        mu = expected_returns.mean_historical_return(self.data)
        Sigma = risk_models.sample_cov(self.data)

        ef = EfficientFrontier(mu, Sigma, weight_bounds=(0, 1))
        ef.min_volatility()
        v = ef.portfolio_performance()[1]

        ef.set_weights(latest_prices * self.count / s)
        self.p_performance = ef.portfolio_performance()
        self.p_alloc = DiscreteAllocation(
            ef.clean_weights(), latest_prices, total_portfolio_value=s).lp_portfolio()[0]

        ef = EfficientFrontier(mu, Sigma, weight_bounds=(0, 1))
        ef.efficient_risk(v + self.val)
        self.performance = ef.portfolio_performance()
        self.alloc, self.rem = DiscreteAllocation(
            ef.clean_weights(), latest_prices, total_portfolio_value=s).lp_portfolio()

        self.n = max(len(str(sum(self.p_alloc.values()))) + 5, 8)
        self.m = max(len(max(self.names.values(), key=len)) + 3, 28)

    def profit_year(self):
        return f'{round(self.p_performance[0] * 100, 2)}%', f'{round(self.performance[0] * 100, 2)}%'

    def volatility_year(self):
        return f'{round(self.p_performance[1] * 100, 2)}%', f'{round(self.performance[1] * 100, 2)}%'

    def koef_sharp(self):
        return f'{round(self.p_performance[2], 2)}', f'{round(self.performance[2], 2)}'

    def final(self):
        return f'{sum(self.p_alloc.values())} шт.', f'{sum(self.alloc.values())} шт.'

    def balance(self):
        return "{:.2f}$".format(self.rem)

    def fin_stock(self):
        return '\n'.join(f'\t{b}:\n' + '\n'.join([f'\t{self.names[i]}:'.ljust(self.m) +
                                                  f'До - {self.p_alloc.get(i, 0)} шт.\t'.ljust(
                                                      self.n) +
                                                  f'После - {self.alloc.get(i, 0)} шт.' for i in t])
                         for b, t in self.brokers.items())


