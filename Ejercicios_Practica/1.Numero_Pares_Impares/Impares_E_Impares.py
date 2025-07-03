#Ejercicio para numeros pares e impares
# Autor: KamiroDark

"""Este programa permite al usuario ver números pares e impares
   hasta un número máximo ingresado, o verificar si un número específico
   es par o impar. El usuario puede elegir entre varias opciones"""

def welcome():
    while True:
        print("")
        print("Que deseas hacer? \n")
        print("1. Ver numeros pares")
        print("2. Ver numeros impares")
        print("3. Ingresar un numero para ver si es par o impar")
        print("4. Salir del programa")

        opcion = input("Ingrese una opcion: ")
        if opcion == "1":
            even_numbers()
        elif opcion == "2":
            odd_numbers()
        elif opcion == "3":
            verify_number()
        elif opcion == "4":
            print("Gracias por usar el programa. ¡Hasta luego!")
            break


def even_numbers():
    while True:
        print("Ingrese el numero maximo hasta el cual desea ver los numeros pares:")
        try:
            number = int(input())
            for i in range(0, number + 1):
                if i % 2 == 0:
                    print(i)
            break        
        except ValueError:
            print("Por favor, ingrese un numero valido.")

def odd_numbers():
    while True:
        try:
            print("Ingrese el numero maximo hasta el cual desea ver los numeros impares:")
            number = int(input())
            for i in range(0, number + 1):
                if i % 2 != 0:
                    print(i)
            break
        except ValueError:
            print("Por favor, ingrese un numero valido.")

def verify_number():
    while True:
        try:
            print("Ingrese un numero para verificar si es par o impar:")
            number = int(input())
            if number % 2 == 0:
                print("El numero", number, "es par.")
            else:
                print("El numero", number, "es impar.")
            break
        except ValueError:
            print("Por favor, ingrese un numero valido.")

print("Bienvenido al programa de pares e impares! \n By KamiroDark")
welcome()