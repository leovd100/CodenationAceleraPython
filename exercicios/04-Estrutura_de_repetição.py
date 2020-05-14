for i in range(10):
    print(i)


print('='*10,end='')
print('Lista de convidados',end='')
print('='*10)

convidados = ['Leonardo','Maria','Vincius','Guilherme','Laura']

for convidado in convidados:
    print(f'{convidado} : Está convidado')


print('\n'+'='*10,end='')
print('Usando Len',end='')
print('='*10+'\n')

for i in range(len(convidados)):
    convidado = convidados[i]
    print(f'{convidado} : Está convidado')


print('\n'+'='*10,end='')
print('While',end='')
print('='*10+'\n')

saida = True
contador = 0

while saida:
    contador += 1
    if contador == 5:
        saida = False

print('Contador : {}'.format(str(contador)))

