numeros_str = input ("Dame 3 numeros separados por espacios").split() # se convierte numeros ingresados en lista de strings  
lista_numeros = (list(map(int,numeros_str))) #funcion map convierte los elementos de la lista en enteros


suma = sum(lista_numeros) #sum trabaja con iterables y map es iterable, por lo tanto en este problema no es tan necesario agregar el list
print(suma)

#numeros_str = input ("Dame 3 numeros separados por espacios").split() # se convierte numeros ingresados en lista de strings  
#lista_numeros = map(int,numeros_str) #el objeto map tambien es un iterable


#suma = sum(lista_numeros) 
#print(suma)


