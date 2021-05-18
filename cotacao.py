import requests
import json

cidade = input('Escreva sua cidade:')

requisicao = requests.get('http://api.openweathermap.org/data/2.5/weather?q=' + cidade + '&app')

tempo = json.loads(requisicao.text)

print('Condicao do tempo:', tempo['weather'][0]['main'])
print('Temperatura', float(tempo['main']['temp']) - 273.15)