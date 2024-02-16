
import pandas as pd
import ccxt
import numpy as np

def bann():
    pair = "BTC/USDT"
    df = pd.DataFrame(columns=['exchange', 'ask', 'bid'])
    ccex = ccxt.exchanges
    ba = (['bitbns','btcmarkets', 'timex', 'bitteam'])
    ccex = np.setdiff1d(ccex, ba).tolist()
    i = -1
    for t in ccex:
        t2 = getattr(ccxt, t)
        try:
            i += 1
            df.loc[i, 'exchange'] = t
            df.loc[i, 'ask'] = t2().fetch_ticker(pair)['ask']
            df.loc[i, 'bid'] = t2().fetch_ticker(pair)['bid']
        except Exception:
            df.loc[i, 'ask'] = np.nan
            df.loc[i, 'bid'] = np.nan

    ban = df[df['ask'].isna()]
    ban = ban['exchange'].to_numpy()
    ccex = df.dropna()
    ccex = ccex['exchange'].to_numpy()
    ccex = np.setdiff1d(ccex, ban)
    np.savetxt('ccex.csv', ccex, delimiter=",", fmt='%s')
    return ccex

print('---')
print(bann())
print('---')

