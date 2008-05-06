import sys, pygame

pygame.init()

size = width, height = 800, 600
cor = 255, 255, 255
base_speed = [800, 600]

postrect = [None,None,None]
postespeed = [[0,0],[0,0],[0,0]]

screen = pygame.display.set_mode(size)

diskrect = [None, None, None, None, None, None, None]
diskspeed = [[0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0]]

base = pygame.image.load("images/base.gif")
poste = pygame.image.load("images/post.gif")

#Fazendo retangulos
baserect = base.get_rect()
postrect[0] = poste.get_rect()

#Criando um poste para caber as argolas
poste = pygame.transform.scale(poste, (postrect[0].width, postrect[0].height * 8))
poste.convert()

#Criando tres retangulos para os postes
for nrec in range(3):
    postrect[nrec] = poste.get_rect()

#Colocando a base no centro
base_speed[0] = (base_speed[0] / 2) - (baserect.width / 2)
base_speed[1] = base_speed[1] - baserect.height
baserect = baserect.move(base_speed)

screen.fill(cor) 
screen.blit(base, baserect)

for nrec in range(3):
    #postespeed[nrec][0] = (baserect.width / 6) * (2 * nrec + 1) - (postrect[nrec].width / 2) + (size[0]-baserect.width)/2
    
    #calculo da posicao das torres
    #ps = (bw / 6) * (2n + 1) - (pw / 2) + (size - bw) /2
    #ps = ((bw * 2n + bw) /6 ) - (pw / 2 + (size - bw) /2)
    #ps = (bw * 2n + bw - 3pw + 3size - 3bw) / 6
    #ps = ((bw * (2n -2)) - 3pw + 3size) / 6
    
    postespeed[nrec][0] = ((baserect.width * (2 * nrec - 2)) - 3 * postrect[nrec].width + 3 * size[0]) / 6
    
    postespeed[nrec][1] = size[1] - baserect.height - postrect[nrec].height
    
    #movendo os postes p/ a posicao correta
    postrect[nrec] = postrect[nrec].move(postespeed[nrec])

    #imprimindo os postes
    screen.blit(poste, postrect[nrec])
    
#carregando, posicionando e imprimindo discos
center_position = (baserect.width / 6) * 3 - (postrect[nrec].width / 2) + (size[0]-baserect.width)/2
disk_position = size[1] -  baserect.height 
for ndisk in range(6,-1,-1):
    disk = pygame.image.load("images/disk0%s.gif"%(ndisk+1))
    diskrect[ndisk] = disk.get_rect()
    
    disk_position -= diskrect[ndisk].height
    
    diskspeed[ndisk][0] = center_position
    diskspeed[ndisk][1] = disk_position
    diskrect[ndisk] = diskrect[ndisk].move(diskspeed[ndisk])
    screen.blit(disk, diskrect[ndisk])


pygame.display.flip()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
