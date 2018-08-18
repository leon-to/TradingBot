import oandapyV20
import oandapyV20.endpoints.forexlabs as labs
import oandapyV20.endpoints.pricing as pricing
import oandapyV20.endpoints.instruments as instruments
import json
from pandas.io.json import json_normalize
import pandas as pd
from credentials import Credentials
import matplotlib.pyplot as plt

my_credentials = Credentials.fromJsonFile('credentials.json')

api = oandapyV20.API(access_token=my_credentials.token)

params = {
  "count": 200,
  "granularity": "H1"
}
# request
r = instruments.InstrumentsCandles(instrument="DE30_EUR",
                                   params=params)

api.request(r)
candles = r.response['candles']
# print (json.dumps(r.response['candles'], indent=2))

# initiate data frame
df = json_normalize(candles).drop(columns=['complete'])
# rename column
df = df.rename(columns={
  'time': 'date',
  'mid.c': 'close',
  'mid.h': 'high',
  'mid.l': 'low',
  'mid.o': 'open'
})
# convert to datetime object
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%dT%H:%M:%S')
# set index column
df = df.set_index('date')
# conver object into float64
# df = df.apply(pd.to_numeric, errors='coerce')
for x in ['close', 'high', 'low', 'open']:
  df[x] = pd.to_numeric(df[x])


# print(df['2018-08-17 0:0:0'])
# print (df['close'])
# df.reset_index()
print (df.dtypes)

df['close'].plot()
df['open'].plot()
plt.show()
