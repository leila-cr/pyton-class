texto = "ATG CCT TAA GGT" #string
lista = texto.split()
print(lista) #se imprime una lista en la que el delimitador es automaticamente el espacio

texto = "ATG,CCT,TAA,GGT"
lista = texto.split(",") #comas son el delimitador 
print(lista)

texto = "ATG-CCT-TAA-GGT"
lista = texto.split("-", 2) #guiones son el delimitador, se toman en cuenta unicamente los dos primeros 
print(lista)

texto = "ATGCCTTAAGGT"
lista = texto.split("T", 2) #solo son normales los primero sque tienen el -, ya despues lo imprime todo lo que sigue
print(lista)

texto = "ATG\tCCT\tTAA\tGGT" #tabuladores en un string
lista = texto.split("\t") #el delimitador sera el string
print(lista)


