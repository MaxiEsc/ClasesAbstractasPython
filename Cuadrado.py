'''No habra diferencia en las clases Hijas'''

from FiguraGeometrica import FiguraGeometrica
from Color import Color

class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado, color):
        # super().__init__(lado)
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)

    # Este metodo al derivar de una clase abstracta debe ser si o si implementado en las clases hijas, de lo contrario sera imposible
    # realiza una instacia del metodo. por eso es importante que esta ultima lo implemente.
    def calcular_area(self):
        return self.alto * self.ancho

    def __str__(self):
        return f'{FiguraGeometrica.__str__(self)} {Color.__str__(self)}'
