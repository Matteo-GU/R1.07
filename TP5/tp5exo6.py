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
    wagonrange == 1:
        if i=='a':
            wagonrange=2
        else:
            wagonrange=0
    if wagonrange==2:
        if i=='g':
            wagonrange=3
        else:
            wagonrange=0
    if wagonrange==3:
        if i=='o':
            wagonrange=4
        else:
            wagonrange=0
    if wagonrange==4:
        if i=='n':
            wagon+=1
        wagonrange=0
print(f"Il y a {voyelle} voyelles et {wagon} wagons.")