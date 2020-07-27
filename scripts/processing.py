import pandas as pd 
import csv

def write_csv(mode, row):
    with open('output.csv', mode, newline='') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        wr.writerow(my_list)

position = pd.read_csv('data/position_processed.csv', usecols=['openingTimestamp'])
tradeHistory = pd.read_csv('data/tradingHistory.csv', usecols=['side', 'timestamp'])
user_margin = pd.read_csv('data/user_margin.csv', usecols=['marginUsedPcnt'])

tradeHistory['timestamp'] = tradeHistory['timestamp'].str.replace(r'\.\d{3}Z', ' ', regex=True).str.replace('T', ' ')

position['openingTimestamp'] = pd.to_datetime(position['openingTimestamp'])
tradeHistory['timestamp'] = pd.to_datetime(tradeHistory['timestamp'])

timestamp_position = position.loc[:,'openingTimestamp'][0]
index = (position['openingTimestamp'] - tradeHistory['timestamp']).idxmin()
side, timestamp_trade = tradeHistory.iloc[index, :][['side', 'timestamp']]
margin_pcnt = user_margin['marginUsedPcnt'][0]
my_list = ['timestamp', 'side', 'marginUsedPcnt']
write_csv(mode='w', row=my_list)
my_list = [timestamp_position, side, margin_pcnt]
write_csv(mode='a', row=my_list)

