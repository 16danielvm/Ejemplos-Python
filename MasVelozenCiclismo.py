'''

Planteamiento de la situación
Estas compitiendo con tus amigos para determinar cuál es más veloz en ciclismo en ruta. Para esto propones aplicar tus conocimientos de programación para optimizar el proceso. Propones anotar en una agenda los tiempos de varias rutas en varios días y para la toma del tiempo utilizas el formato horas:minutos:segudos.

Ya han pasado varios meses y en tu agenda tienes los siguientes datos: los tiempos de las rutas Bogotá, Bucaramanga y Medellín. En la ruta Bogotá tomaste tres registros de tiempo, en la ruta Bucaramanga tomaste dos registros de tiempo y en la ruta Medellín tomaste nuevamente tres registros. A tu amigo le compartes el mismo proceso indicándole la ruta exacta que desarrollaste.

Aprovechando que has iniciado un curso de programación, decides automatizar el proceso para impresionar a tus amigos sobre la forma efectiva y rápida de hacer estos cálculos.

Planteamiento del reto
¿De qué manera podrías obtener automáticamente el mejor tiempo por ruta? Como el proceso se puede repetir para ti y cada uno de tus amigos, define una función que reciba como parámetros una cadena de texto con el siguiente formato:

"Bogota, 1: 22: 30, 1:20:40, 1: 15: 20;

Bucaramanga, 2: 10: 10, 2: 5: 20;

Medellín, 3: 50: 40, 3: 50: 50, 3: 50: 55”

Y un segundo parámetro con el nombre de la persona que hará el cálculo. Por ejemplo: calculadoraTiempos(registroDeTiempos, nombre)

Retorna la respuesta con el siguiente formato por ejemplo para las entradas: calculadoraTiempos("Bogotá,1:22:30,1:20:40,1:15:20;Bucaramanga,2:10:10,2:5:20;Medellín,3:50:40,3:50:50,3:50:55", "Egan")
la salida sería ('Egan', {'Bogotá': '1:15:20', 'Bucaramanga': '2:5:20', 'Medellín': '3:50:40'}).

'''

from datetime import datetime

def calculadoraTiempos(registroDeTiempos, nombre):
    """
        La función toma como argumentos : 
            - Un registro de tiempos por ciudad
            - Un nombre

        Args:
            registroDeTiempos(String): Ciudad y registros de tiempo separados por ";"
            nombre(String): nombre de la persona que hizo dichos registros de tiempo
        
        Return:
            tuple: Retorna una tupla con el nombre y los registros de tiempo minimos por cada ciudad
    """
    #Divide los registros por ";"
    cadaregistro = registroDeTiempos.split(";")
    
    #Crea una lista de listas dividiendo por ","
    listadelistas = []
    for i in cadaregistro:
        listadelistas.append(i.split(','))
    
    #Convierte el primer elemento en str y los demas en tipo fecha.
    for i in range(len(listadelistas)):
        for j in range(len(listadelistas[i])):
            if j == 0:
                str(listadelistas[i][j])
            else:
                listadelistas[i][j] = datetime.strptime(listadelistas[i][j],'%H:%M:%S')

    #Crea dos listas, una para las ciudades y otro para los tiempos minimos de cada ciudad
    ciudad = []
    tiempo = []

    #Agregar cada ciudad a la lista ciudad y borrarla de la lista
    for i in range(len(listadelistas)):
        for j in range(len(listadelistas[i])):
            if j == 0:
                ciudad.append(listadelistas[i][j])
                listadelistas[i].pop(j)

    #Calcula el tiempo minimo de cada ciudad
    for i in range(len(listadelistas)):
            tiempo.append(min(listadelistas[i]))
    
    #Se crea el diccionario
    dic={}

    #Se agrega como claves cada ciudad
    dic = dic.fromkeys(ciudad)

    #Se agrega cada tiempo minimo a su respectiva ciudad
    i = 0
    for key in dic:
        dic[key] = tiempo[i].strftime('%H:%M:%S')
        i= i+1
    
    #Se crea la tupla con el nombre y la ciudad con su respectivo tiempo minimo de recorrido
    tuple = (nombre,dic)

    return tuple



print(calculadoraTiempos("Bogotá,1:22:30,1:20:40,1:15:20;Bucaramanga,2:10:10,2:5:20;Medellín,3:50:40,3:50:50,3:50:55","Egan"))