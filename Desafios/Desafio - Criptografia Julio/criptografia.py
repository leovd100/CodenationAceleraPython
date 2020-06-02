import requests
import string
lista = []
response = requests.get('https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=8e31f890912b404a2f156ac619f31a5fea0da5b7')
ResponseJson = response.json()

# arquivo = open('answer.json','w')
# arquivo.write(str(ResponseJson))
# arquivo.close()
# for x,y in ResponseJson.items():
#     print(x,y)
lista = list(ResponseJson['cifrado'])
retorno = ''.join(lista).lower()
lista = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

listaNum = []

for x in range(25):
    listaNum.append(x)
print(listaNum)





for y,x in enumerate(lista):
    numero = 0
    if (y+12) > len(lista):
        numero = (len(lista)+1) - (y+1)
    print(y+1,end=' ')
    print(x,end = ' ')
    print(numero)