#!/usr/bin/env python3

# -- Eloi v1.2 ---
from PIL import Image
from random import *
from IPython.display import display
import urllib.request

# ouvrir une image hébergée sur internet
im = Image.open(urllib.request.urlopen('https://raw.githubusercontent.com/hackathon-nsi/h7n-nsi-01/main/images/washington.bmp'))


# Traitement de l'image: Découpe de petites boites et intervertion des boites
# -----------------------

# Disposer (piocher) les boites avec une boucle à des endroits aléatoires

# On crée une liste de variables box 
box_list = ["box1", "box2", "box3", "box4", "box5", "box6", "box7", "box8"]

# une liste de variables de régions
region_list = ["region1", "region2", "region3", "region4", "region5", "region6", "region7", "region8"]

# Création manuelle(provisoire) des valeurs de bords gauches
bords_gauches = [150, 200, 250, 300, 350, 400, 450, 500]

# Création avec une boucle des bords droits qui sont les bords gauches + 40
bords_droits = []
for i in range(0,len(bords_gauches) -1):
    bords_droits.append(bords_gauches[i] + 40)

# Création manuelle(provisoire) des valeurs de bords hauts
bords_hauts = [160, 150, 160, 150, 160, 150, 160, 150]

# Création avec une boucle des bords bas qui sont les bords hauts + 30
bords_bas = []
for i in range(0,len(bords_hauts) -1):
    bords_bas.append(bords_hauts[i] + 30)

# Attribuer les morceaux d'images (boites) à des variables
# créer les listes de coordonnées
coord = []
for (g, d, h, b) in zip(bords_gauches,bords_droits,bords_hauts,bords_bas):
    coord.append((g,d,h,b))


#Maintenant on attribue les coordonnées aux variables
for i in range(0,len(coord)):
    globals()[box_list[i]] = coord[i]

    
# On crope les régions définies ci-dessus (box...)
for i in range(0,len(coord)):
    globals()[region_list[i]] = im.crop(coord[i])


# et maintenant on réordonne les crops et on les affiches
# Test manuel mais qui ne fonctionne pas .....
im.paste(region4, box1)

im.paste(region3, box2)

im.paste(region1, box3)

im.paste(region2, box4)


    
# Afficher l'image transformée

im.show()


