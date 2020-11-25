import requests

palavra = 'SOS'
url = 'http://www.morsecode-api.de/encode?string={word}'

url = url.format(word = palavra)
response = requests.get(url).json()

print('palavra:',response['plaintext'],'\nmorse :',response['morsecode'])