from PIL import Image
##from IPython.display import display
import urllib.request

# ouvrir une image hébergée sur internet
im = Image.open('PF.jpg')
# créer une nouvelle image vide
# le deuxième argument représente la taille de l'image et le troisième argument (optionnel) la couleur de remplissage au format RVB
# taille de l'image
width, height = im.size
im_new = Image.new("RGB", (width, height), (128, 128, 128))

# informations sur l'image
print(im.format, im.size, im.mode)


def eloi():

    # valeurs du pixel de coordonnées x, y (l'origine (0, 0) est en haut à gauche)
    for x in range(width) :
        for y in range(height) :
            pixel = im.getpixel((x, y))

    # valeurs des couleurs rouge, vert, bleu
            p_rouge = pixel[0]
            p_vert =  pixel[1]
            p_bleu =  pixel[2]

    # modification du pixel de coordonnées x, y
    ##        im.putpixel((x,y),(r,g,b))
            if p_rouge==0 and p_bleu==0 and p_vert==0:
                p_rouge=255

            im_new.putpixel((x,y),(p_rouge,p_vert,p_bleu))
    # affichage de l'image
##    im_new.save("sortie.png")
    im_new.show()



