import math

def solicitar_cantidad_vectores():
    while True:
        try:
            n = int(input("¿Cuántos vectores desea sumar?: "))
            if n <= 0:
                print("Debe ser un número mayor a 0.")
                continue
            return n
        except ValueError:
            print("Entrada inválida. Debe ser un número entero.")

def ingresar_vector():
    print("Seleccione método de entrada del vector:")
    print("1. Magnitud y dirección (en grados)")
    print("2. Componentes (x, y)")

    while True:
        opcion = input("Opción (1 o 2): ")
        if opcion == '1':

            magnitud = float(input("  Magnitud: "))
            direccion = float(input("  Dirección (°): "))

            # Convertir ángulo a radianes por trigonometría
            rad = math.radians(direccion)
            x = magnitud * math.cos(rad)
            y = magnitud * math.sin(rad)

            return {'x': x, 'y': y, 'm': magnitud, 'a': direccion, 'tipo': "Por magnitud"}
        elif opcion == '2':

            x = float(input("  Componente X: "))
            y = float(input("  Componente Y: "))
            magnitud = math.sqrt(x**2 + y**2)
            angulo = math.degrees(math.atan2(y, x)) % 360 # ángulo a 0-360°

            return {'x': x, 'y': y, 'm': magnitud, 'a': angulo, 'tipo': "Por componentes"}
        else:
            print("Opción inválida. Intente nuevamente.")
