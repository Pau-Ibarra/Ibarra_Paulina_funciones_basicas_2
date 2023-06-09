#Cuenta regresiva: crea una función que acepte un número como entrada. 
#Devuelve una lista nueva que cuente de uno en uno, desde el número (como elemento 0) hasta 0 (como último elemento). 
#Ejemplo: countdown(5) debería devolver [5,4,3,2,1,0]

def cuenta_regresiva(num): # definí una función con un parámetro "modificable"
    lista =[]    #creo una variable de tipo lista [] para reservar el espacio de mi lista, q por ahora está vacía
    for num in range (num,-1,-1):#el bucle for me permite generar los valores que se almacenarán en mi lista
        lista.append(num) # para q se almacenen en la lista uso metodo append, lo que corresponde a la variable x se añadirá a lista
    return lista # returna la lista, esto hace que el valor se fije.


resultado= cuenta_regresiva(5) #debo crear una variable que almacene el resultado de la función, ya q si llamo directamente la función, se "pisa" con la definición de la función???
print(resultado) 


