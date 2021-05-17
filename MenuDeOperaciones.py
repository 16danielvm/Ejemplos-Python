
from os import system

"""
    El usuario digita 2 numeros cualquiera y el codigo despliega un menú de opciones para realizar alguna de las 4 operaciones básicas entre dichos números.

    Args:
        a(int)
        b(int)

    Returns:
        float: Resultado de la operación

    Raises:
        ValueError: Al digitar numeros no enteros o caracteres.

"""

option = 0
a = int(input("Digite el primer numero "))
b = int(input("Digite el segundo numero "))

while option!= -1:
    print("\n==============MENÚ==============")
    print("\nDigite una de las opciones")
    print("\n1. Suma")
    print("2. Resta")
    print("3. Multiplicar")
    print("4. Dividir")
    print("Presione -1 para salir del menú")
    option=int(input("Digite la opción que desea "))

    if option==1:
        system("cls")
        print("\nSuma:", a+b)
    elif option==2:
        system("cls")
        print("\nResta:", a-b)
    elif option==3:
        system("cls")
        print("\nMultiplicación:", a*b)
    elif option==4:
        if b!=0:
            system("cls")
            print("\nDivision:", a/b)
        else:
            system("cls")
            print("\nNo es posible la división por cero")
            b = int(input("\nIngrese el nuevo valor de b "))
    elif option==-1:
        system("cls")
        print("\nMuchas gracias por usar el software ...")
    else:
        system("cls")
        print("\nNo es un numero valido")