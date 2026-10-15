from random import randint
n=101
tour=0
x=randint(0,100)
while (n!=x):
    n=int(input())
    if (n<x):
        print("La valeur est plus grande")
    if (n>x):
        print("La valeur est moins grande")
    tour=tour+1
print("La valeur est correcte")
print(f"Vous avez trouvé en {tour} tours")