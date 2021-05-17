def FibonacciModificada(n=3):
    """
    Muestra la cantidad de números de la serie Fibonacci "modificada que el usuario desea.

    Args:
        n(int, optional): Es el argumento que determina la cantidad de números que mostrara la función.
    
    Returns:
        int

    Notes:
        En la serie Fibonacci el primer y segundo término de la sucesión son 0 y 1, los siguientes términos se obtienen sumando los dos términos que les preceden.
        Ejm: 0,1,2,3,5,8,13...
        Pero en este caso cierta sucesión parte de los números 0,1,1. De ahí en adelante los nuevos términos se forman mediante la suma de los tres términos inmediatamente anteriores, asi: 0,1,1,2,4,7,13,24
    
    """
    i=0
    a=0
    b=1
    c=1
    print(a)
    print(b)
    while i<=n-3:
        d=a+b+c
        print(c)
        a=b
        b=c
        c=d
        i+=1

FibonacciModificada(27)