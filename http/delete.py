import requests

response = requests.delete('https://www.example.com')

print(response.status_code)
print(response.content)
