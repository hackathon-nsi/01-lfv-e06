#!/usr/bin/env python3

# -- Eloi v1.1 ---
from PIL import Image
from IPython.display import display
import urllib.request

# ouvrir une image hébergée sur internet
im = Image.open(urllib.request.urlopen('https://raw.githubusercontent.com/hackathon-nsi/h7n-nsi-01/main/images/washington.bmp'))


# Traitement de l'image: Découpe de petites boites et intervertion des boites
# -----------------------



def technique_5():
    # decoupe (crop) de 4 régions
    # La région est définie par 4 valeurs, où les coordonnées sont:
    # gauche, supérieure, droite, inférieure.
    box1 = (400, 160, 440, 190)
    region1 = im.crop(box1)
    
    box2 = (300, 150, 340, 180)
    region2 = im.crop(box2)
    
    box3 = (250, 160, 290, 190)
    region3 = im.crop(box3)
    
    box4 = (350, 200, 390, 230)
    region4 = im.crop(box4)
    
    # Intervertion
    im.paste(region4, box1)
    
    im.paste(region3, box2)
    
    im.paste(region1, box3)
    
    im.paste(region2, box4)

    # affichage de l'image
    # display(im)
    im.show()

technique_5()


