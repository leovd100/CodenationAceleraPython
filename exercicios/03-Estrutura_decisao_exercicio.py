idade = 20

if idade < 18:
    print('Menor de idade')
else:
    print('Maior de idade')


veiculo = {
    'Tipo':'moto',
    'Marca':'Honda',
    'Potencia':140
}

if veiculo['Tipo'] == 'moto' and veiculo['Marca'] == 'Honda':
    print('O veículo é uma Moto')
else:
    print('O veículo é um Carro')

if veiculo['Tipo'] == 'moto' or  veiculo['potencia_motor'] < 120:
    print("Você tem um veículo muito rápido")
else:
    print('Seu veículo não é rápido')


condicao = [1,2,3]

if len(condicao):
    print('verdadeiro')
else:
    print('falso')

print(len(condicao))
