import json
import requests

response = requests.get('https://tv.kofteistan.co/')
data = response.json()
print(data[1])
id = data[1]['id']

another_response = requests.get(f'https://tv.kofteistan.co/{id}/season/3')
another_data = another_response.json()

some_data = another_data['episodes'][1]
print(another_data['episodes'])

# for i in range(1,10):


