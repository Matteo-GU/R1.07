L1 = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7, 6]

nombreFrequent=0
occurenceFrequent=0

for i in range(len(L1)):
    nombreTest=L1[i]
    if L1.count(nombreTest) > occurenceFrequent:
        nombreFrequent=nombreTest
        occurenceFrequent=L1.count(nombreTest)

print(f"Le nombre le plus fréquent dans la liste est le : {nombreFrequent} ({occurenceFrequent} x)")