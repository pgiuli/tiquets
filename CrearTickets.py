import os
import os.path
from time import sleep
from PIL import Image, ImageFont, ImageDraw



#Escollim Font
title_font = ImageFont.truetype('assets/font.ttf', 32)
#Assignem Resolucio
resolucio = 285, 119



def crearTickets(quantitat):
    #Creem una carpeta on guardarem els tickets
    if os.path.isdir("imatges") == False:
        os.mkdir("imatges")
    else:
        print("La carpeta amb els tiquets ja existeix! Elimina-la per crear-ne de nous!")
        sleep(3)
        exit()

    input("Presiona Enter per a començar...")

    i = 1
    while i < (quantitat + 1):
        #Obrim la imatge
        nom_imatge = 'assets/1.png'
        imatge = Image.open(nom_imatge) 

        #Text imatge
        text_imatge = str(i)

        #Fem imatge editable
        imatge_amb_text = ImageDraw.Draw(imatge)

        #Editem Imatge
        imatge_amb_text.text((525, 289), text_imatge, (0, 0, 0), font=title_font)

        #Guardem la imatge amb el text
        nom_imatge = 'imatges/' + str(i) + '_text.png'
        imatge.save(nom_imatge)
        print('Text colocat a la imatge : '+ str(i))

        #Obrim la imatge amb el text
        nom_imatge = 'imatges/' + str(i) + '_text.png'
        imatge = Image.open(nom_imatge) 

        #Canviem la resolucio
        imatge2 =imatge.resize(resolucio, Image.Resampling.LANCZOS)

        #Guardem la imatge amb la resolucio canviada
        nom_imatge = 'imatges/' + str(i) + '.png'
        imatge2.save(nom_imatge)

        #Eliminem la imatge amb el text unicament
        os.remove('imatges/' + str(i) + '_text.png')

        print('Finalitzada imatge : '+ str(i))

        i+=1
    
    print("""
    Finalitzat!
    """)

    input("Presiona Enter per a sortir...")



print("""Creador de tiquets de entrada al pàrquing.
Per: Spork
""")

input("Presiona Enter per a continuar...")

#Preguntem quants tickets volem crear
quantitat = int(input("Introdueix la quantitat de tickets a crear: "))

crearTickets(quantitat)