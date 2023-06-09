def mayores_que_segundo(lista):
    resultado =[]
    
    if len(lista)>=2:
        for numero in lista:
            if numero>lista[1]:
                resultado.append(numero)
                
                

        print (len(resultado))
        if len(lista)<2:
                return False
        else:
                return resultado

lista1 =mayores_que_segundo([5,2,3,2,1,4])
print ("Lista 1: ", lista1)

lista2 =mayores_que_segundo([87, 36, 95, 524, 616, 707])
print ("Lista 2: ", lista2)

lista3 =mayores_que_segundo([87, 98])
print ("Lista 3: ", lista3)

lista4 =mayores_que_segundo([87])
print ("Lista 4: ", lista4)