inputfile = "4_input_adapters.txt"
outputfile = "4_input_no_adapters.txt"


#Se lee el archivo que contiene las secuencias
with open (inputfile, "r") as infile, open (outputfile, "w") as outfile:
    for linea in infile:
        # Se cortan los adaptadores primeros 14 nucleotidos
        secuencia_limpia = linea.strip()[14:] #Se toma de la posicion 14 en adelante

        
        #Secuencia sin adaptadores se manda a un archivo
        outfile.write(f"{secuencia_limpia}\n") 



#Otra opcion
#with open("4_input_adapters.txt", "r") as infile, open("4_input_adapters.txt", "w") as outfile:
    #for linea in infile:
        #secuencia_limpia = linea.strip()[14:]
        #print(secuencia_limpia, file=outfile, end="\n")


