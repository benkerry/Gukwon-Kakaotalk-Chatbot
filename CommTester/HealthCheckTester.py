import requests

response = requests.get("0.0.0.0:5000/")
print(response.text())