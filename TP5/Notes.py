m=0
div=0
admis=""
for i in range(5):
    print(f"Veuillez entrer la note du module {i} et le coefficient correspondant : ")
    S1=(input())
    S2=S1.split(" ")
    m+=float(S2[0])*float(S2[1])
    div=div+float(S2[1])
    if float(S2[0])<8:
        admis="non"
m=m/div
if m<=10:
    admis="non"
print(f"La moyenne générale de l'étudiant est {m}. Il est {admis} admis.")