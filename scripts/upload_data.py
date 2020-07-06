import pandas as pd
from sqlalchemy import types
from sqlalchemy.orm import sessionmaker
import pymysql
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Boolean, Float, BigInteger
from sqlalchemy.dialects.mysql import LONGTEXT



user = 'root'
password = '$3noR1@l2020'
host = 'localhost'
port = 3306
database_name = 'trading_db'

# user = 'root'
# password = 'H@s@n.@bb@s'
# host = 'localhost'
# port = 3306
# database_name = 'testdb'


def make_connection(host=host, user=user, password=password, database_name=database_name, port=port):
    print('Connecting to the database\n')

    connection = pymysql.connect(
                                host=host,
                                user=user,
                                password=password,
                                db=database_name,
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor,
                                port=port)

    return connection

def close_connection(db):
    print('Closing the connection')
    db.close()

def show_data(db, table):
    cursor = db.cursor()
    sql = f'select * from {table}'
    cursor.execute(sql)
    data = cursor.fetchall()
    return data

def show_tables(db):
    cursor = db.cursor()
    sql = f'show tables'
    cursor.execute(sql)
    data = cursor.fetchall()

    # for d in data:
    #     key = 'Tables_in_' + database_name
    #     print(d[key])
    return data


def drop_tables(db, tables, truncate=True):
    cursor = db.cursor()
    if truncate:
        # x = input(f'Press y/Y to truncate table {" ".join(tables)}\n')
        # if x=='y' or x=='Y':
        for tablename in tables:
            sql = f'truncate table {tablename}'
            cursor.execute(sql)
            print(f'{tablename} table truncated')
    else:
        x = input(f'Press y/Y to drop table {" ".join(tables)}\n')
        if x=='y' or x=='Y':
            for tablename in tables:
                sql = f'drop table {tablename}'
                cursor.execute(sql)
                print(f'{tablename} table dropped')

def db_connection(user=user, password=password, host=host, port=port, database_name=database_name):
    connection_string = f'mysql+pymysql://{user}:{password}@{host}:{port}/{database_name}' #newdb
    engine = create_engine(connection_string)
    Session = sessionmaker(bind = engine)
    session = Session()
    session.commit()
    session.close()
    return engine



