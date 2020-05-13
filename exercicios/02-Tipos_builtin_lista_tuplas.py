lista_de_convidados = ['Leonardo','Bianca','Lais','Daniel']

print(lista_de_convidados)

lista_de_convidados.append('Eliete')

print(lista_de_convidados)

li_nova = ['Guilherme','Gustavo','Jéssica']
for x in li_nova:
    lista_de_convidados.append(x)

print(lista_de_convidados)
#------------remover------------
lista_de_convidados.remove('Bianca')
print(lista_de_convidados)

print(lista_de_convidados[0])
print(lista_de_convidados[-1])


lista_de_convidados.append(50)
print(lista_de_convidados)


#Tuple
tupla1 = (1,2,3,4,5)
tupla2 = (6,7,8,9)
tupla3 = tupla1 + tupla2
print(tupla1)
print(tupla2)
print(tupla3)

#Dicionario estrutura de chave valor parecida com JSON

dados_pessoais = {
    'Nome'  :'Leonardo',
    'Idade' :22,
    'Altura': 1.70,
    'Comida': 'macarrão'
}

print(dados_pessoais)
print(dados_pessoais['Nome'])
print(dados_pessoais['Idade'])
print(dados_pessoais['Altura'])
print(dados_pessoais['Comida'])

dados_pessoais['programacao'] = 'Python'
print(dados_pessoais['programacao'])