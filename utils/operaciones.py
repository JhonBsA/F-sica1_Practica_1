import math

# Calcula la suma total de los componentes X y Y
def sumar_vectores(lista_vectores):
    suma_x = sum(v['x'] for v in lista_vectores)
    suma_y = sum(v['y'] for v in lista_vectores)
    return {'x': suma_x, 'y': suma_y}

def calcular_magnitud_angulo(vector):
    x = vector['x']
    y = vector['y']
    magnitud = math.sqrt(x**2 + y**2)
    angulo = math.degrees(math.atan2(y, x)) % 360
    return magnitud, angulo