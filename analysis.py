# -*- coding: utf-8 -*-


import csv

import yfinance as yf
from pypfopt import get_latest_prices, expected_returns, risk_models, EfficientFrontier


class Analysis:
    def __init__(self, file, period):
        with open(file, encoding="utf-8") as csv_file:
            r = sorted(csv.DictReader(csv_file, delimiter=','), key=lambda x: x['tickers'])
            tickers = [i['tickers'] for i in r]
            count = [int(i['count']) for i in r]
            self.names = {i['tickers']: i['name'] for i in r}
            self.brokers = {
                i: list(map(lambda x: x['tickers'], filter(lambda x: x['broker'] == i, r)))
                for i in sorted(set(map(lambda x: x['broker'], r)))}

        data = yf.download(tickers, period=f'{period}Y')['Adj Close']
        self.cost = get_latest_prices(data)
        self.cost.name = 'cost'
        dCloseData = data.pct_change()
        dohMean = dCloseData.mean()
        self.year_yield = (dohMean + 1) ** 365 - 1
        self.year_yield.name = 'year_yield'
        self.share_price = self.cost * count
        self.share_price.name = 'share_price'

        mu = expected_returns.mean_historical_return(data)
        Sigma = risk_models.sample_cov(data)
        ef = EfficientFrontier(mu, Sigma, weight_bounds=(0, 1))
        ef.set_weights(self.cost * count / sum(self.cost * count))
        self.performance = ef.portfolio_performance()

        # цена акции

    def prise_stock(self):
        return dict(self.cost)

        # средняя годовая доходность

    def annual_profit(self):
        return dict(self.year_yield)

        # дивидентный доход

    def dividend_profit(self):
        dividend_yield = self.year_yield / self.cost * 100
        dividend_yield.name = 'dividend_yield'
        return dict(dividend_yield)

        # цена акций(цена * кол-во)

    def price_all_shares(self):
        return dict(self.share_price)

    def price_briefcase(self):
        return round(sum(self.share_price), 3)

    def performance_briefcase(self):
        return map(lambda x: round(x, 2), self.performance)


