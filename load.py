import csv
import requests
import json


headers = {'Content-Type': 'application/json'}


def transform(data):
    for k, v in data.items():
        try:
            data[k] = float(v)
        except:
            data[k] = 0 if k in ["tests_units"] else data[k]
            data[k] = data[k] if v else None
    return data


with open('owid-covid-data.csv') as csvfile:
    for data in csv.DictReader(csvfile, quoting=csv.QUOTE_NONE, delimiter =","):
        data = transform(data)
        r = requests.post('http://127.0.0.1:80/owidCovidData', data= json.dumps(data), headers= headers)
        if r.status_code != 200:
            print(data)
            print(r.status_code)
            print(r.text)
            break