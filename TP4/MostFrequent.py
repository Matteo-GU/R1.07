L1 = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7, 6]

""" ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
* Completez le programme a partir d'ici.
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** * /
"""

nombreFrequent=0
occurenceFrequent=0
nombreTest=0

for i in range(len(L1)):
    nombreTest=L1[i]
    occurenceTest=0
    for j in range (i,len(L1)):
        if L1[j]==nombreTest: occurenceTest=occurenceTest+1
    if occurenceTest>occurenceFrequent:
        nombreFrequent=nombreTest
        occurenceFrequent=occurenceTest

print(f"Le nombre le plus fréquent dans la liste est le : {nombreFrequent} ({occurenceFrequent} x)")


""" ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
* Ne rien modifier apres cette ligne.
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** * /
"""
