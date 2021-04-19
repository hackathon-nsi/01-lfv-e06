
from PIL import Image
from PIL import ImageDraw

from IPython.display import display
import urllib.request

# ouvrir une image hébergée sur internet
im = Image.open('PF.jpg')

# créer une nouvelle image vide
# le deuxième argument représente la taille de l'image et le troisième argument (optionnel) la couleur de remplissage au format RVB
im_new = Image.new("RGB", (866, 587), (60, 0, 65))

# informations sur l'image
print(im.format, im.size, im.mode)

# taille de l'image
width, height = im.size






def jade():




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





def eloi():
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

    im.show()

def philip():
    r=0
    g=0
    b=0

    a=0
    b=40
    c=0
    d=40


    for e in range (40):


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

        for y in range(a,b):
                for x in range(c,d+150):
                    pixel = im.getpixel((x, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[2]
                    p_bleu =  pixel[1]
                    im_new.putpixel((x,y),(p_rouge,p_vert,p_bleu))

        for y in range(a,b):
                for x in range(c,d+300):
                    pixel = im.getpixel((x, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[2]
                    p_bleu =  pixel[1]
                    im_new.putpixel((x,y),(p_rouge,p_vert,p_bleu))

        for y in range(a,b):
                for x in range(c,d+400):
                    pixel = im.getpixel((x, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[2]
                    p_bleu =  pixel[1]
                    im_new.putpixel((x,y),(p_rouge,p_vert,p_bleu))

        ImageDraw.Draw(im_new).rectangle([(200,a),(b,50)])



        a=a+8
        b=b+9
        c=c+8
        d=d+9

    for w in range(20):
        for y in range(a,b):
                for x in range(c,d+420):
                    pixel = im.getpixel((x, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[2]
                    p_bleu =  pixel[1]
                    im_new.putpixel((x,y),(p_rouge,p_vert,p_bleu))

        ImageDraw.Draw(im_new).rectangle([(400,c),(d,100)])

        c=c-7
        d=d-10
        a=a-20
        b=b-15

    cropped = im_new.crop((100,100,800,450))


    # affichage de l'image
    display(im)
    #im.show()
    cropped.show()

menu = input ("Quelle programme voulez-vous executez: Programme <<1>> qui fait décalé,\n"
    "Programme <<2>> qui deplace \n"
    "ou Programme <<3>> qui change les couleurs et se raproche:\n"
    "Option 1\n"
    "Option 2\n"
    "Option 3\n")

if menu == str("1"):
    jade()
elif menu == str("2"):
    eloi()
elif menu == str("3"):
    philip()
