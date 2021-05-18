from twitter import Twitter

consumer_key = str(input('Consumer Key: '))
consumer_secret = str(input('Consumer Secret: '))
token_key = str(input('Token Key: '))
token_secret = str(input('Token Secret: '))
# criando um objeto do tipo twitter, passando a conexao
twitter = Twitter(consumer_key, consumer_secret, token_key, token_secret)

# postando pelo metodo, obtendo resposta
# resposta = twitter.post_twitter('Vamos testar nossa lib')
# print(resposta)
# pesquisando
pesquisa = twitter.search_twitter('solyd', 'pt')
# print(pesquisa)
for resultado in pesquisa:
    print(resultado['text'])
    print(resultado['user']['screen_name'])