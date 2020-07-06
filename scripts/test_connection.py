import pymysql.cursors
import pandas as pd
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Boolean, Float
from sqlalchemy.orm import sessionmaker


# user = 'root'
# password = 'H@s@n.@bb@s'
# # host = '64.227.25.121'
# # host = '127.0.0.1'
# # host = '192.168.1.100'
# # host = 'tradingvps'
# host = 'localhost'
# port = 3306
# database_name = 'testdb'



# def make_connection(host=host, user=user, password=password, database_name=database_name, port=port):
#     print('Connecting to the database\n')

#     connection = pymysql.connect(
#                                 host=host,
#                                 user=user,
#                                 password=password,
#                                 db=database_name,
#                                 charset='utf8mb4',
#                                 cursorclass=pymysql.cursors.DictCursor,
#                                 port=port)

#     return connection

# def close_connection(db):
#     print('Closing the connection')
#     db.close()



# def show_tables(db):
#     cursor = db.cursor()
#     sql = f'show tables'
#     cursor.execute(sql)
#     data = cursor.fetchall()

#     # for d in data:
#     #     key = 'Tables_in_' + database_name
#     #     print(d[key])
#     return data



# def db_connection(user=user, password=password, host=host, port=port, database_name=database_name):
#     connection_string = f'mysql+pymysql://{user}:{password}@{host}:{port}/{database_name}' #newdb
#     engine = create_engine(connection_string)
#     Session = sessionmaker(bind = engine)
#     session = Session()
#     session.commit()
#     session.close()
#     return engine



# def dump_table(table, table_name, chunksize=1000, if_exists='append'):
    
#     if if_exists == 'append':
#         # db = make_connection(host, user, password, database_name, port)
#         # drop_tables(db, [table_name], truncate=True)
#         # close_connection(db)
#         # print(f'Appending {table_name}')
#         engine = db_connection(user=user, password=password, host=host, port=port, database_name=database_name)
#         table.to_sql(name = table_name, con = engine, if_exists = if_exists, index = False, chunksize = 1000)
#         print(f'Table {table_name} appended')

#     elif if_exists == 'replace':
#         print(f'Replacing {table_name}')
#         engine = db_connection(user=user, password=password, host=host, port=port, database_name=database_name)
#         table.to_sql(name = table_name, con = engine, if_exists = if_exists, index = False, chunksize = 1000)
#         print(f'Table {table_name} replaced')

#     else:
#         print('Failed')

# df = pd.read_csv('data/position.csv')
# engine = db_connection()
# dump_table(df, 'position')


df = pd.read_csv('data/user_wallet.csv')
columns = df.columns 

dtypes_dict = {col:df[col].dtype for col in columns}

for key, value in dtypes_dict.items():
    print(value)
    if 'timestamp' in str(value):
        dtypes_dict[key] = 'datetime'
    # elif value == str('datetime'):
    #     dtypes_dict[key] = 'Date Time'
    elif value == str('int64'):
        dtypes_dict[key] = 'Integer'
    elif value == str('float64'):
        dtypes_dict[key] = 'Float'
    elif value == str('bool'):
        dtypes_dict[key] = 'Boolean'
    elif value == str('object'):
        dtypes_dict[key] = 'String(32)'

for  key, value in dtypes_dict.items():
    print(f'Column(\'{key}\', {value}),') 

# dtypes_dict = {
#     'int64': 'Integer',
#     'float64' : 'Float',
#     'bool' : 'Boolean',
#     'datetime''Date Time',
#     'object' : 'String'
# }

# for 

