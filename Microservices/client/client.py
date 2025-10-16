import requests
import json

url = "https://aggregator-image-836478715395.us-west2.run.app/lookup"

payload = {"productID" : "XYZ-12345"}

response = requests.post(url, json=payload)

print(response.text)

payload = {"productID" : "XYZ-23456"}

response = requests.post(url, json=payload)

print(response.text)

payload = {"productID" : "XYZ-99999"}

response = requests.post(url, json=payload)

print(response.text)