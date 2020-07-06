import pandas as pd 
import re
from datetime import timedelta

position_df = pd.read_csv('data/position.csv')
trading_df = pd.read_csv('data/tradingHistory.csv', usecols=['timestamp', 'price'])

position_df['openingTimestamp'] = position_df['openingTimestamp'].str.replace(r'\.\d*Z', '', regex=True).str.replace('T', ' ')
trading_df['timestamp'] = trading_df['timestamp'].str.replace(r'\.\d{3}Z', ' ', regex=True).str.replace('T', ' ')

position_df['openingTimestamp'] = pd.to_datetime(position_df['openingTimestamp'])
trading_df['timestamp'] = pd.to_datetime(trading_df['timestamp'])

# trading_df['timestamp'] = pd.to_datetime(trading_df['timestamp'])

columns = ['currentCost',
'realisedCost',
'unrealisedCost',
'posCost',
'posCost2',
'posComm',
'unrealisedGrossPnl'
]

index = (position_df['openingTimestamp'][0] - trading_df['timestamp']).idxmin()
price = trading_df.iloc[index, :]['price']

for col in columns:
    position_df[col+'_USD'] = position_df[col].astype('float')
    position_df[col+'_USD'] = position_df[col] * 0.00000001 * price
    position_df[col+'_USD'] = position_df[col+'_USD'].astype('str')
    position_df[col+'_USD'] = position_df[col+'_USD'] + ' USD'

    # print(col)

position_df.to_csv('data/position_processed.csv', index=False)
df = pd.read_csv('data/position_processed.csv')



df.to_csv('data/position_processed.csv', index=False)
df['unrealisedPnl'] = df['unrealisedPnl'] * 0.00000001
# df['unrealisedPnl'] = df['unrealisedPnl'].astype('str')
# df['unrealisedPnl_BTC'] = df['unrealisedPnl'] + ' XBT'

df['unrealisedPnlPcnt'] = df['unrealisedPnlPcnt'] * 100
df['unrealisedPnlPcnt'] = df['unrealisedPnlPcnt'].astype('str')
df['unrealisedPnlPcnt'] = df['unrealisedPnlPcnt'] + ' %'

df['unrealisedRoePcnt'] = df['unrealisedRoePcnt'] * 100
df['unrealisedRoePcnt'] = df['unrealisedRoePcnt'].astype('str')
df['unrealisedRoePcnt'] = df['unrealisedRoePcnt'] + ' %'

df['realisedPnl'] = df['realisedPnl'] * 0.00000001
# df['realisedPnl'] = df['realisedPnl'].astype('str')
# df['realisedPnl_BTC'] = df['realisedPnl'] + 'XBT'


df['unrealisedGrossPnl'] = df['unrealisedGrossPnl'] * 0.00000001
# df['unrealisedGrossPnl'] = df['unrealisedGrossPnl'].astype('str')
# df['unrealisedGrossPnl_BTC'] = df['unrealisedGrossPnl'] + ' XBT'

to_drop = ['unrealisedPnl', 'realisedPnl', 'unrealisedGrossPnl']
df.drop(to_drop, axis=1, inplace=True)

df.to_csv('data/position_processed.csv', index=False)
# df = pd.read_csv('data/tradingHistory.csv')

# df.loc[df['tradePublishIndicator'] == 'PublishTrade', 'execCost'] = df.loc[df['tradePublishIndicator'] == 'PublishTrade', 'execCost'] * 0.00000001 * df.loc[df['tradePublishIndicator'] == 'PublishTrade','price']
# df.loc[df['tradePublishIndicator'] == 'PublishTrade', 'execComm'] = df.loc[df['tradePublishIndicator'] == 'PublishTrade', 'execCost'] * 0.00000001 * df.loc[df['tradePublishIndicator'] == 'PublishTrade','price']

# df.to_csv('data/tradingHistory_processed.csv', index=False)