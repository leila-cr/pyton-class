secuencias = input("Ingresa secuencias separadas por comas").split(",") # Al aplicar el split, convierte el string a una lista

codones_inicio = [secuencia.strip() [:3] for secuencia in secuencias] # De cada secuencia se extraen los primeros 3 nucleotidos 
print(codones_inicio) # El resultado devuelto es una lista []