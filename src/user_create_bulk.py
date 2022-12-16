#!/usr/bin/python3

import sys
import json
import time
import csv
import pprint
import requests
import argparse
from dotenv import load_dotenv

load_dotenv('.dp.env') 
dptoken = os.environ['dptoken']

parser = argparse.ArgumentParser(description='Bulk create users from a CSV file. ',
        usage='use "%(prog)s --help" for more information',
        formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument("-i", default="users_import.csv",dest='inputfile',
                    help='''CSV input file. Must include a header row with field names.
See https://developers.dialpad.com/reference/userscreate'''
                    )
parser.add_argument("-v", action="count", default=0,
                    help="Increase output verbosity. Maybe be specified multiple times.")
args = parser.parse_args()

sys.exit()

url = "https://dialpad.com/api/v2/users"

payload = {
    "auto_assign": False,
    "license": "agents",
    "email": "nxn.1002.dialpad@nxtre.com",
    "first_name": "N1002",
    "last_name": "R1002",
    "office_id": 5068549373853696
}
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "authorization": "Bearer " + dptoken
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)