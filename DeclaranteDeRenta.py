'''
Planteamiento de la situación

En Colombia una persona es declarante de renta cuando sus ingresos totales del año gravable sean igual o superiores a $49.850.000. La Universidad Industrial de Santander (UIS) tiene una lista de trabajadores donde conoce: su nombre, cedula, pago por hora y número de horas trabajadas semanales. La UIS desea conocer cuántos y cuáles de sus empleados están en obligación de declarar renta. En caso de declarar renta avisarle la fecha que deben declarar de acuerdo con el calendario establecido por la DIAN. Asuma que un año tiene 48 semanas.

Últimos dos dígitos:

Entre el 00 y 20                   Declarar antes de agosto 24

Entre el 21 y 40                   Declarar antes de septiembre 24

Entre el 41 y 60                   Declarar antes de octubre 24

Entre el 61 y 80                   Declarar antes de noviembre 24

Entre el 81 y 99                   Declarar antes de diciembre 24


Requerimientos del reto

El aplicativo debe cumplir los siguientes requerimientos: 

1.Solicitar nombre. 

2.Solicitar cédula. 

3. Solicitar pago por hora

4. Solicitar el número de horas trabajadas semanales

'''

cont=0
n=1

while n<=3:

    nombre = input()
    cedula = input()
    p_hora = int(input())
    h_trabajadas = int(input())


    ingreso_anual = p_hora*h_trabajadas*53

    if ingreso_anual>=49850000:
        cont+=1
        print(nombre, "es declarante de renta")
        digito = int(cedula[5]+cedula[6])
        if 21<=digito<=40:
            print("Declarar antes de septiembre 24") 
        elif 41<=digito<=60:
            print("Declarar antes de octubre 24") 
        elif 61<=digito<=80:
            print("Declarar antes de noviembre 24") 
        elif 81<=digito<=99:
            print("Declarar antes de diciembre 24") 
        else:
            print("Declarar antes de agosto 24") 
    else:
        print(nombre, "no es declarante de renta")
    
    n+=1

print("Total declarantes de renta:", cont)


