from datetime import date

def Ano_Bisiesto(year= date.today().year):
    """
        La función toma como argumento un año y muestra si dicho año es bisiesto o no.

        Args:
            year(date.year): Debe ser un año.
        
        Return:
            String: Si es bisiesto o no
        
        Raises:
            TypeError: Cuando el argumento sea una cadena de caracteres

    """
    if year%4!=0:
        print(year, "no es bisiesto")
    elif year%4==0 and year%100!=0:
        print(year, "es bisiesto")
    elif year%4==0 and year%100==0 and year%400!=0:
        print(year, "no es bisiesto")
    elif year%4==0 and year%100==0 and year%400==0:
        print(year, "es bisiesto")
