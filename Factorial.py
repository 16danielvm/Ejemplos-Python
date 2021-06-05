'''
Ingrese un numero para determinar su factorial
'''


a = int(input("Ingrese el numero"))
resultado = 1

print(a,"! es igual a ", end="" )

for i in range(a,0,-1):
    resultado*=i
    if i==1:
        print(i, end="")
    else:
        print(i,"x", end="")
print(" =", resultado)