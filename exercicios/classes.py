class Animal:
    def fazer_parulho(self):
        print("Esse animal faz barulho")

class Mamifero(Animal):
    def tem_pelos(self):
        return True
class Animal_domestico():
    def dorme(self):
        return True

class Cachorro(Mamifero,Animal_domestico):
    def bagunca(self):
        print("Sim")

class Gato(Mamifero):
    def fazer_parulho(self):
        print("Miau ... miau")

cachorro = Cachorro()
print(cachorro.dorme())
print(cachorro.tem_pelos())
print(cachorro.bagunca())