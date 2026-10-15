# Demande le nombre d'étudiants à l'utilisateur
nombreEtudiants = int(input("Donnez le nombre d'etudiants : "))
moyenne = 0.0
# déclaration d’une liste vide qui va contenir autant de notes que d'étudiants
notes = []

for i in range(nombreEtudiants):
    notes.append(float(input(f"Note étudiant {i} : ")))
    moyenne += notes[i]

moyenne /= nombreEtudiants

print(f"Moyenne de classe : {moyenne}\n")

print("Numéro de l'Etudiant | note | écart a la moyenne")
for i in range (nombreEtudiants):
    print(f"{i} | {notes[i]} | {notes[i]-moyenne}")