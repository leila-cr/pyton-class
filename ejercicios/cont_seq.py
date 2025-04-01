inputfile = "dna_sequences.fa"


with open(inputfile, "r") as infile:
    lineas = infile.readlines() #Se lee el archivo pero lo da en formato de lista

# Se filtran lineas que empiezan con un ">"
lineas_filtradas = [linea for linea in lineas if linea.startswith(">")]
print(f"Total de lineas de secuencias: {len(lineas_filtradas)}")