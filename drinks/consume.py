import requests

response = requests.get('http://127.0.0.1:8003/drinks/2/')
print(response.json())