import requests

response = requests.get('https://www.example.com')

print(response.status_code)
print(response.content)