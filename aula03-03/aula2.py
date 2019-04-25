class AnimalEstimacao():
    def __init__(self, nome, especie, dono):
        self.nome = nome
        self.especie = especie
        self.dono = dono

    def __str__(self):
        return self.nome

import aula2 as animal 

isabellita = animal.AnimalEstimacao('Isabellita', 'Capivara','Teste')

class Calculadora():
    def __init__(self,a,b):
        self.a = a
        self.b = b
    
    def somar(self):
        return self.a + self.b

    def dividir(self):
        return self.a / self.b

    def multiplicar(self):
        return self.a * self.b

    def subtrair(self):
        return self.a - self.b