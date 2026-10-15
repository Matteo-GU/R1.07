sub10=0
sub15=0
sub20=0
for i in range(10):
    nombre=21
    while (0<=nombre>=20):
        nombre = float(input("Entrez une valeur entre 0 et 20:"))
        if nombre>20 or nombre<0:
            print("La valeur est incorrecte")
    if nombre<10:
        sub10=sub10+1
    elif nombre<15:
        sub15=sub15+1
    else:
        sub20=sub20+1
print(f"Le nombre de valeurs strictement inférieures à 10 est {sub10}")
print(f"Le nombre de valeurs supérieures ou égales à 10 et strictement inférieures à 15 est {sub15}")
print(f"Le nombre de valeurs supérieures ou égales à 15 est {sub20}")