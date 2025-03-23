with open ("genes.gff") as file:
    for linea in file: 
        columnas  = linea.strip().split("\t") #se eliminan espacios de lineas, posteriormente se convierte en una lista strings delimitada por \t 
        tamano = int(columnas[4])-int(columnas[3])+1 #se cambia a lista de enteros y se obtiene resta de la columna 4 y 3 
        print(tamano)


   
#with open ("genes.gff") as file:
    #for linea in file:#itera sobre cada linea en el archivo
        #print(linea)
        #columnas  = linea.strip().split("\t") #quitar espacios y con el split delimitar 
        #print(columnas[3])# se imprime la columna 3 pero no como lista checar eso