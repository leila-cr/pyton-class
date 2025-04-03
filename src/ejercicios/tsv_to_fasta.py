inputfile = "./data/ejercicios/dna_sequences.txt"
outputfile = "./results/ejercicios/dna_sequences.fa"


# Se lee y abre el archivo de entrada
with open(inputfile,"r") as infile, open(outputfile, "w") as outfile:
    for linea in infile:
        id, seq = linea.strip().split("\t") #Se eliminan espacios y el string se divide en una lista de dos elementos 
        outfile.write(f">{id}\n{seq.upper()}\n") #Upper va a convertir letras a mayusculas


