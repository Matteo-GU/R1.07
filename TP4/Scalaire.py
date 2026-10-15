nMax=3
v1 = []
v2 = []
scalaire=0.0
n=int(input(f"Quelle est la taille de vos vecteurs [entre 1 et {nMax}] ? "))
while 1 > n > nMax:
    n=int(input(f"La valeur n'est pas entre 1 et {nMax}, entrez a nouveau : "))

print("\nSaisie du premier vecteur :")
for i in range(n):
    v1.append(int(input(f"v1[{i}] = ")))

print("\nSaisie du second vecteur :")
for i in range(n):
    v2.append(int(input(f"v2[{i}] = ")))

for i in range(n):
    scalaire=scalaire+v1[i]*v2[i]
print(f"Le produit scalaire de v1 par v2 vaut {scalaire}")