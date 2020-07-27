import pandas as pd 
import numpy as np
import re
from datetime import timedelta
import os

position_df = pd.read_csv('data/position.csv')
trading_df = pd.read_csv('data/execution_tradeHistory.csv', usecols=['timestamp', 'price'])

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



# df['unrealisedRoePcnt_currentQty'] = np.abs(df['unrealisedRoePcnt'] * df['currentQty'])

# df['unrealisedPnl'] = df['unrealisedPnl'] * 0.00000001
# # df['unrealisedPnl'] = df['unrealisedPnl'].astype('str')
# # df['unrealisedPnl_BTC'] = df['unrealisedPnl'] + ' XBT'

# df['unrealisedPnlPcnt'] = df['unrealisedPnlPcnt'] * 100
# df['unrealisedPnlPcnt'] = df['unrealisedPnlPcnt'].astype('str')
# df['unrealisedPnlPcnt'] = df['unrealisedPnlPcnt'] + ' %'

# df['unrealisedRoePcnt'] = df['unrealisedRoePcnt'] * 100
# df['unrealisedRoePcnt'] = df['unrealisedRoePcnt'].astype('str')
# df['unrealisedRoePcnt'] = df['unrealisedRoePcnt'] + ' %'

# df['realisedPnl'] = df['realisedPnl'] * 0.00000001
# # df['realisedPnl'] = df['realisedPnl'].astype('str')
# # df['realisedPnl_BTC'] = df['realisedPnl'] + 'XBT'


# df['unrealisedGrossPnl'] = df['unrealisedGrossPnl'] * 0.00000001
# # df['unrealisedGrossPnl'] = df['unrealisedGrossPnl'].astype('str')
# # df['unrealisedGrossPnl_BTC'] = df['unrealisedGrossPnl'] + ' XBT'

# to_drop = ['unrealisedPnl', 'realisedPnl', 'unrealisedGrossPnl']
# df.drop(to_drop, axis=1, inplace=True)

# df.to_csv('data/position_processed.csv', index=False)
# # df = pd.read_csv('data/tradingHistory.csv')

# # df.loc[df['tradePublishIndicator'] == 'PublishTrade', 'execCost'] = df.loc[df['tradePublishIndicator'] == 'PublishTrade', 'execCost'] * 0.00000001 * df.loc[df['tradePublishIndicator'] == 'PublishTrade','price']
# # df.loc[df['tradePublishIndicator'] == 'PublishTrade', 'execComm'] = df.loc[df['tradePublishIndicator'] == 'PublishTrade', 'execCost'] * 0.00000001 * df.loc[df['tradePublishIndicator'] == 'PublishTrade','price']

# # df.to_csv('data/tradingHistory_processed.csv', index=False)


# test_dict = {'account': 63908,
#  'currency': 'XBt', 
#  'prevDeposited': 98311965,
#   'prevWithdrawn': 58600000, 
#   'prevTransferIn': 10000000, 'prevTransferOut': 0,
#    'prevAmount': 963374, 
#    'prevTimestamp': '2020-07-05T12:00:00.015Z', 
#    'deltaDeposited': 0, 
#    'deltaWithdrawn': 0, 
#    'deltaTransferIn': 0, 
#    'deltaTransferOut': 0,
#     'deltaAmount': 0,
#      'deposited': 98311965, 
#      'withdrawn': 58600000,
#       'transferIn': 10000000, 
#       'transferOut': 0, 
#       'amount': 963374,
#        'pendingCredit': 0,
#         'pendingDebit': 0,
#          'confirmedDebit': 0, 
#          'timestamp': '2020-07-05T12:00:00.662Z',
#           'addr': '2NBMEXRjjsDBRNbC3jx2CcBsMMtZbGsw4Up',
#            'script': '532102c10be2f0dc20f4285c25156aa22a0c46d2b89ccc4d1c8eaed92ea0c1a8f40c002102ceba29da1af96a0f2ef7cda6950b8be2baeb1adf12c0d5efebb70dbcaa086ba021034dce67afa4c9e25bf39de42600c466dd870118ea398e25df25152aac7e1fe5f02103d5a42b90e9d7156155661979530a09d2e12e252ef4104e5611274a7ae7e2b09454ae',
#             'withdrawalLock': []
#             }


# print(pd.DataFrame.from_dict(test_dict, orient='index').T)

for filename in os.listdir('data/'):
    df = pd.read_csv(f'data/{filename}')
    print(filename)
    print(df.shape[1])
    print('------------------------------------------------------')


