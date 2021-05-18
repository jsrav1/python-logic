arquivo = open( )

for i in range(0,1000):
    arquivo.write(str(i)+'\n')



arquivo = open('logo.png', 'rb')
print(arquivo.read())