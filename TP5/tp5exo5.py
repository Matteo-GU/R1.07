heures=int(input("Nombre d'heures : "))
salaire=float(input("Salaire horaire : "))
paie=float(0)
for i in range (heures) :
    if i < 160 :
        paie=paie+salaire
    elif i < 200 :
        paie=paie+(salaire*1.25)
    else : paie=paie+(salaire*1.5)
print(f"Le salaire est {paie}")