apes = ["Pongo py", "Pan nosequ", "Gor noseque"]

for ape in apes:
    name_length = len(ape)
    first_letter = ape[0]
    print (f"{ape} is an ape. Its name starts with {first_letter}") #entre las llaves van las variables igual se pueden hacer operaciones dentro
    print (f"Its name has {len(ape)}")  # es por que se esta concatenando un string con un int