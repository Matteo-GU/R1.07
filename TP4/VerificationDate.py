correct="correcte"
date=input("Entrez la date: ")
while len(date)!=8:
    date=input("Mauvais format, corrigez votre saisie: ")

annee=int(date[-1]) + int(date[-2])*10 + int(date[-3])*100 + int(date[-4])*1000
mois=int(date[3])+int(date[2])*10
jour=int(date[1])+int(date[0])*10

if annee%4==0 and annee%100!=0 or annee%400==0:
    bissextile=True
else:
    bissextile=False

if mois==2 and jour>28:
    if bissextile==True and jour==29:
        correct="correcte"
    else:
        correct="incorrecte"

if jour>31: correct="incorrecte"

if jour==31:
    if mois==4 or mois==6 or mois==9 or mois==11:
        correct="incorrecte"

print(f"La date est {correct}")