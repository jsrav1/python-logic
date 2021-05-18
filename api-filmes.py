import requests
import json

def requisicao(titulo):
    try: 
        req = requests.get('https://www.omdbapi.com/?t=' + titulo)
        dicionario = json.loads(req.text)
        return dicionario
    except:
        print('Erro de conexão')
        return None

def printar_detalhes(filme):
    print('Título:', filme['Title'])
    print('Ano:', filme['Year'])
    print('Diretor:', filme['Director'])
    print('Atores:', filme['Actors'])
    print('Nota:', filme['imbdRating'])
    print('')

sair = False
while not sair:
    op = input('Escreva o nome de um filme ou SAIR para fechar: ')
    if op == 'SAIR':
        sair = True
    else:
        filme = requisicao(op)
        if filme['Response'] == 'False':
            print('Filme não encontrado')
        else:
            printar_detalhes(filme)




