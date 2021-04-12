#!/usr/bin/env python3

# -- Eloi v1.1 ---
from PIL import Image
from IPython.display import display
import urllib.request
from PIL import ImageDraw

# ouvrir une image hébergée sur internet
im = Image.open(urllib.request.urlopen('https://raw.githubusercontent.com/hackathon-nsi/h7n-nsi-01/main/images/washington.bmp'))

im_new = Image.new("RGB", (450, 600), (60, 0, 65))

# Traitement de l'image: Découpe de petites boites et intervertion des boites
# -----------------------

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

def philip():
    r=0
    g=0
    b=0

    a=0
    b=40
    c=0
    d=40
    f=100
    g=110
    h=100
    i=110

    for e in range (42):


        for y in range(a,b):
                for x in range(c,d):
                    pixel = im.getpixel((x, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[2]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x,y),(p_rouge,p_vert,p_bleu))

        for y in range(a,b+150):
                for x in range(c,d):
                    pixel = im.getpixel((x, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[2]
                    p_bleu =  pixel[1]
                    im_new.putpixel((x,y),(p_rouge,p_vert,p_bleu))

        for y in range(a-200,b+150):
                for x in range(c,d):
                    pixel = im.getpixel((x, y))
                    p_rouge = pixel[2]
                    p_vert =  pixel[0]
                    p_bleu =  pixel[1]
                    im_new.putpixel((x,y),(p_rouge,p_vert,p_bleu))

        for y in range(a-300,b+150):
                for x in range(c,d):
                    pixel = im.getpixel((x, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[2]
                    p_bleu =  pixel[0]
                    im_new.putpixel((x,y),(p_rouge,p_vert,p_bleu))

        for y in range(a-400,b+150):
                for x in range(c,d):
                    pixel = im.getpixel((x, y))
                    p_rouge = pixel[2]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x,y),(p_rouge,p_vert,p_bleu))


        for y in range(a+80,b+80):
            for x in range(c,d):
                pixel = im.getpixel((x, y))
                p_rouge = pixel[0]
                p_vert =  pixel[2]
                p_bleu =  pixel[0]
                p_rouge = 0
                im_new.putpixel((x,y),(p_rouge,p_vert,p_bleu))

        for x in range(c-80,d-80):
            for y in range(c,d):
                pixel = im.getpixel((x, y))
                p_rouge = pixel[0]
                p_vert =  pixel[0]
                p_bleu =  pixel[2]
                p_rouge = 100
                im_new.putpixel((x,y),(p_rouge,p_vert,p_bleu))


        a=a+10
        b=b+10
        c=c+10
        d=d+10
        f=f-10
        g=g-10
        h=h-10
        i=i-10


    ImageDraw.Draw(im_new).rectangle([(200,1),(1,50)])


    # affichage de l'image
    display(im)
    #im.show()
    im_new.show()

# affichage de l'image
# display(im)
im.show()