correct=0
tarif1=0
tarif2=0

while correct==0:
    hdebut=int(input("Donnez l’heure de début de la location (un entier) : "))
    hfin=int(input("Donnez l’heure de fin de la location (un entier) : "))

    if hdebut<0 or hdebut>24 or hfin<0 or hfin>24:
        print(" Les heures doivent être comprises entre 0 et 24 !\n")
    elif hdebut==hfin:
        print(" Attention ! l’heure de fin est identique à l’heure de début.\n")
    elif hdebut>hfin:
        print("Attention ! le début de la location est après la fin ...\n")
    else: correct=1

for i in range (hdebut+1,hfin+1):
    if 7<=i<=17:
        tarif2+=1
    else:
        tarif1+=1
print("Vous avez loué votre vélo pendant")
if tarif1!=0: print(f"{tarif1} heure(s) au tarif horaire de 1.0 euros")
if tarif2!=0: print(f"{tarif2} heure(s) au tarif horaire de 2.0 euros")
print("Le montant total à payer est de {} euro (s).".format(tarif1+tarif2*2))
