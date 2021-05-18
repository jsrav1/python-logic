# EXERCICIO: Escreva uma função que recebe um objeto de coleção
# e retorna o valor do maior numero dentro dessa coleção
# Faça outra função que retorna o menor numero dessa coleção


def maior(colecao):
    maior_item = colecao[0]
    for item in colecao:
        if item > maior_item:
            maior_item = item
    return maior_item

maiornum = maior([15, 5, 0, 20, 10])
print('O maior item é: ', maiornum)


def menor(colecao):
    menor_item = colecao[0]
    for item in colecao:
        if item < menor_item:
            menor_item = item
    return menor_item

menornum = menor([15, 5, 0, 20, 10, -7])
print('O menor item é: ', menornum)
