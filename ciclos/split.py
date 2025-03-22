texto = "ATG CCT TAA GGT"
lista = texto.split()
print(lista)

texto = "ATG,CCT,TAA,GGT"
lista = texto.split(",") #puede se con comas u apostrofes pues es un string
print(lista)

texto = "ATG-CCT-TAA-GGT"
lista = texto.split("-", 2) #solo son normales los primero sque tienen el -, ya despues lo imprime todo lo que sigue
print(lista)

#input recive strings y sum numeros