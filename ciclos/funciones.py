#funcion enumerate
secuencia = "GCCTAAGGC"

for i, base in enumerate(secuencia): #enumerate da el indice de la posicion del string, ademas de la letra que lo ocupa
    print(f"Posicion {i} : {base}")


#funcion zip
bases = "ATGC"
complementos = "TACG"

for base,complemento in zip(bases, complementos): #zip permite iterar con 2 elementos
    print (f"{base}---> {complemento}")

#otro caso con la funcion zip
genes = ["AraC", "LE8", "THR8"]
longitudes = [356, 89] 

for gen, long in zip(genes, longitudes):#en este caso zip ignorara los elementos sobrantes
    print(f"Gen {gen} ----> {long}pb")