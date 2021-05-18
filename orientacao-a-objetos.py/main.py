from veiculo import Veiculo
from carro import Carro


caminhao_rosa = Veiculo('Rosa', 6, 'Ford', 10)

print("CAMINHÃO ROSA")
print("Cor: ", caminhao_rosa.cor)
print("Marca: ", caminhao_rosa.marca)
print("Tanque: ", caminhao_rosa.tanque)



carro_azul = Carro('Azul', 'Bmw', 30)

print("\n CARRO AZUL")
print("Cor: ", carro_azul.cor)
print("Marca: ", carro_azul.marca)
print("Tanque: ", carro_azul.tanque)
carro_azul.abastecer(10)
print("Tanque", carro_azul.tanque)
carro_azul.abastecer(70)
print("Tanque", carro_azul.tanque)

caminhao_rosa.abastecer(100)
print("Tanque", caminhao_rosa.tanque)