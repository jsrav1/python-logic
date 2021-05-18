import requests

cabecalho = {'User-agent': 'Windows 12', 
             'Referer': 'https://google.com',
             'cf-ipcountry': 'US'}

meus_cookies = {'Ultima-visita': '10-10-2020'}

dados = {'username':'rainer',
         'password': 'rainer123'}

texto = None

try:
    requisicao = requests.get('https://putsreq.com/qMEEjaNQVhhukZBd62FY',
    headers = cabecalho,
    cookies = meus_cookies,
    data = dados)


    texto = requisicao.text

except Exception as e:
    print('Requisição deu erro:', e)

print(texto)