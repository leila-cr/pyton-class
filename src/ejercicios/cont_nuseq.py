secuencias = input("Ingresa secuencias separadas por comas").upper().split(",") # Funcion upper pasa minusculas a mayusculas

#Conteo de  A,C,T,G en cada secuencia
count = [[secuencia.count("A"), secuencia.count("T"), secuencia.count("G"), secuencia.count("C")] for secuencia in secuencias] 
print(count) # Se devuelve una lista, con listas del conteo realizado en cada secuencia



#Si no se usa diccionario
#count = [[f"A:{secuencia.count('A')}", f"T:{secuencia.count('T')}", f"G:{secuencia.count('G')}", f"C:{secuencia.count('C')}"] for secuencia in secuencias] 