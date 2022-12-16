import requests

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
    "authorization": "Bearer Emd8D7a4yAbGtj29mEWwB3HyqEgcEF7genNbFRk8zG4Y37CUBNFYkbxnLVFDucaCaQ8dMaGFQrjnvxFvbeB8gcSwPp9cZ7sNQNFE"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)