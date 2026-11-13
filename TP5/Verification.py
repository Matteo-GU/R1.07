import os.path
import datetime

path1=input("Entrez le premier nom de fichier : ")
path2=input("Entrez le deuxième nom de fichier : ")

if os.path.isfile(path1)==True and os.path.isfile(path2)==True:
    print(f"Taille du premier fichier : {os.path.getsize(path1)} octets")
    print(f"Taille du deuxième fichier : {os.path.getsize(path2)} octets")
    if os.path.getmtime(path1)>os.path.getmtime(path2):
        print(f"Le fichier le plus recent est le premier, qui date de {datetime.datetime.fromtimestamp(os.path.getmtime(path1))}")
    else : print(f"Le fichier le plus recent est le deuxième, qui date de {datetime.datetime.fromtimestamp(os.path.getmtime(path2))}")
else : print("Un des fichiers n'existe pas")