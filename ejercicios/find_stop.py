sequences = input("Ingresa secuencias separadas por comas").upper().split(",")

# Busqueda de secuencias que contengan codon de paro
sequence_stop = [sequence for sequence in sequences if "TGA" in sequence or "TAG" in sequence or "TAA" in sequence] 
print(sequence_stop)