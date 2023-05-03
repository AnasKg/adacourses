import requests


data = {'name': 'Python', 'age': 19}
response = requests.post('https://www.example.com', data=data)

print(response.status_code)
print(response.content)
