from PIL import Image
##from IPython.display import display
import urllib.request
# ouvrir une image hébergée sur internet
im = Image.open('PF.jpg')

# créer une nouvelle image vide
# le deuxième argument représente la taille de l'image et le troisième argument (optionnel) la couleur de remplissage au format RVB
##im_new = Image.new("RGB", (1000,1000), (128, 128, 128))

# informations sur l'image
print(im.format, im.size, im.mode)

# taille de l'image
width, height = im.size

    # valeurs du pixel de coordonnées x, y (l'origine (0, 0) est en haut à gauche)
def modif_jade():

    decalage = input ("Décalage de: ")
    decalage = int(decalage)
    im_new = Image.new("RGB", (width,height+decalage), (229, 190, 0))


    for i in range(width//decalage):
        for x in range(decalage*i,decalage*i+decalage//2):
            for y in range(height):
                pixel = im.getpixel((x, y))

                p_rouge = pixel[0]
                p_vert =  pixel[1]
                p_bleu =  pixel[2]

                im_new.putpixel((x,y+decalage),(p_rouge,p_vert,p_bleu))

    for i in range(width//decalage):
        for x in range(decalage*i+decalage//2,decalage*i+decalage):
            for y in range(height):
                pixel = im.getpixel((x, y))

                p_rouge = pixel[0]
                p_vert =  pixel[1]
                p_bleu =  pixel[2]

                im_new.putpixel((x,y),(p_rouge,p_vert,p_bleu))



##                if x<40:
##                    im_new.putpixel((x,y+40),(p_rouge,p_vert,p_bleu))
##                else:
##                    im_new.putpixel((x,y),(p_rouge,p_vert,p_bleu))

##    im_new.save('sortie.jpg')
    im_new.show()
modif_jade()
