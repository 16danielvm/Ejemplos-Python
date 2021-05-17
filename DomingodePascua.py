from datetime import date

def DomingodePascua(year= date.today().year):
    """
        La función toma como argumento un año y muestra la fecha(dia,mes,año) del Domingo de pascua del año seleccionado.

        Args:
            year(date.year): Debe ser un año.
        
        Return:
            String: N "del mes", año
        
        Raises:
            TypeError: Cuando el argumento sea una cadena de caracteres

    """

    A = year % 19
    B = year % 4
    C = year % 7
    D = (19 * A + 24 )% 30
    E = (2*B + 4*C + 6*D + 5 ) % 7
    N = (22 + D + E)

    if N <= 31:
        print(N, "de Marzo de,", year)
    else:
        print(N-31, "de Abril,", year)

