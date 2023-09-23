import math

def circulo(radio):
    return math.pi * radio ** 2

radio1 = 3
radio2 = 4

circulo1 = circulo(radio1)
circulo2 = circulo(radio2)

print("el area del circulo uno es: ", circulo1)
print("el area del segubdo circulo es: ", circulo2)

def rectangulo(ancho, largo):
    return ancho * largo

ancho1 = 3
largo1 = 3

ancho2 = 4
largo2 = 5

area1 = rectangulo(ancho1, largo1)
area2 = rectangulo(ancho2, largo2)

print("El área del primero es:", area1)
print("El área del segundo es:", area2)