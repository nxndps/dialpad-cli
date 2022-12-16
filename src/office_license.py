#!/usr/bin/python3

from dotenv import load_dotenv
import os
import requests

load_dotenv('.dp.env') 
dptoken = os.environ['dptoken']

url = "https://dialpad.com/api/v2/offices/5068549373853696/available_licenses"

headers = {
    "accept": "application/json",
    "authorization": "Bearer "+ dptoken
}

response = requests.get(url, headers=headers)

print(response.text)