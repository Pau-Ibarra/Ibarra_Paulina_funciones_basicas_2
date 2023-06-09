"""
Escribe una función que acepte dos enteros como parámetros: tamaño y valor. 
La función debe crear y devolver una lista cuya longitud sea igual al tamaño dado, y cuyos valores sean 
todos el valor dado.
Ejemplo: length_and_value(4,7) debe devolver [7,7,7,7]
Ejemplo: length_and_value(6,2) debe devolver [2,2,2,2,2,2]
"""
def longitud_igual_tamaño (tamaño, valor):
    resultado = []
    

    for _ in range (tamaño):
            resultado.append(valor)
            
    return resultado



lista1 = longitud_igual_tamaño(5,6)
print (lista1)

lista2 = longitud_igual_tamaño(10,31)
print (lista2)