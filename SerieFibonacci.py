def Fibonacci(n=2):
    """
    Muestra la cantidad de números de la serie Fibonacci que el usuario desea.

    Args:
        n(int, optional): Es el argumento que determina la cantidad de números que mostrara la función.
    
    Returns:
        int

    Notes:
        En la serie Fibonacci el primer y segundo término de la sucesión son 0 y 1, los siguientes términos se obtienen sumando los dos términos que les preceden.
        Ejm: 0,1,2,3,5,8,13...

    """
    i=0
    a=0
    b=1
    print(a)
    while i<=n-2:
        c=a+b
        print(c)
        a=b
        b=c
        i+=1
