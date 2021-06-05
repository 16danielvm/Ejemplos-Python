<<<<<<< HEAD
import os

option = 0
num = int(input("Digite el numero "))



while option!= -1:
    print("\n==============MENÚ==============")
    print("\nDigite una de las opciones")
    print("\n1. Par o Impar")
    print("2. Primo")
    print("3. Perfecto")
    print("Presione -1 para salir del menú")
    option=int(input("Digite la opción que desea "))

    if option==1:
        os.system('cls')
        if (num%2)==0:
            print(num, "\nes par")
        else:
            print(num, "\nes impar")
    elif option==2:
        os.system('cls')
        div=1
        sumaDiv=0
        while div<=num:
            if num%div==0:
                sumaDiv+=1
            div+=1
        else:
            if sumaDiv==2:
                print(num, "\nes numero primo")
            else:
                print(num, "\nno es numero primo")
    elif option==3:
        os.system('cls')
        div=1
        sumaDiv=0
        while div<num:
            if (num%div)==0:
                sumaDiv+=div
            div+=1
        else:
            if num==sumaDiv:
                print(num, "\nes numero perfecto")
            else:
                print(num, "\nno es numero perfecto")
    elif option==-1:
        os.system('cls')
        print("\nMuchas gracias por usar el software ...")
    else:
=======
import os

option = 0
num = int(input("Digite el numero "))



while option!= -1:
    print("\n==============MENÚ==============")
    print("\nDigite una de las opciones")
    print("\n1. Par o Impar")
    print("2. Primo")
    print("3. Perfecto")
    print("Presione -1 para salir del menú")
    option=int(input("Digite la opción que desea "))

    if option==1:
        os.system('cls')
        if (num%2)==0:
            print(num, "\nes par")
        else:
            print(num, "\nes impar")
    elif option==2:
        os.system('cls')
        div=1
        sumaDiv=0
        while div<=num:
            if num%div==0:
                sumaDiv+=1
            div+=1
        else:
            if sumaDiv==2:
                print(num, "\nes numero primo")
            else:
                print(num, "\nno es numero primo")
    elif option==3:
        os.system('cls')
        div=1
        sumaDiv=0
        while div<num:
            if (num%div)==0:
                sumaDiv+=div
            div+=1
        else:
            if num==sumaDiv:
                print(num, "\nes numero perfecto")
            else:
                print(num, "\nno es numero perfecto")
    elif option==-1:
        os.system('cls')
        print("\nMuchas gracias por usar el software ...")
    else:
>>>>>>> 38d34672c7ec75fb6e8270988a8f22c942e32c22
        print("\nNo es un numero valido")