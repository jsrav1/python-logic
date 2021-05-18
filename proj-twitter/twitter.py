import oauth2
import urllib
import json

class Twitter:
    # funcao inicial
    def __init__(self, consumer_key, cpnsumer_secret, token_key, token_secret):
        self.conexao(consumer_key, cpnsumer_secret, token_key, token_secret)

    # funcao de conexao
    def conexao(self, consumer_key, consumer_secret, token_key, token_secret):
        self.consumer = oauth2.Consumer(consumer_key, consumer_secret)
        self.token = oauth2.Token(token_key, token_secret)
        self.cliente = oauth2.Client(self.consumer, self.token)

    # requisicao
    def post_twitter(self, novo_twitter):
        query = urllib.parse.quote(novo_twitter, safe='')
        # o cliente é retornado pelo main o novo objeto twitter
        requisicao = self.cliente.requests('http://api.twitter.com/1.1/status/update.json?status='+ query,
                                           method='POST')
        decodificar = requisicao[1].decoder()
        objeto = json.loads(decodificar)
        return objeto

    # pesquisar
    def search_twitter(self, query, lang):
        query_codificada = urllib.parse.quote(query, safe='')
        requisicao = self.cliente.request('http://api.twitter.com/1.1/search/tweets.json?q='+ query_codificada+
                                          '&lang='+ lang)
        decodificar = requisicao[1].decode()
        objeto = json.loads(decodificar)
        twitters = objeto['statuses']
        return twitters