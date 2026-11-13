dic={"name":"toto","firstname":"titi","promo":2026,"group":202}

print(f"votre nom est {dic['name']}, prénom est {dic['firstname']}, vous faites partie de la promo {dic['promo']} et votre groupe est {dic['group']}")

print("Les clés du dictionnaire sont :")
for i in dic.keys():
    print(f"- {i}")

print("Les clés du dictionnaire sont :")
for i in dic.values():
    print(f"- {i}")

print("Les tuplets du dictionnaire sont :")
for i in dic.items():
    print(f"- {i}")

dic2={"name":"tutu","firstname":"tata","promo":2026,"group":102}
binome={"one":dic,"two":dic2}

print("Les étudians formants le binôme sont :")
print("-L'étudiant {} {} du groupe {}".format(binome["one"]["firstname"], binome["one"]["name"],binome["one"]["group"]))
print("-L'étudiant {} {} du groupe {}".format(binome["two"]["firstname"], binome["two"]["name"],binome["two"]["group"]))