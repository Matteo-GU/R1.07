string=input("Saisissez une chaîne de caractères : ")
string=str.lower(string)
voyelle=0
count=0
wagon=0
wagonrange=0
for i in string :
    count+=1
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='y' :
        voyelle=voyelle+1
    if i=='w' and wagonrange==0:
        wagonrange=1
    if i=='a' and wagonrange==1:
        wagonrange=2
    if i=='g' and wagonrange==2:
        wagonrange=3
    if i=='o' and wagonrange==3:
        wagonrange=4
    if i=='n' and wagonrange==4:
        wagon+=1
        wagonrange=0
print(f"Il y a {voyelle} voyelles et {wagon} wagons.")