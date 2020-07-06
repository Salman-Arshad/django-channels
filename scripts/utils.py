import pandas as pd 
import numpy as np  
import requests
from requests.exceptions import HTTPError
from bs4 import BeautifulSoup
import codecs
import re
import csv


def get_bitcoin_rate():
    url = 'https://blockchain.info/ticker'

    try:
        r = requests.get(url)
    except HTTPError as http_err:
        print(f'Http error occured {http_err}')
    except Exception as e:
        print(e)
    else:
        print(f'Success')

    data = r.json()
    exchange_rate = data["USD"]["last"]
    print(f'Bitcoin exchange rate = {exchange_rate} USD')
    exchange_rate = float(exchange_rate)
    return exchange_rate

def write_csv(filename, mode, row):
    with open(filename, mode, newline='') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        wr.writerow(row)