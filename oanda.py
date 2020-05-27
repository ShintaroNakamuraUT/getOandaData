from oandapyV20 import API
from oandapyV20.contrib.factories import InstrumentsCandlesFactory
from datetime import datetime, timedelta
import pandas as pd
import numpy as np

class GetData:
    def __init__(self, token, instruments,granularity, start_day, end_day, candle):
        self.token = token
        self.instruments = instruments
        self.start_day = start_day
        self.end_day = end_day
        start = datetime.strftime(self.start_day, '%Y-%m-%dT%H:%M:%SZ')
        end = datetime.strftime(self.end_day, '%Y-%m-%dT%H:%M:%SZ')
        self.params = {'from':start, 'to':end, 'granularity':granularity}
        self.candle = candle
    def getdata(self):
        client = API(access_token= self.token)
        data = {}
        data_frame = pd.DataFrame()
        for traindpairs in self.instruments:
            dictionary = {}
            for r in InstrumentsCandlesFactory(instrument = traindpairs, params = self.params):
                client.request(r)
                for datas in range(len(r.response.get('candles'))):
                    dictionary[datetime.strptime(r.response.get('candles')[datas]['time'].replace(".000000000Z", ''), '%Y-%m-%dT%H:%M:%S')] = r.response.get('candles')[datas]['mid'][self.candle]
            pair_dict = pd.Series(dictionary)
            data_frame[traindpairs] = pair_dict
        return data_frame