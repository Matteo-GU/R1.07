argent=int(input("Combien d'argent? "))
thune=argent
cent=0
cinquante=0
dix=0
deux=0
un=0

while thune>=100:
    thune=thune-100
    cent+=1

while thune>=50:
    thune=thune-50
    cinquante+=1

while thune>=10:
    thune=thune-10
    dix+=1

while thune>=2:
    thune=thune-2
    deux+=1

while thune>0:
    thune=thune-1
    un+=1

print(f"{argent} euros, c'est donc {cent} billets de 100, {cinquante} de 50, {dix} de 10, {deux} pièces de 2 et {un} pièce de 1.")