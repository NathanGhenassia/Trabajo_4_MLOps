# Funcion Saludo Personalizado
def saludo_personalizado():
    nombre = input("Ingrese su nombre: ")
    print(f"Hola, {nombre}! Bienvenido/a.")


# Funcion Contador de Números
def contador_numeros():
    numero = int(input("Ingrese un número entero positivo: "))
    for i in range(1, numero + 1):
        print(i)

# Funcion Calculadora Básica
def calculadora_basica():
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    operacion = input("Ingrese la operación (+, -, *, /): ")

    if operacion == '+':
        resultado = num1 + num2
    elif operacion == '-':
        resultado = num1 - num2
    elif operacion == '*':
        resultado = num1 * num2
    elif operacion == '/':
        resultado = num1 / num2
    else:
        print("Operación no válida")
        return

    print(f"Resultado: {resultado}")

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
        elif opcion == '2':
            contador_numeros()
        elif opcion == '3':
            calculadora_basica()
        elif opcion == '4':
            break
        else:
            print("Opción no válida. Intente de nuevo.")