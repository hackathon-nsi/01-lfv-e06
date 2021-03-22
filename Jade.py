from PIL import Image
##from IPython.display import display
import urllib.request
# ouvrir une image hébergée sur internet
im = Image.open(urllib.request.urlopen('https://raw.githubusercontent.com/hackathon-nsi/h7n-nsi-01/main/images/washington.bmp'))

# créer une nouvelle image vide
# le deuxième argument représente la taille de l'image et le troisième argument (optionnel) la couleur de remplissage au format RVB
##im_new = Image.new("RGB", (1000,1000), (128, 128, 128))

# informations sur l'image
print(im.format, im.size, im.mode)

# taille de l'image
width, height = im.size
im_new = Image.new("RGB", (width+40,height+40), (128, 128, 128))


    # valeurs du pixel de coordonnées x, y (l'origine (0, 0) est en haut à gauche)
def modif_jade():

    for i in range(width//40):
        for x in range(40*i,40*i+20):
            for y in range(height):
                pixel = im.getpixel((x, y))

                p_rouge = pixel[0]
                p_vert =  pixel[1]
                p_bleu =  pixel[2]

                if x<40:
                    im_new.putpixel((x,y+40),(p_rouge,p_vert,p_bleu))
                else:
                    im_new.putpixel((x,y),(p_rouge,p_vert,p_bleu))

##    im_new.save('sortie.jpg')
    im_new.show()