secuencias = input("Ingresa una secuencia separada por comas").split(",")

# Se invierte la secuencia de nucleotidos
secuencia_inver = [secuencia.strip()[::-1] for secuencia in secuencias]
print(secuencia_inver)# Se devuelve una lista de strings

   