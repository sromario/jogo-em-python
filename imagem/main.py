import random
import pygame
pygame.init()

x= 1280   #convertendo médidas
y= 720

screen = pygame.display.set_mode((x,y))  #abrir tela
pygame.display.set_caption('meu jogo')  


bg = pygame.image.load('imagem/bg.jpg').convert_alpha() #convertendo tamanho tela
bg = pygame.transform.scale(bg, (x, y)) 


boneco = pygame.image.load('imagem/boneco.png').convert_alpha() #convertendo tamanho boneco
boneco = pygame.transform.scale(boneco, (90, 90 )) 



nave = pygame.image.load('imagem/nave.png').convert_alpha() #convertendo tamanho nave
nave = pygame.transform.scale(nave, (80, 80 ))



missil = pygame.image.load('imagem/missil.png').convert_alpha() #convertendo missil
missil = pygame.transform.scale(missil, (25, 25 )) 
missil = pygame.transform.rotate(missil, -45)



pos_nave_x = 500   #posição nave
pos_nave_y = 360  


pos_boneco_x = 200 #posição boneco
pos_boneco_y = 150   


vel_missil_x = 0  #posição missil
pos_missil_x = 200
pos_missil_y = 150

pontos = 4
triggered = False
rodando = True
font = pygame.font.SysFont('fonts/PixelGameFront.ttf', 50)

boneco_rect = boneco.get_rect() #colisão missil / alvo
nave_rect = nave.get_rect()
missil_rect = missil.get_rect()


def respawn():  #função lista
    x = 1350
    y = random.randint(1,640)
    return [x,y]

def respawn_missil(): #função respawn missil novamente
    triggered = False
    respawn_missil_x = pos_boneco_x
    respawn_missil_y = pos_boneco_y
    vel_missil_x = 0
    return [respawn_missil_x, respawn_missil_y, triggered, vel_missil_x]


def colisions():            #colisão pontos 
    global pontos 
    if boneco_rect.colliderect(nave_rect) or nave_rect.x == 60:
        pontos -= 1
        return True
    elif missil_rect.colliderect(nave_rect):
         pontos == pontos 
         return True
    else:
        return False

while rodando:   #possibilitar tela abrir, e encerrar no quit 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            rodando = False

    screen.blit(bg, (0,0)) 
    


    rel_x = x % bg.get_rect().width
    screen.blit(bg, (rel_x - bg.get_rect().width, 0)) #criar background
    if rel_x < 1280:
        screen.blit(bg, (rel_x, 0))


   
    tecla = pygame.key.get_pressed()         #teclas 
    if tecla[pygame.K_UP] and pos_boneco_y > 1:
       pos_boneco_y -= 1 
       if not triggered:  
           pos_missil_y -= 1

    if pontos == 0:
        rodando = False


    if tecla[pygame.K_DOWN] and pos_boneco_y < 665:
       pos_boneco_y += 1 
       if not triggered:
              pos_missil_y += 1


    if tecla[pygame.K_SPACE]:
        triggered = True
        vel_missil_x = 2

    if pos_nave_x == 50:         #respawn
        pos_nave_x = respawn()[0]
        pos_nave_y = respawn()[1]

    if pos_missil_x == 1300:
        pos_missil_x, pos_missil_y, triggered, vel_missil_x = respawn_missil()


    if pos_nave_x == 50 or colisions():
        pos_nave_x = respawn()[0]
        pos_nave_y = respawn()[1]

   
    boneco_rect.y = pos_boneco_y   #posição rect
    boneco_rect.x = pos_boneco_x

    nave_rect.y = pos_nave_y   
    nave_rect.x = pos_nave_x

    missil_rect.y = pos_missil_y   
    missil_rect.x = pos_missil_x
   
   
    x-=2            #movimento
    pos_nave_x -= 2

    pos_missil_x += vel_missil_x


    #pygame.draw.rect(screen , (255, 0, 0), boneco_rect, 4) 
    #pygame.draw.rect(screen , (255, 0, 0), nave_rect, 4) 
    #pygame.draw.rect(screen , (255, 0, 0), missil_rect, 4) 





    screen.blit(nave, (pos_nave_x, pos_nave_y)) #criando imagens
    screen.blit(missil, (pos_missil_x, pos_missil_y))
    screen.blit(boneco, (pos_boneco_x, pos_boneco_y)) 

    score = font.render(f' pontos {int(pontos)} ', True, (0,0,0))
    screen.blit(score, (50,50))

     
    print(pontos)

    pygame.display.update()