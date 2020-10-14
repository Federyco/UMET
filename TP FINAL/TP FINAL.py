import pygame
from pygame import mixer

# inicializando el pygame
pygame.init()
# contienen el tamaño de la pantalla
display_width = 1240
display_height = 900
# creacion de la pantalla de juego
screen = pygame.display.set_mode((display_width,display_height))
# si quiero full screen asi es
# screen = pygame.display.set_mode((800,600), pygame.FULLSCREEN)
# reloj
clock = pygame.time.Clock()
# boleano que maneja el inicio y fin del juego
game_on = True
# titulo de pantalla
pygame.display.set_caption("Find Me")
# Carga de imagenes
rectangulo_objeto_1 = pygame.image.load('../images/sprite.png')
# Icono
icon = pygame.image.load('../images/wizard.png')
# fondo pantalla
background = pygame.image.load('../images/Background.png')
# Musica
#mixer.music.load('../Music/Master_History.wav')
#mixer.music.play(-1)
black = (255,255,255)

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def button(msg, x,y,w,h, action=None):
    score=0
    mouse = pygame.mouse.get_pos()
    click_derecho = pygame.mouse.get_pressed()
    if (x+w > mouse[0] > x and y+h > mouse[1] > y):
            button_1=pygame.draw.rect(screen,(150,150,150), (x,y,w,h))
            if(click_derecho[0] == 1 and action !=None):
                contador=0
                if(action == "found"):
                    contador = 1
                    print("asdf")
                    dibujo_el_fondo()
                    pygame.display.update()
                    #remove(button_1)

            
    smallText = pygame.font.Font("freesansbold.ttf", 20)
    TextSurf, TextRect = text_objects(msg, smallText)
    TextRect.center =   (x+round(((w/2))), (y+round(((h/2)))))
    screen.blit(TextSurf, TextRect)
    

def dibujo_el_fondo():
     screen.blit(background, (0,0))

def remove(object):
    del object 

# icono
pygame.display.set_icon(icon)
while game_on:
    button("Encontrado", 1027,557,280,180, "found")
    dibujo_el_fondo() 
    #construccion_de_rectangulos()
    # Dibujo el fondo de la pantalla
    #dibujo_el_fondo() 
    
    
    #ubicación_de_objetos()



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_on = False #game_off
            pygame.quit()
            quit()    
    pygame.display.update()
            

