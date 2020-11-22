#El zatustro nos sirve para gestionar archivos
#modo de apertura 
# r : solo lectura -> Si el archivo no existe va a sacar error
# w : modo escritura -> Crea el archivo si no existe
# a : anadir  -> Crea el archivo si no existe
# r+: lectura y escritura -> Si el archivo no existe saca error
# w+: Lectura y escritura -> Crea el archivo si no existe
# a+: Lectura y escritura -> El archivo es creado si no existe

def funcion(x):
    return 2*x + 1

archivo = open("numeros.txt","r")
archivo2 = open("Resultado.txt","w")
lineas = archivo.readlines()
for linea in lineas:
    x = int(linea)
    y = funcion(x)
    print(y)
    y = str(y)
    archivo2.write(y)
    archivo2.write("\n")
archivo.close()
archivo2.close()