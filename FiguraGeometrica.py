'''
Python Posee una idea para la clase abstracta por lo que es interesante como se planntea la idea de python

'''

#ABC = Abstract Base Class: con esto ya python dispone de un biblioteca para utlizar las clases abstractas
from abc import ABC, abstractmethod

class FiguraGeometrica(ABC):
    def __init__(self, ancho, alto):
        if self._validar_valor(ancho):
            self._ancho = ancho
        else:
            self._ancho = 0
            print(f'Valor erroneo ancho: {ancho}')
        if self._validar_valor(alto):
            self._alto = alto
        else:
            self._alto = 0
            print(f'Valor erroneo alto: {alto}')

    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, ancho):
        if self._validar_valor(ancho):
            self._ancho = ancho
        else:
            print(f'Valor erroneo ancho: {ancho}')

    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, alto):
        if self._validar_valor(alto):
            self._alto = alto
        else:
            print(f'Valor erroneo alto: {alto}')

    #Metodo obstracto que permite la ejecucion de codigo en las clases hijas, Pero es una clase abstracta y lo interesante es que
    #Este es un metodo padre de las clase abstracta. Por lo que es interesante, que la idea. apesar de los pequeños casos de cambio
    #El codigo sigue funcionando.
    @abstractmethod
    def calcular_area(self):
        pass

    def __str__(self):
        return f'FiguraGeometrica [Ancho: {self._ancho}, Alto: {self.alto} ]'

    def _validar_valor(self, valor):
        return True if 0 < valor < 10 else False