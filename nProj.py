import os
import sys

if(len(sys.argv)==2):
    Repertoire=(sys.argv[1])
    if not os.path.exists(Repertoire):
        print("Le dossier n'existe pas")
    else:
        os.chdir(Repertoire)
        print(os.getcwd())
NomProj= input("Nom du projet: \n")
Description= input("Desciprtion du projet: \n")
os.makedirs(NomProj)
print("Le dossier", NomProj, "à été cree")
os.chdir(NomProj)

fichier = open("README.txt", "a")
fichier.write("*****************************************\n")
fichier.write("Nom du projet :"+NomProj+"\n")
fichier.write("*****************************************\n")
fichier.write("Description du projet :"+Description+"\n")
fichier.close()