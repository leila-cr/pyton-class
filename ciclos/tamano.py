with open ("genes.gff") as file:
    for linea in file:
        print(linea)
        columnas  = linea.strip().split("\t")
        tamano = int(columnas[4])-int(columnas[3])+1

   #tengo que hacer aui lo de archivo nano y aque lo hice en otro lado
        