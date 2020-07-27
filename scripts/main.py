import argparse
from .fetch_data import fetch_endpoints
from .utils import write_csv
from .upload_data import db_connection, create_tables ,dump_table, show_tables, make_connection, drop_tables, show_data,close_connection
import pandas as pd 
from collections import namedtuple

def getData(endpoint='/position'):
    # parser = argparse.ArgumentParser(description='Fetch data from Bitmex API')
    # parser.add_argument('--fileType', type=str, default='json',
    #                     help='Output file type. Must end be json or csv.')
    # parser.add_argument('--filter', type=str,
    #                     help='Query filter as JSON.')
    # parser.add_argument('--endpoint', '--ep', type=str, help='Endpoint name')
    # parser.add_argument('--isquery', '--isquery', type=bool, default=False, help='Provide query?')
    # args = parser.parse_args()
    # args = (endpoint='C:/Program Files/Git/position', fileType='json', filter=None, isquery=False)
    Data =  namedtuple("args",["fileType","filter","isquery","endpoint"])
    args = Data("json",None,False,endpoint)
    print(args)
    
    
    json_data = fetch_endpoints(args, endpoint)
    # print(json_data)
    endpoint = endpoint.replace('/','_')[1:]
    # df = pd.DataFrame.from_dict(json_data, orient='index').T
    # df = pd.DataFrame(json_data)
    # print(json_data)
    # df.to_csv(f'data/{endpoint}.csv', index=False)
    # print(df.head())
    # # df.fillna(0, inplace=True) # Recheck it
    # output_filename = args.endpoint[1:].replace('/','_') + '.csv'
    # df.to_csv(f'data/test_{output_filename}', index=False)
    # print(f'Wrote csv {output_filename}')

    # df = pd.read_csv('data/position.csv')
    # orders = pd.read_csv('data/orders.csv')
    # tradeHistory = pd.read_csv('data/tradingHistory.csv')
    # db = make_connection()
    
    # drop_tables(db, ['position'], truncate=False)
    # drop_tables(db, ['tradeHistory'], truncate=False)
    # drop_tables(db, ['orders'], truncate=False)

    # engine = db_connection()
    # create_tables(engine)
    
    # dump_table(df, 'position')

    # # # db = make_connection()
    # # # drop_tables(db, ['order'], truncate=False)

    # dump_table(orders, 'orders')

    # dump_table(tradeHistory, 'tradeHistory')

    # print(show_tables(db))
    # print(show_data(db, 'position'))
    # print('-------------------------------------')
    # print(show_data(db, 'tradeHistory'))
    # print('-------------------------------------')
    # print(show_data(db, 'orders'))
    # print('-------------------------------------')
    # close_connection(db)

    return json_data



if __name__== '__main__':
    """"Pass the name of the endpoint
    You can find the endpoints here https://www.bitmex.com/api/explorer/#/Execution"""
    df = getData(endpoint='/user/wallet')
    # print(df.head())