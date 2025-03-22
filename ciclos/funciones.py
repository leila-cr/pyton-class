#caso de funcion enumerate
secuencia = "GCCTAAGGC"

for i, base in enumerate(secuencia):
    print(f"Posicion {i} : {base}")


#funcion zip
bases = "ATGC"
complementos = "TACG"

for base,complemento in zip(bases, complementos): #con zip se pueden iterar mas de 1 elemento
    print (f"{base}---> {complemento}")


genes = ["AraC", "LE8", "THR8"]
longitudes = [356, 89] #... terminarlo