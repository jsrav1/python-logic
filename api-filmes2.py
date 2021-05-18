import requests
import json
import time

def listas_filmes(titulo):
    lista = []
    for i in range(1,100):
        try:
            print('Pesquisando em pagina:', i)
            url = requests.get('http://www.omdbapi.com/?s=') + titulo + '&type=movie&page='
            req = requests.get(url)
            resposta = json.loads(req.text)
            if resposta['Response'] == 'True':
                for filme in resposta['Search']:
                    tit = filme['Title']
                    ano = filme['Year']
                    string = tit + ' (' + ano + ')'
                    lista.append(string)
            else:
                print('Fim das paginas')
                break
            
        except:
            print('Conexão Falhou')
    return lista

sair = False
while not sair:
    op = input('Pesquise por um filme ou digite SAIR')
    if op == 'SAIR':
        sair = True
    else:
        lista_de_filmes = listas_filmes(op)
        print('Filmes encontrados:', len(lista_de_filmes))
        for filme in lista_de_filmes:
            print(filme)