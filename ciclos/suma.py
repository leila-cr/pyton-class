numeros_str = input ("dame 3 numeros separados por espacios").split() #al aplicar lo convierte en una lista al principio era un string 
lista_numeros = (list(map(int,numeros_str)))


#print(numeros_str)
suma = sum(lista_numeros) #sum trabaja con iterables y map es un iterable, por lo tanto en este problema no es tan necesario agregar el list
print(suma)

 