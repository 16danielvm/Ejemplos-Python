'''
Una empresa tiene un numero n de empleados y tiene la siguiente informacion: cedula, nombre, numero de hijos, salario por hora y numero de horas trabajadas semanales, retencion de empleados se calcula:
- Para los salarios menores a 1300000: si el numero de hijos es mayor a 3 no se le retiene si el numero de hijos es menor o igual a 3 se le retiene el 5% por cada hijo.
- Para salarios mayores o iguales a 1300000 sie el numero de hijos es menor a 2, se le retiene un 10% si es mayor o igual a 2 se le retiene un porcentaje igual a 15/el numero de hijos
- Por cada hijo la empresa le subsidia 20000
Elabore un programa que muestre: cedula, nombre del trabajador, salario devengado, retencion, subsidio, y total a pagar
'''


option = 0

while option==0:

    nombre = input("Digite Nombre: ")
    cedula = int(input("Digite Cedula: "))
    n_hijos = int(input("Numero de hijos: "))
    salario_h = 3500
    h_trabajadas = int(input("Horas laboradas semanales: "))
    salario = (salario_h*h_trabajadas)*4

    if salario< 1300000:
        if n_hijos>3:
            retencion=0
        else:
            retencion=salario*0.05
    else:
        if n_hijos<2:
            retencion=salario*0.10
        else:
            retencion= salario*((15/n_hijos)/100)
    print("\n=======Datos del empleado======")
    print("Nombre: ", nombre)
    print("Cedula: ", cedula)
    print("Salario devengado: ", salario)
    print("Retencion: ", retencion)
    print("Subsidio: ", n_hijos*20000)
    print("Total a pagar: ", salario+(n_hijos*20000)-retencion)

    ing = input("Desea ingresar otro empleado? S/N")
    if ing=="S":
        option=0
    else:
        option=1