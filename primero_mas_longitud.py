#Primero más longitud: crea una función que acepte una lista y 
#devuelva la suma del primer valor de la lista, más la longitud de la lista.
#Ejemplo: primero_mas_longitud([1,2,3,4,5]) debe devolver 6 (primer valor: 1 +length: 5)

def primero_mas_longitud (lista):
    primer_valor= lista[0]
    longitud = len(lista)
    resultado = primer_valor + longitud
    return resultado

lista =[1,2,3,4,5]
resultado = primero_mas_longitud(lista)
print(resultado)

