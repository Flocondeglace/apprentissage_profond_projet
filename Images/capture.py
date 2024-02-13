from PIL import ImageGrab
import json
import sys

""" Fonctionnement de l'appli :
- lancer avec python3 capture.py
- vous pouvez aussi lancer en définissant les extrémités du rectangle à screen : python3 capture.py 0 0 1920 1080
- vous pouvez aussi ajouter un nom à ajouter dans les noms des fichiers pour plus de précision (genre nom épisode) python3 capture.py mickey_mange_une_pomme ou python3 capture.py 0 0 1920 1080 mickey_mange_une_pomme
- saississez la touche correspondant au monsieur dont vous faites le screenshot
a = "mickey", 
z = "minnie", 
e = "donald", 
r = "daisy", 
q = "dingo", 
s = "pluto"
- ça sauvegarde tout seul dans le bon dossier c'est magique
- appuyer sur 'p' pour enregistrer les valeurs du dictionnaire maison (qui contient combien d'image on été prise pour chaque perso)
- et le tour est joué !
"""

# Paramètre Image
print(len(sys.argv))

if len(sys.argv) == 5 or len(sys.argv) == 6 :
    region = [int(x) for x in sys.argv[1:5]]
else :
    region = (0, 0, 1920, 1080)

# Ajout de l'extension
if len(sys.argv) == 6 :
    extension = sys.argv[5]
elif len(sys.argv) == 2 :
    extension = sys.argv[1]
else :
    extension = ""

print("région définie : " + str(region))

# Dictionnaire contenant les persos
print("---chargement des données---")
with open("sauvegarde.txt","r") as fp:
    maison = json.load(fp)
touches = dict(a = "mickey", z = "minnie", e = "donald", r = "daisy", q = "dingo", s = "pluto", t = "test")
print("donnée loadé : " + str(maison))
print("---debut de l'attente de screenshot---")

# Boucle de fonctionnement
while True :
    t = input("Saissisez une touche:\n")
    if t == "p":
        break
    if (t not in touches):
        print("touche non définie")
    else:
        img = ImageGrab.grab(region)
        perso = touches[t]
        maison[perso] += 1
        nom = perso + "/" + perso + "_" + str(maison[perso]) + "_" + extension + ".png"
        print(perso + " enregistré")
        img.save(nom)


# Sauvegarder le fichier
somme = 0
for i in maison:
	somme += maison[i]
print("total :" + str(somme))
with open ("sauvegarde.txt","w") as fp:
    json.dump(maison,fp)
print("---fichier sauvegardé---")
exit(0)
