from abc import ABC, abstractmethod


class Department:

    def __init__(self, name, code):
        self.__name = name  # Recebe o nome do departamento
        self.__code = code  # Recebe o codigo do departamento

    def get_name(self):  # Retorna o nome do departamento
        return self.__name

    def set_name(self, nome):  # Altera o nome do departamento
        self.__name = nome


class Employee(ABC):

    def __init__(self, code, name, salary):
        self.__code = code  # Recebe o código do empregado
        self.__name = name  # Recebe o nome do empregado
        self.__salary = salary  # Recebe o salario do empregado
        self.__horas = 8  # horario fixo para cada empregado

    @abstractmethod
    def calc_bonus(self):
        return self.__salary * 0.15

    def get_hours(self):
        return self.__horas


class Manager(Employee):

    def __init__(self, code, name, salary):
        super().__init__(code, name, salary)
        # Instancia a classe Department
        self.__departament = Department('managers', 1)
        self.salary = salary

    def calc_bonus(self):
        return self.salary * 0.15

    def get_department(self):
        return self.__departament.get_name()

    def set_department(self, nome):
        self.__departament.set_name(nome)


class Seller(Employee):

    def __init__(self, code, name, salary):
        super().__init__(code, name, salary)
        self.__departament = Department('sellers', 2)
        self.__sales = 0

    def calc_bonus(self):
        return self.get_sales() * 0.15

    def get_sales(self):
        return self.__sales

    # Acumula na variável vendas o valor de cada venda
    def put_sales(self, valores):
        valor = self.__sales + valores
        self.__sales = valor

    def get_department(self):
        return self.__departament.get_name()

    def set_department(self, nome):
        self.__departament.set_name(nome)
