from utils.entrada import solicitar_cantidad_vectores, ingresar_vector
from utils.operaciones import sumar_vectores
from utils.consola import imprimir_banner, imprimir_resultado_completo

def main():
    imprimir_banner()
    n = solicitar_cantidad_vectores()
    lista_vectores = []

    for i in range(n):
        print(f"\n--- Vector #{i + 1} ---")
        vector = ingresar_vector()
        lista_vectores.append(vector)

    resultado = sumar_vectores(lista_vectores)
    imprimir_resultado_completo(lista_vectores, resultado)

if __name__ == "__main__":
    main()