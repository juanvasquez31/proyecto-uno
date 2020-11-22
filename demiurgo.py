#El demiurgo nos sirve para gestionar archivos
#modo de apertura 
# r : solo lectura -> Si el archivo no existe va a sacar error
# w : modo escritura -> Crea el archivo si no existe
# a : anadir  -> Crea el archivo si no existe
# r+: lectura y escritura -> Si el archivo no existe saca error
# w+: Lectura y escritura -> Crea el archivo si no existe
# a+: Lectura y escritura -> El archivo es creado si no existe

def funcion(x):
    return 2*x +1

archivo = open("numeros.txt","r")

#linea = archivo.readline() #lee la primera linea por linea
#print(linea)
#linea = archivo.readline() #lee la segunda linea
#print(linea)
#archivo.close()

linea = archivo.readline()    
print(linea)
while linea != "":
    linea = archivo.readline()
    y = funcion(linea)
    print(linea+1)
    linea = archivo.readline()
#siempre que abrimos, cerramos
archivo.close()