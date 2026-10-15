n=float(input("Vous cherchez la table de multiplication de quel nombre? "))
table=list()
for i in range (10):
    table.append(n*i)
for i in range (len(table)):
    print(f"{n} * {i} = {round(table[i],2)}")