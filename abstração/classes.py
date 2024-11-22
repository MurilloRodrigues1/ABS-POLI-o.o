from abc import ABC, abstractmethod

class Funcionarios:

    def _init_(self, nome, idade, cpf, salario_base):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.salario = salario_base

    @abstractmethod
    def calcular_salario(self):
        pass

    def informacoes(self):
        return f"Nome: {self.nome} Idade: {self.idade} CPF: {self.cpf} Salario:R$ {self.calcular_salario():.2f}"
    
class Gerente(Funcionarios):

    def calcular_salario(self):
        return self.salario_base * 1.2

    def mostrar_info(funcionario: Funcionarios):
        print(funcionario.informacoes())
    
class Pião(Funcionarios):

    def calcular_salario(self):
        return self.salario_base * 1.2
    
    def mostrar_info(funcionario: Funcionarios):
        print(funcionario.informacoes())


gerente = Gerente("Pedro", 16, 47889719841, 2500)
piao = Pião("João Pincinato", 16, 12345678900, 2500)


Funcionarios.informacoes(gerente)
Funcionarios.informacoes(piao)