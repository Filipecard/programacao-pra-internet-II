import requests


url = 'http://shibe.online/api/shibes?count=[1-100]&urls=[true/false]&httpsUrls=[true/false]'

response = requests.get(url).json()
print('https://cdn.shibe.online/shibes/'+ response[0] +'.jpg')
