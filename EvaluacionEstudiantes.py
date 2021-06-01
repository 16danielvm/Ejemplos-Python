contAprobados=0
contReprobados=0

option=""
contEstudiantes=0
promedioCurso=0

while option!="NO":
    contEstudiantes+=1
    print("Estudiante", contEstudiantes)
    nombre=input("nombre:")
    codigo=int(input("codigo:"))
    nota1=eval(input("nota1:"))
    while nota1<0 or nota1>5:
        nota1=eval(input("nota1:"))

    nota2=eval(input("nota2:"))
    while nota2<0 or nota2>5:
        nota2=eval(input("nota2:"))

    nota3=eval(input("nota3:"))
    while nota3<0 or nota3>5:
        nota3=eval(input("nota3:"))


    notaDef=nota1*0.2+nota2*0.3+nota3*0.5
    promedioCurso+=notaDef

    if notaDef>=3:
        contAprobados+=1
    else:
        contReprobados+=1    
        
    print("\nNota definitiva estudiante:", notaDef)    
    print("El número de estudiantes aprobados:", contAprobados)    
    print("El número de estudiantes reprobados:", contReprobados)    
    option=input("Desea continuar SI/NO: ")
else:
    promedioCurso/=contEstudiantes
    print("Promedio del curso", promedioCurso)
    print("Porcentaje de aprobados del curso:",100*contAprobados/contEstudiantes,"%")
    print("Porcentaje de reprobados del curso:", 100*contReprobados/contEstudiantes,"%")