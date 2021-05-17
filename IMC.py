def IMC(estatura, peso):
    """
        Se toma la estatura y el peso para calcular el IMC

        Args:
            estatura(float): dato en metros(m)
            peso(float): dato en kilogramos(Kg)
        
        Return:
            String: Muestra lo que determina el valor calculado de IMC
        
        Raises:
            ValueError: Si los argumentos no son de tipo int o float
        
        Notes:
            El índice de masa corporal (IMC) es un número que se calcula con base en el peso y la estatura de la persona. Para la mayoría de las personas, el IMC es un indicador confiable de la gordura y se usa para identificar las categorías de peso que pueden llevar a problemas de salud.
        


    """
    imc= peso/(estatura**2)
    if imc <= 18.5:
        print("Bajo peso")
    elif (18.5 < imc < 24.9):
        print("Normal")
    elif (25.0 < imc < 26.9 ):
        print("Sobre peso grado I")
    elif (27.0 < imc < 29.9):
        print("Sobrepeso grado II")
    elif (30.0 < imc < 34.9):
        print("Obesidad de tipo I")
    elif (35.0 < imc < 39.9):
        print("Obesidad de tipo II")
    elif (40.0 < imc < 49.9):
        print("Obesidad de tipo III")
    else:
        print("Obesidad de tipo IV")

