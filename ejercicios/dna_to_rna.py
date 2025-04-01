secuencias = input("Dame secuencias separadas por comas").split(",")

secuenacias_arn = [secuencia.strip().replace("T","U") for secuencia in secuencias] # En cada secuencia se quitan espacios, y se reemplazan "T" por "U"
print(secuenacias_arn) 