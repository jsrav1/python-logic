import time

def abre_arquivo():
    try:
        arquivo = open( )
        return True
    except Exception as erro:
        print("Aconteceu algum erro:", erro)
        return False

while not abre_arquivo():
    print('Tentando abrir o arquivo')
    time.sleep(5)

print('Consegui abrir o arquivo')