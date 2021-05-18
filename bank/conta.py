import time

class Conta:

    def __init__(self, cliente, saldo):
        self.cliente = cliente
        self.saldo = saldo
    
    def depositar(self, quant):
        
            if quant > 0:
                self.saldo += quant
                print('Deposito sendo processado...')
                time.sleep(3)
                print('Voce depositou R$',quant, '\n' 'Seu novo saldo é de: R$', self.saldo)
                time.sleep(3)
                
            else:
                print('Erro no deposito')
                

    def consulta_saldo(self):
        return self.saldo

    def sacar(self,quant):
        if self.saldo - quant < 0:
            print('Saldo insuficiente.')
        elif quant <= 0:
            print('Erro na retirada')
        else:
            print('Saque sendo processado...')
            self.saldo -= quant
            time.sleep(3)
            print('Saque de R$', quant, '\n' 'Seu novo saldo é de: R$', self.saldo, )
            time.sleep(1)
             