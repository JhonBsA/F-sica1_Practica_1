from utils.operaciones import calcular_magnitud_angulo

def imprimir_banner():
    print("=" * 40)
    print("        SUMA DE VECTORES EN 2D")
    print("=" * 40)

def imprimir_resultado_completo(lista_vectores, resultado):
    print("\n=== DETALLE DE VECTORES INGRESADOS ===")
    print("{:<10} {:>10} {:>10} {:>10} {:>10} {:>10}".format("Vector", "Magnitud", "Ángulo", "X", "Y", "Tipo"))

    for i, v in enumerate(lista_vectores, start=1):
        print("{:<10} {:>10} {:>10} {:>10} {:>10}   {}".format(
            f"# {i}",
            f"{v['m']:.2f}m",
            f"{v['a']:.2f}°",
            f"{v['x']:.2f}m",
            f"{v['y']:.2f}m",
            v['tipo']
        ))

    mag, ang = calcular_magnitud_angulo(resultado)

    print("\n=== VECTOR RESULTANTE ===")
    print(f"Magnitud total: {mag:.2f}m")
    print(f"Ángulo: {ang:.2f}°")
    print(f"Componente X: {resultado['x']:.2f}m")
    print(f"Componente Y: {resultado['y']:.2f}m")