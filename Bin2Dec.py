def Bin2Dec(N=0):
    """
        La función convierte cualquier numero binario en su equivalente en código decimal.
    
        Args:
            N(int,opcional)
        
        Returns
            Int: Regresa en código decimal el número en binario a convertir.and
        
        Raises:
            ValueError: Al no digitar un numero binario en decimal, o una cadena de caracteres.
    """
    N1 = str(N)
    suma = 0
    loop = len(N1)
    val = True
    for i in range(loop-1,-1,-1):
        if N1[i] == "1":
            j = (len(N1)-1)-i
            suma = suma+(2**j)
        elif N1[i] == "0":
            suma = suma+0
        else:
            val = False
            break;
    if val == True:
        print("El numero",N,"en decimal es:",suma)
    else:
        print("El numero debe ser binario")

