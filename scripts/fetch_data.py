import argparse
import json
import csv
import sys
from lib import bitmex
from settings import API_KEY, API_SECRET, API_BASE
from utils import get_bitcoin_rate
import pandas as pd 
from sqlalchemy import create_engine


def fetch_endpoints(args):
    # Validate Args
    fileType = args.fileType
    if fileType not in ('json', 'csv'):
        raise Exception('Output file type must be json or csv! Given: %s' % fileType)

    if args.filter:
        # Verify if it's proper JSON
        try:
            json.loads(args.filter)
        except ValueError as e:
            raise ValueError("Filter is not valid JSON! Make sure to single-quote the string.")

    # Create connector
    connector = bitmex.BitMEX(base_url=API_BASE, apiKey=API_KEY, apiSecret=API_SECRET)

    # Do trade history query
    count = 500  # max API will allow
    query = {
        'reverse': 'true',
        'start': 0,
        'count': count,
        'filter': args.filter
    }

    out = []
    json_data_dict_list = []

    # bitcoin_rate = get_bitcoin_rate()

    while True:
        path = args.endpoint
        print(path)
        if args.isquery:
            data = connector._curl_bitmex(path=path, verb="GET", query=query, timeout=10)
        else:
            data = connector._curl_bitmex(path=path, verb="GET", timeout=10)
        
        out.extend(data)
        # print(out)
        query['start'] += count
        if len(data) < count:
            break
        
    if len(out) == 0:
        print('No trade history found for this account. Exiting.', file=sys.stderr)
        exit(1)

    # Write to stdout
    if fileType == 'csv':
        df = pd.DataFrame()
        for d in out:

        # csv requires dict keys
        # keys = out[0].keys()
        # keys = sorted(keys)
        # csvwriter = csv.DictWriter(sys.stdout, fieldnames=keys)
        # csvwriter.writeheader()
        # csvwriter.writerows(out)
            temp = pd.DataFrame([d])
            df = df.append(temp)
        output_filename = path[1:] + '.csv'
        output_filename = output_filename.replace('/', '_')
        output_path = 'data/' + output_filename
        df.to_csv(output_path, index=False)

    elif fileType == 'json':
        for i in out:
            d = json.dumps(i, sort_keys=True, indent=4, separators=(',', ': '))
            # json_data = json.dumps(out)

            json_data = json.loads(d)
            
            # print(json_data)
            
            if args.endpoint == '/position':
                columns = ['currentCost',
                            'realisedCost',
                            'unrealisedCost',
                            'posCost',
                            'posCost2',
                            'posComm',
                            'unrealisedGrossPnl'
                            ]
                for col in columns:
                    # if json_data[col] != None:
                    #     json_data[col] = float(json_data[col]) * 0.00000001 * bitcoin_rate
                    pass
                # print(json_data)
                json_data_dict_list.append(json_data)
            else:
                json_data_dict_list.append(json_data)
        
        # print(json_data_dict)
        return json_data_dict_list

    else:
        # Shouldn't happen
        raise Exception('Unknown output file type.')