def create_tables(engine):
    meta = MetaData()
    df = pd.read_csv('data/position.csv')
    columns = df.columns 
    position = Table(
    'position', meta, 
   Column('account', Integer),
    Column('symbol', String(32)),
    Column('currency', String(32)),
    Column('underlying', String(32)),
    Column('quoteCurrency', String(32)),
    Column('commission', Float),
    Column('initMarginReq', Float),
    Column('maintMarginReq', Float),
    Column('riskLimit', BigInteger),
    Column('leverage', Integer),
    Column('crossMargin', Boolean),
    Column('deleveragePercentile', Integer),
    Column('rebalancedPnl', Integer),
    Column('prevRealisedPnl', Integer),
    Column('prevUnrealisedPnl', Integer),
    Column('prevClosePrice', Float),
    Column('openingTimestamp', String(32)),
    Column('openingQty', Integer),
    Column('openingCost', Integer),
    Column('openingComm', Integer),
    Column('openOrderBuyQty', Integer),
    Column('openOrderBuyCost', Integer),
    Column('openOrderBuyPremium', Integer),
    Column('openOrderSellQty', Integer),
    Column('openOrderSellCost', Integer),
    Column('openOrderSellPremium', Integer),
    Column('execBuyQty', Integer),
    Column('execBuyCost', Integer),
    Column('execSellQty', Integer),
    Column('execSellCost', Integer),
    Column('execQty', Integer),
    Column('execCost', Integer),
    Column('execComm', Integer),
    Column('currentTimestamp', String(32)),
    Column('currentQty', Integer),
    Column('currentCost', Integer),
    Column('currentComm', Integer),
    Column('realisedCost', Integer),
    Column('unrealisedCost', Integer),
    Column('grossOpenCost', Integer),
    Column('grossOpenPremium', Integer),
    Column('grossExecCost', Integer),
    Column('isOpen', Boolean),
    Column('markPrice', Float),
    Column('markValue', Integer),
    Column('riskValue', Integer),
    Column('homeNotional', Float),
    Column('foreignNotional', Integer),
    Column('posState', Float),
    Column('posCost', Integer),
    Column('posCost2', Integer),
    Column('posCross', Integer),
    Column('posInit', Integer),
    Column('posComm', Integer),
    Column('posLoss', Integer),
    Column('posMargin', Integer),
    Column('posMaint', Integer),
    Column('posAllowance', Integer),
    Column('taxableMargin', Integer),
    Column('initMargin', Integer),
    Column('maintMargin', Integer),
    Column('sessionMargin', Integer),
    Column('targetExcessMargin', Integer),
    Column('varMargin', Integer),
    Column('realisedGrossPnl', Integer),
    Column('realisedTax', Integer),
    Column('realisedPnl', Integer),
    Column('unrealisedGrossPnl', Integer),
    Column('longBankrupt', Integer),
    Column('shortBankrupt', Integer),
    Column('taxBase', Integer),
    Column('indicativeTaxRate', Float),
    Column('indicativeTax', Integer),
    Column('unrealisedTax', Integer),
    Column('unrealisedPnl', Integer),
    Column('unrealisedPnlPcnt', Float),
    Column('unrealisedRoePcnt', Float),
    Column('simpleQty', Float),
    Column('simpleCost', Float),
    Column('simpleValue', Float),
    Column('simplePnl', Float),
    Column('simplePnlPcnt', Float),
    Column('avgCostPrice', Float),
    Column('avgEntryPrice', Float),
    Column('breakEvenPrice', Float),
    Column('marginCallPrice', Integer),
    Column('liquidationPrice', Integer),
    Column('bankruptPrice', Integer),
    Column('timestamp', String(32)),
    Column('lastPrice', Float),
    Column('lastValue', Integer)
    )

    tradeHistory = Table(
    'tradeHistory', meta,
    Column('execID', String(200)),
    Column('orderID', String(200)),
    Column('clOrdID', String(200)),
    Column('clOrdLinkID', Float),
    Column('account', Integer),
    Column('symbol', String(32)),
    Column('side', String(32)),
    Column('lastQty', Integer),
    Column('lastPx', Float),
    Column('underlyingLastPx', Float),
    Column('lastMkt', String(32)),
    Column('lastLiquidityInd', String(32)),
    Column('simpleOrderQty', Float),
    Column('orderQty', Integer),
    Column('price', Float),
    Column('displayQty', Float),
    Column('stopPx', Float),
    Column('pegOffsetValue', Float),
    Column('pegPriceType', String(32)),
    Column('currency', String(32)),
    Column('settlCurrency', String(32)),
    Column('execType', String(32)),
    Column('ordType', String(32)),
    Column('timeInForce', String(32)),
    Column('execInst', String(32)),
    Column('contingencyType', Float),
    Column('exDestination', String(32)),
    Column('ordStatus', String(32)),
    Column('triggered', String(32)),
    Column('workingIndicator', Boolean),
    Column('ordRejReason', Float),
    Column('simpleLeavesQty', Float),
    Column('leavesQty', Integer),
    Column('simpleCumQty', Float),
    Column('cumQty', Integer),
    Column('avgPx', Float),
    Column('commission', Float),
    Column('tradePublishIndicator', String(32)),
    Column('multiLegReportingType', String(32)),
    Column('text', String(200)),
    Column('trdMatchID', String(200)),
    Column('execCost', Integer),
    Column('execComm', Integer),
    Column('homeNotional', Float),
    Column('foreignNotional', Integer),
    Column('transactTime', String(32)),
    Column('timestamp', String(32)),
    )

    orders = Table(
    'orders', meta,
    Column('orderID', String(200)),
    Column('clOrdID', Float),
    Column('clOrdLinkID', Float),
    Column('account', Integer),
    Column('symbol', String(32)),
    Column('side', String(32)),
    Column('simpleOrderQty', Float),
    Column('orderQty', Integer),
    Column('price', Float),
    Column('displayQty', Float),
    Column('stopPx', Float),
    Column('pegOffsetValue', Float),
    Column('pegPriceType', String(32)),
    Column('currency', String(32)),
    Column('settlCurrency', String(32)),
    Column('ordType', String(32)),
    Column('timeInForce', String(32)),
    Column('execInst', String(32)),
    Column('contingencyType', Float),
    Column('exDestination', String(32)),
    Column('ordStatus', String(32)),
    Column('triggered', String(32)),
    Column('workingIndicator', Boolean),
    Column('ordRejReason', String(200)),
    Column('simpleLeavesQty', Integer),
    Column('leavesQty', Integer),
    Column('simpleCumQty', Float),
    Column('cumQty', Integer),
    Column('avgPx', Float),
    Column('multiLegReportingType', String(32)),
    Column('text', String(200)),
    Column('transactTime', String(32)),
    Column('timestamp', String(32)),
    )

    meta.create_all(engine)
    print('Tables Created')

def dump_table(table, table_name, chunksize=1000, if_exists='append'):
    
    # if if_exists == 'append':
    #     db = make_connection(host, user, password, database_name, port)
    #     drop_tables(db, [table_name], truncate=True)
    #     close_connection(db)
    #     print(f'Appending {table_name}')
    #     engine = db_connection(user=user, password=password, host=host, port=port, database_name=database_name)
    #     table.to_sql(name = table_name, con = engine, if_exists = if_exists, index = False, chunksize = 1000)
    #     print(f'Table {table_name} appended')

    # elif if_exists == 'replace':
    print(f'Replacing {table_name}')
    engine = db_connection(user=user, password=password, host=host, port=port, database_name=database_name)
    table.to_sql(name = table_name, con = engine, if_exists = if_exists, index = False, chunksize = 1000)
    print(f'Table {table_name} replaced')

    # else:
    #     print('Failed')
    
    