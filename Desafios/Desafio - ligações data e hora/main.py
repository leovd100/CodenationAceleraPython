from datetime import datetime,time
from operator import itemgetter
import math
records = [
    {'source': '48-996355555',
     'destination': '48-666666666',
     'end': 1564610974,
     'start': 1564610674},

    {'source': '41-885633788',
     'destination': '41-886383097',
     'end': 1564506121,
     'start': 1564504821},

    {'source': '48-996383697',
     'destination': '41-886383097',
     'end': 1564630198,
     'start': 1564629838},

    {'source': '48-999999999',
     'destination': '41-885633788',
     'end': 1564697158,
     'start': 1564696258},

    {'source': '41-833333333',
     'destination': '41-885633788',
     'end': 1564707276,
     'start': 1564704317},

    {'source': '41-886383097',
     'destination': '48-996384099',
     'end': 1564505621,
     'start': 1564504821},

    {'source': '48-999999999',
     'destination': '48-996383697',
     'end': 1564505721,
     'start': 1564504821},

    {'source': '41-885633788',
     'destination': '48-996384099',
     'end': 1564505721,
     'start': 1564504821},

    {'source': '48-996355555',
     'destination': '48-996383697',
     'end': 1564505821,
     'start': 1564504821},

    {'source': '48-999999999',
     'destination': '41-886383097',
     'end': 1564610750,
     'start': 1564610150},

    {'source': '48-996383697',
     'destination': '41-885633788',
     'end': 1564505021,
     'start': 1564504821},

    {'source': '48-996383697',
     'destination': '41-885633788',
     'end': 1564627800,
     'start': 1564626000}
]
def calcularValores(inicio,fim):
    inicio = datetime.fromtimestamp(inicio)
    fim = datetime.fromtimestamp(fim)
  
    if inicio.hour > 22 or fim.hour < 6:
        return 0.36
    
    if fim.hour >= 22:
        fim = datetime(fim.year,fim.month,fim.day,22)
    if inicio.hour < 6:
        inicio = datetime(inicio.year,inicio.month,inicio,6)

    duracao = math.floor((fim - inicio).seconds/60)
    preco = (duracao*0.09) + 0.36
    return preco


def separar(records):
    resultado = [] 

    for record in records:
        i = False
        for result in resultado:
            if record['source'] == result['source']:
                i = True               
                anterior = result['total']
                preco = calcularValores(record['start'],record['end'])
                update = round((anterior + preco),2)
                result['total'] = update
        if i == False:  
            preco =  calcularValores(record['start'],record['end'])
            resultado.append({'source' : record['source'],'total': round(preco,2)})
    total = sorted(resultado, key=itemgetter('total'), reverse=True)
    return total



def classify_by_phone_number(records):
    return separar(records)





#-----------------------------------------------

