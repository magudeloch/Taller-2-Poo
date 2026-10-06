import math

class Circulo:
    def __init__(self, radio: float):
        self.radio = radio

    def calcular_area(self) -> float:
        return math.pi * (self.radio ** 2)

    def calcular_perimetro(self) -> float:
        return 2 * math.pi * self.radio

class Rectangulo:
    def __init__(self, base: float, altura: float):
        self.base = base
        self.altura = altura

    def calcular_area(self) -> float:
        return self.base * self.altura

    def calcular_perimetro(self) -> float:
        return 2 * (self.base + self.altura)

class Cuadrado:
    def __init__(self, lado: float):
        self.lado = lado

    def calcular_area(self) -> float:
        return self.lado ** 2

    def calcular_perimetro(self) -> float:
        return 4 * self.lado

class TrianguloRectangulo:
    def __init__(self, base: float, altura: float):
        self.base = base
        self.altura = altura

    def calcular_area(self) -> float:
        return (self.base * self.altura) / 2

    def calcular_hipotenusa(self) -> float:
        return math.hypot(self.base, self.altura)

    def calcular_perimetro(self) -> float:
        return self.base + self.altura + self.calcular_hipotenusa()

    def determinar_tipo_triangulo(self) -> str:
        hipotenusa = self.calcular_hipotenusa()
        lados = [self.base, self.altura, hipotenusa]

        if math.isclose(lados[0], lados[1]) and \
           math.isclose(lados[1], lados[2]):
            return "Equilatero"
        elif math.isclose(lados[0], lados[1]) or \
             math.isclose(lados[0], lados[2]) or \
             math.isclose(lados[1], lados[2]):
            return "Isosceles"
        else:
            return "Escaleno"

def main():
    circulo = Circulo(5.0)
    rectangulo = Rectangulo(4.0, 6.0)
    cuadrado = Cuadrado(4.0)
    triangulo = TrianguloRectangulo(3.0, 4.0)

    print("Circulo:")
    print(f"  Area: {circulo.calcular_area():.2f} cm2")
    print(f"  Perimetro: {circulo.calcular_perimetro():.2f} cm\n")

    print("Rectangulo:")
    print(f"  Area: {rectangulo.calcular_area():.2f} cm2")
    print(f"  Perimetro: {rectangulo.calcular_perimetro():.2f} cm\n")

    print("Cuadrado:")
    print(f"  Area: {cuadrado.calcular_area():.2f} cm2")
    print(f"  Perimetro: {cuadrado.calcular_perimetro():.2f} cm\n")

    print("Triangulo Rectangulo:")
    print(f"  Hipotenusa: {triangulo.calcular_hipotenusa():.2f} cm")
    print(f"  Area: {triangulo.calcular_area():.2f} cm2")
    print(f"  Perimetro: {triangulo.calcular_perimetro():.2f} cm")
    print(f"  Tipo: {triangulo.determinar_tipo_triangulo()}")

if __name__ == "__main__":
    main()