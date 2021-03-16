
def main():
    pass

if __name__ == '__main__':
    main()

from PIL import Image
from PIL import ImageDraw

from IPython.display import display
import urllib.request

# ouvrir une image hébergée sur internet
im = Image.open(urllib.request.urlopen('https://raw.githubusercontent.com/hackathon-nsi/h7n-nsi-01/main/images/washington.bmp'))

# créer une nouvelle image vide
# le deuxième argument représente la taille de l'image et le troisième argument (optionnel) la couleur de remplissage au format RVB
im_new = Image.new("RGB", (450, 600), (60, 0, 65))

# informations sur l'image
print(im.format, im.size, im.mode)

# taille de l'image
width, height = im.size

# valeurs du pixel de coordonnées x, y (l'origine (0, 0) est en haut à gauche)

# valeurs des couleurs rouge, vert, bleu


# modification du pixel de coordonnées x, y

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

##def philip2():


