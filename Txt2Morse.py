'''
Escribir un código en python que permita codificar un mensaje en codigo Morse
'''
import pandas as pd

IntMorseCode = {"A":".- ","B":"-... ","C":"-.-. ","D":"-.. ","E":". ","F":"..-. ","G":"--. ","H":".... ","I":".. ","J":".--- ","K":"-.- ","L":".-.. ","M":"-- ","N":"-. ","O":"--- ","P":".--. ","Q":"--.- ","R":".-. ","S":"... ","T":"- ","U":"..- ","V":"...- ","W":".-- ","X":"-..- ","Y":"-.-- ","Z":"--.. ","1":".---- ","2":"..--- ","3":"...-- ","4":"....- ","5":"..... ","6":"-.... ","7":"--... ","8":"---.. ","9":"----. ","0":"----- ",".":".-.-.- ",",":"--..-- ","?":"..--.. "," ":"/ "}

df = pd.DataFrame([[key, IntMorseCode[key]] for key in IntMorseCode.keys()], columns=['Letra', 'Señal'])
df.set_index('Letra', inplace=True)
print(df)

mensaje = input("Escriba su mensaje para convertir a codigo Morse ")

def Txt2Morse(txt):
    '''
    Argumento:
            txt(string): Mensaje escrito por el usuario, solicitado por el sistema
    '''
    IntMorseCode = {"A":".- ","B":"-... ","C":"-.-. ","D":"-.. ","E":". ","F":"..-. ","G":"--. ","H":".... ","I":".. ","J":".--- ","K":"-.- ","L":".-.. ","M":"-- ","N":"-. ","O":"--- ","P":".--. ","Q":"--.- ","R":".-. ","S":"... ","T":"- ","U":"..- ","V":"...- ","W":".-- ","X":"-..- ","Y":"-.-- ","Z":"--.. ","1":".---- ","2":"..--- ","3":"...-- ","4":"....- ","5":"..... ","6":"-.... ","7":"--... ","8":"---.. ","9":"----. ","0":"----- ",".":".-.-.- ",",":"--..-- ","?":"..--.. "," ":"/ "}
    txtn = txt.upper()
    for i in txtn:
        for key in IntMorseCode.keys():
            if i == key:
                print(IntMorseCode[key],end="")
Txt2Morse(mensaje)