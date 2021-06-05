'''
Escribir un código en python que permita decifrar el código morse escrito por el usuario a texto
'''
import pandas as pd

IntMorseCode = {"A":".- ","B":"-... ","C":"-.-. ","D":"-.. ","E":". ","F":"..-. ","G":"--. ","H":".... ","I":".. ","J":".--- ","K":"-.- ","L":".-.. ","M":"-- ","N":"-. ","O":"--- ","P":".--. ","Q":"--.- ","R":".-. ","S":"... ","T":"- ","U":"..- ","V":"...- ","W":".-- ","X":"-..- ","Y":"-.-- ","Z":"--.. ","1":".---- ","2":"..--- ","3":"...-- ","4":"....- ","5":"..... ","6":"-.... ","7":"--... ","8":"---.. ","9":"----. ","0":"----- ",".":".-.-.- ",",":"--..-- ","?":"..--.. "," ":"/ "}

df = pd.DataFrame([[key, IntMorseCode[key]] for key in IntMorseCode.keys()], columns=['Letra', 'Señal'])
df.set_index('Letra', inplace=True)
print(df)

morse1 = input("Escriba su codigo morse separando cada señal con un espacio incluyendo la ultima ")

def Morse2txt(morse):
    '''
    Argumento:
            morse(string): Escrito por el usuario, solicitado por el sistema
    '''
    IntMorseCode = {"A":".- ","B":"-... ","C":"-.-. ","D":"-.. ","E":". ","F":"..-. ","G":"--. ","H":".... ","I":".. ","J":".--- ","K":"-.- ","L":".-.. ","M":"-- ","N":"-. ","O":"--- ","P":".--. ","Q":"--.- ","R":".-. ","S":"... ","T":"- ","U":"..- ","V":"...- ","W":".-- ","X":"-..- ","Y":"-.-- ","Z":"--.. ","1":".---- ","2":"..--- ","3":"...-- ","4":"....- ","5":"..... ","6":"-.... ","7":"--... ","8":"---.. ","9":"----. ","0":"----- ",".":".-.-.- ",",":"--..-- ","?":"..--.. "," ":"/ "}

    listamorse = morse.split(sep="/ ")
    listapalabras = []
    for i in range(len(listamorse)):
        listapalabras.append(listamorse[i].split(" "))
    for i in listapalabras:
        for j in i:
            if j == "":
                j ="/ "
            else:    
                j = j+" "
            for key, value in IntMorseCode.items():
                if j == value:
                    print(key,end="")


Morse2txt(morse1)