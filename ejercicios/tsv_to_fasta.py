inputfile = "dna_sequences.txt"
outputfile = "dna_sequences.fa"


# Se lee y abre el archivo de entrada
with open("dna_sequences.txt","r") as infile, open("dna_sequences.fa", "w") as outfile:
    for linea in infile:
        id, seq = linea.strip().split("\t") #Se eliminan espacios y el string se divide en una lista de dos elementos 
        outfile.write(f">{id}\n{seq.upper()}\n") #Upper va a convertir letras a mayusculas


