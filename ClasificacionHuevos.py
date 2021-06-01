'''
Planteamiento de la situación

En una granja acaban de adquirir una máquina que le permitirá a una empresa de huevos aumentar la rapidez con la que son dispuestos sus productos para la distribución al usuario final. Se requiere un ingeniero de sistemas para que programe esta máquina bajo ciertos estándares.

Los huevos son clasificados según su calidad y su peso. Para identificar la calidad de los huevos existen tres categorías A, B y C. Los huevos de categoría A son huevos frescos sin defectos y aptos para el consumo humano. Los huevos de categoría B son huevos de calidad normal que han sido sometidos a procesos de conservación. Los huevos tipo C son huevos que deben ser pasados por procesos industriales para ser considerados aptos para el consumo.

Los huevos de categoría A son clasificados según su peso como:

    Huevos A cuyo peso va desde los 55 g. hasta un peso menor de 60 g.
    Huevos AA cuyo peso va desde los 60 g. hasta un peso menor de 65 g.
    Huevos AAA cuyo peso es igual o mayor a 65 g.

y los tipo B y C o BC como:

    Huevos B cuyo peso va desde 43 g. hasta un peso menor de 55 g.
    Huevos C cuyo peso es menor de 43 g.

Escriba una función llamada clasificacion_huevos que, de entrada, reciba una lista de datos tipo flotantes asociada al peso de un conjunto de huevos. La lista puede tener cualquier número de datos. Un ejemplo de esta lista de datos puede ser:

[46.5, 60.8, 58.7, 70.0, 49.8]

donde cada ítem como se mencionó está asociado al peso de cada huevo, es decir el primer ítem pertenece a un huevo que pesa 46.5 gr.

La función debe ser capaz de clasificar los huevos de acuerdo con el peso que se especifique en la lista anteriormente mencionada. Los huevos deben ser clasificados si son A, AA, AAA o si son BC (Una única clasificación para los huevos B y C). Es decir, el primer huevo pesa 46.5 gr lo que indica que el huevo es de categoría BC.

Al clasificar los huevos determine el total de huevos de cada uno de los tipos de huevos, A, AA, AAA y BC. Habiendo determinado el número de huevos de acuerdo a cada clasificación, desarrolle una función adicional, llamada calcular_bandejas, que permita calcular cuántas bandejas de huevos se pueden obtener para cada una de las categorías, considerando que los huevos tipo A se empacan en grupos de 30 huevos, los tipos AA en grupos de 24 huevos, los tipo AAA en grupos de 12 huevos y los tipo BC en grupos de 24 huevos. Esta función debe recibir como parámetro de entrada el número de huevo y los huevos por bandeja.

La función clasificacion_huevos debe retornar la siguiente información y estructura:

A:27->Bandejas tipo A:0
AA:24->Bandejas tipo AA:1
AAA:18->Bandejas tipo AAA:1
BC:31->Bandejas tipo BC:1

 

Debe tenerse en cuenta el orden de cada una de las distintas clases de huevos. Tenga en cuenta que los huevos tipo BC son la unión de los huevos tipo B y los tipo C.
'''

cont_A=0
cont_AA=0
cont_AAA=0
cont_BC=0

def calcular_bandejas(cont_A,cont_AA,cont_AAA,cont_BC):
    
    A = "A:"+str(cont_A)+"->Bandejas tipo A:"+str(cont_A//30)
    AA = "AA:"+str(cont_AA)+"->Bandejas tipo AA:"+str(cont_AA//24)
    AAA = "AAA:"+str(cont_AAA)+"->Bandejas tipo AAA:"+str(cont_AAA//12)
    BC =  "BC:"+str(cont_BC)+"->Bandejas tipo BC:"+str(cont_BC//24)

    D = A+"\n"+AA+"\n"+AAA+"\n"+BC

    return D

def clasificacion_huevos(lista):
    global cont_A
    global cont_AA
    global cont_AAA
    global cont_BC
    for i in lista:
        if (i>=55) and (i<60):
            cont_A+=1
        elif (i>=60) and (i<65):
            cont_AA+=1
        elif (i>=65):
            cont_AAA+=1
        else:
            cont_BC+=1
    
    return calcular_bandejas(cont_A,cont_AA,cont_AAA,cont_BC)

print(clasificacion_huevos([56.21063116338781, 47.7948592196791, 49.3465398154398, 45.088736973782886, 41.904588419941064, 55.53079786396371, 58.150395220919236, 41.462583204709624, 53.39340540085833, 53.97213553608458, 52.213196858556245, 52.65636968150478, 56.16579904504961, 58.656770287858706, 52.75228288278458, 46.88090365925265, 68.95791081652551, 41.41489786587632, 53.93736590433801, 65.44535216103853, 51.47460766502953, 59.124113762141064, 46.08140309766326, 63.90240726854179, 48.61702882571772, 55.62221185129054, 65.3994939665756, 50.59295825621861, 65.92249338401521, 43.13787857718743, 66.97331421598852, 48.08995917027214, 61.86273519770555, 61.33795604386076, 54.42450939260516, 58.34149708315052, 67.96911052572517, 68.03818555471125, 61.725049585008364, 66.8636106580667, 61.397597440203235, 40.455932475814066, 67.66753379921022, 46.44166382594054, 44.01624352417587, 64.74961371683732, 69.16467049281272, 48.41707528041957, 43.841247948729475, 64.17694084079663, 56.73594381755263, 66.85558113955751, 43.3707747083959, 53.591036889620206, 40.222046309623835, 47.004035466731445, 67.78018446633645, 45.98952120985176, 50.22868735749795, 41.73507074507547, 45.61395481743725, 56.03134581568086, 62.11164312672585, 47.204016916703225, 63.374797315015414, 69.82672951989325, 69.83914597066266, 68.58146261336243, 46.86086233828525, 42.80605943147338, 61.063327975167134, 45.863404558988975, 59.20470999189604, 52.337915485709665, 50.177249201896565, 56.74546549112554, 55.56803858725005, 53.94945720289324, 57.1000232248806, 54.71471449412769, 49.03024230308958, 67.5935467172066, 66.63869075141623, 57.850937437661926, 69.04459086139013, 49.553200616836676, 55.175393878134706, 55.30668524898195, 48.151598243553565, 40.42804977553425, 48.262037331155945, 56.5201030160736, 50.30862047348601, 40.6334512050607, 67.91053549432823, 57.7349864620126, 44.355330877667456, 58.89932920045244, 47.63547760179575, 41.33222060399971]))

