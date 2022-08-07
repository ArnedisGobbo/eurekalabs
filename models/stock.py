from db import db
import uuid


class StockModel(object):
    def __init__(self, open_price, higher_price, lower_price, variation):
        self.open_price = open_price
        self.higher_price = higher_price
        self.lower_price = lower_price
        self.variation = round(variation, 4)

    def json(self):
        return {
            'open price': self.open_price,
            'higher price': self.higher_price,
            'lower price': self.lower_price,
            'variation between last 2 closing price values': self.variation
        }
