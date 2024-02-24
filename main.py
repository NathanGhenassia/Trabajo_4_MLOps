# Funcion Saludo Personalizado
def saludo_personalizado():
    nombre = input("Ingrese su nombre: ")
    print(f"Hola, {nombre}! Bienvenido/a.")


# Funcion Contador de Números


# Funcion Calculadora Básica


# Menú Principal
if __name__ == '__main__':
    while True:
        print("\n1. Saludo Personalizado")
        print("2. Contador de Números")
        print("3. Calculadora Básica")
        print("4. Salir")
        opcion = input("Seleccione una opción (1-4): ")

        if opcion == '1':
            saludo_personalizado()
        elif opcion == '4':
            break
        else:
            print("Opción no válida. Intente de nuevo.")