#position
# Column('account', Integer),
# Column('symbol', String(32)),
# Column('currency', String(32)),
# Column('underlying', String(32)),
# Column('quoteCurrency', String(32)),
# Column('commission', Float),
# Column('initMarginReq', Float),
# Column('maintMarginReq', Float),
# Column('riskLimit', Integer),
# Column('leverage', Integer),
# Column('crossMargin', Boolean),
# Column('deleveragePercentile', Integer),
# Column('rebalancedPnl', Integer),
# Column('prevRealisedPnl', Integer),
# Column('prevUnrealisedPnl', Integer),
# Column('prevClosePrice', Float),
# Column('openingTimestamp', String(32)),
# Column('openingQty', Integer),
# Column('openingCost', Integer),
# Column('openingComm', Integer),
# Column('openOrderBuyQty', Integer),
# Column('openOrderBuyCost', Integer),
# Column('openOrderBuyPremium', Integer),
# Column('openOrderSellQty', Integer),
# Column('openOrderSellCost', Integer),
# Column('openOrderSellPremium', Integer),
# Column('execBuyQty', Integer),
# Column('execBuyCost', Integer),
# Column('execSellQty', Integer),
# Column('execSellCost', Integer),
# Column('execQty', Integer),
# Column('execCost', Integer),
# Column('execComm', Integer),
# Column('currentTimestamp', String(32)),
# Column('currentQty', Integer),
# Column('currentCost', Integer),
# Column('currentComm', Integer),
# Column('realisedCost', Integer),
# Column('unrealisedCost', Integer),
# Column('grossOpenCost', Integer),
# Column('grossOpenPremium', Integer),
# Column('grossExecCost', Integer),
# Column('isOpen', Boolean),
# Column('markPrice', Float),
# Column('markValue', Integer),
# Column('riskValue', Integer),
# Column('homeNotional', Float),
# Column('foreignNotional', Integer),
# Column('posState', Float),
# Column('posCost', Integer),
# Column('posCost2', Integer),
# Column('posCross', Integer),
# Column('posInit', Integer),
# Column('posComm', Integer),
# Column('posLoss', Integer),
# Column('posMargin', Integer),
# Column('posMaint', Integer),
# Column('posAllowance', Integer),
# Column('taxableMargin', Integer),
# Column('initMargin', Integer),
# Column('maintMargin', Integer),
# Column('sessionMargin', Integer),
# Column('targetExcessMargin', Integer),
# Column('varMargin', Integer),
# Column('realisedGrossPnl', Integer),
# Column('realisedTax', Integer),
# Column('realisedPnl', Integer),
# Column('unrealisedGrossPnl', Integer),
# Column('longBankrupt', Integer),
# Column('shortBankrupt', Integer),
# Column('taxBase', Integer),
# Column('indicativeTaxRate', Float),
# Column('indicativeTax', Integer),
# Column('unrealisedTax', Integer),
# Column('unrealisedPnl', Integer),
# Column('unrealisedPnlPcnt', Float),
# Column('unrealisedRoePcnt', Float),
# Column('simpleQty', Float),
# Column('simpleCost', Float),
# Column('simpleValue', Float),
# Column('simplePnl', Float),
# Column('simplePnlPcnt', Float),
# Column('avgCostPrice', Float),
# Column('avgEntryPrice', Float),
# Column('breakEvenPrice', Float),
# Column('marginCallPrice', Integer),
# Column('liquidationPrice', Integer),
# Column('bankruptPrice', Integer),
# Column('timestamp', String(32)),
# Column('lastPrice', Float),
# Column('lastValue', Integer)

# Tradinghistory
# Column('execID', String(32)),
# Column('orderID', String(32)),
# Column('clOrdID', String(32)),
# Column('clOrdLinkID', Float),
# Column('account', Integer),
# Column('symbol', String(32)),
# Column('side', String(32)),
# Column('lastQty', Integer),
# Column('lastPx', Float),
# Column('underlyingLastPx', Float),
# Column('lastMkt', String(32)),
# Column('lastLiquidityInd', String(32)),
# Column('simpleOrderQty', Float),
# Column('orderQty', Integer),
# Column('price', Float),
# Column('displayQty', Float),
# Column('stopPx', Float),
# Column('pegOffsetValue', Float),
# Column('pegPriceType', String(32)),
# Column('currency', String(32)),
# Column('settlCurrency', String(32)),
# Column('execType', String(32)),
# Column('ordType', String(32)),
# Column('timeInForce', String(32)),
# Column('execInst', String(32)),
# Column('contingencyType', Float),
# Column('exDestination', String(32)),
# Column('ordStatus', String(32)),
# Column('triggered', String(32)),
# Column('workingIndicator', Boolean),
# Column('ordRejReason', Float),
# Column('simpleLeavesQty', Float),
# Column('leavesQty', Integer),
# Column('simpleCumQty', Float),
# Column('cumQty', Integer),
# Column('avgPx', Float),
# Column('commission', Float),
# Column('tradePublishIndicator', String(32)),
# Column('multiLegReportingType', String(32)),
# Column('text', String(32)),
# Column('trdMatchID', String(32)),
# Column('execCost', Integer),
# Column('execComm', Integer),
# Column('homeNotional', Float),
# Column('foreignNotional', Integer),
# Column('transactTime', String(32)),
# Column('timestamp', String(32)),


#Order 
# Column('orderID', String(32)),
# Column('clOrdID', Float),
# Column('clOrdLinkID', Float),
# Column('account', Integer),
# Column('symbol', String(32)),
# Column('side', String(32)),
# Column('simpleOrderQty', Float),
# Column('orderQty', Integer),
# Column('price', Float),
# Column('displayQty', Float),
# Column('stopPx', Float),
# Column('pegOffsetValue', Float),
# Column('pegPriceType', String(32)),
# Column('currency', String(32)),
# Column('settlCurrency', String(32)),
# Column('ordType', String(32)),
# Column('timeInForce', String(32)),
# Column('execInst', String(32)),
# Column('contingencyType', Float),
# Column('exDestination', String(32)),
# Column('ordStatus', String(32)),
# Column('triggered', String(32)),
# Column('workingIndicator', Boolean),
# Column('ordRejReason', String(32)),
# Column('simpleLeavesQty', Integer),
# Column('leavesQty', Integer),
# Column('simpleCumQty', Float),
# Column('cumQty', Integer),
# Column('avgPx', Float),
# Column('multiLegReportingType', String(32)),
# Column('text', String(32)),
# Column('transactTime', String(32)),
# Column('timestamp', String(32)),