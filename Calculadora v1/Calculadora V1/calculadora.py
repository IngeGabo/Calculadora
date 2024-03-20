def sumar(x, y):
    return x + y

def restar(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    # Verificamos si y es cero para prevenir la división por cero.
    if y == 0:
        raise ValueError("No se puede dividir por cero.")
    return x / y

def calculadora():
    while True:
        print("Operaciones disponibles: \n1. Sumar\n2. Restar\n3. Multiplicar\n4. Dividir\n5. Salir")
        try:
            opcion = int(input("Selecciona una operación: "))
            if opcion == 5:
                print("Saliendo de la calculadora...")
                break
            elif opcion < 1 or opcion > 5:
                print("Por favor, ingresa una opción válida.")
                continue

            x = float(input("Ingresa el primer número: "))
            y = float(input("Ingresa el segundo número: "))

            if opcion == 1:
                print("Resultado:", sumar(x, y))
            elif opcion == 2:
                print("Resultado:", restar(x, y))
            elif opcion == 3:
                print("Resultado:", multiplicar(x, y))
            elif opcion == 4:
                print("Resultado:", dividir(x, y))
        except ValueError as e:
            print("Error: Entrada inválida. Por favor, ingresa números válidos.", e)
        except Exception as e:
            print("Ha ocurrido un error inesperado.", e)

calculadora()
