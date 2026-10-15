n=int(input("n="))
boucle=input('Souhaitez vous une boucle "for" ou une boucle "while"? ')
factorielle=1

if boucle=="for":
    for i in range (1,n+1):
        factorielle=factorielle*i
        print(factorielle)

elif boucle=="while":
    i=1
    while i<=n:
        factorielle=factorielle*i
        print(factorielle)
        i=i+1


else: print("Choix incorrect")