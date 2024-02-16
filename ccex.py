
from time import perf_counter

import numpy as np
import pandas as pd
import ccxt

pair = "BTC/USDT"
ccex = np.loadtxt('ccex.csv', dtype='str', delimiter=",").tolist()

def exche():
#    print(ccex)
    arr = np.array([[np.NaN, np.NaN, np.NaN]])
    for t in ccex:
        try:
            t2 = getattr(ccxt, t)
            arr = np.append(arr,
                    [[t,
                    t2().fetch_ticker(pair)['ask'], 
                    t2().fetch_ticker(pair)['bid']]],
                    axis=0)
        except Exception:
            pass

    arr = np.delete(arr, 0, 0)
#    print(arr)
    return arr

if __name__ == '__main__':
    while True:
        start = perf_counter()
        arr = exche()
        df = pd.DataFrame(arr, columns=['exchange', 'ask', 'bid'])
        df = df.dropna()
        df = df.set_index(['exchange'])

        ask = df[['ask']].sort_values(by=['ask']).head(1)
        askvalue = float(df.loc[ask.index[0]]['ask'])
        askexche = ask.index[0]

        bid = df[['bid']].sort_values(by=['bid']).tail(1)
        bidvalue = float(df.loc[bid.index[0]]['bid'])
        bidexche = bid.index[0]

        profit = round((bidvalue - askvalue) / (askvalue / 100), 2)

        #df= pd.DataFrame( {'exchange': [bidexche, askexche], 'price': [bidvalue, askvalue], 'profit': [profit,'%' ]}, index = ['bid','ask'] )
 
        df= pd.DataFrame( {'exchange ask': [askexche], 'price ask': [askvalue], 'exchange bid': [bidexche], 'price bid': [bidvalue], 'profit': [profit]} )
        
#        if profit > 0:
#            df.to_csv('exchen.csv', index = False, mode='a', header = False)
        if profit > 0:
            df.to_csv('exchen2.csv', index = False, mode='a', header = False)
        
        print(df)

        exch = pd.read_csv('exchen2.csv')
        print(exch.groupby(['exchange ask', 'exchange bid'])['profit'].sum())

        print(f'time taken: {perf_counter() - start}, min: {(perf_counter()- start)/60}')

        print('------')

