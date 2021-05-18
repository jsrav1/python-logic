from cliente import Cliente
from conta import Conta


cliente1 = '0'

usuariocpf = input("\nQual o seu CPF? \n")
if len(usuariocpf) <= 11:
    usuariocpf = usuariocpf.zfill(11)
    cpf = '{}.{}.{}-{}'.format(usuariocpf[:3],
                           usuariocpf[3:6], usuariocpf[6:9], usuariocpf[9:])
else:
    cpf = usuariocpf


if cpf == '123.456.789-10':
    cliente1 = Cliente('Rainer', '123.456.789-10', 24)

    print('\nMEU PERFIL:', cliente1)

    conta_do_rainer = Conta(cliente1, 10.50)

    print('Saldo:', conta_do_rainer.consulta_saldo())

    while True:
        operacao = int(input('\nEscolha o que deseja: \n[1] DEPOSITO\n[2] RETIRADA\n[3] SAIR\n\n'))

        if operacao == 1:
            vlrdeposito = input('\nQual o valor que quer depositar? \n')
            conta_do_rainer.depositar(float(vlrdeposito))
        elif operacao == 2:
            vlrsacar = input("\nQual o valor que quer retirar? \n")
            conta_do_rainer.sacar(float(vlrsacar))
        elif operacao == 3:
            print('\nVoce saiu.\n')
            break
        else:
            print('\nEsta opção não é valida')

else:
    print("Esse usuario não existe")
    


