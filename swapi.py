import requests

from pprint import pprint

response = requests.get('https://swapi.dev/api/planets/1/')
pprint(response.json().get('diameter'))
