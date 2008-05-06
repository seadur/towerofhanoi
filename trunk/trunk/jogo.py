import sys, pygame, pdb
from objects import disk, base, torre

class Hanoi:
                        
    def __init__(self):
        pygame.init()

        size = width, height = 800, 600
        cor = 255, 255, 255
        self.screen = pygame.display.set_mode(size)
        
        self.piso = base()

        #Colocando a base no centro
        self.piso.move(((size[0] / 2) - (self.piso.width / 2), size[1] - self.piso.height))
        #base_speed[0] = (base_speed[0] / 2) - (baserect.width / 2)
        #base_speed[1] = base_speed[1] - baserect.height
        
        self.screen.fill(cor)
        self.screen.blit(self.piso.picture, self.piso.rect)
        
        torres = [torre(numero = ntorres) for ntorres in range(3)]
        for t in torres:
            x = ((self.piso.width * (2 * t.numero - 2)) - 3 * t.width + 3 * size[0]) / 6
            y = size[1] - self.piso.height - t.height
            t.move((x, y))
            self.screen.blit(t.picture, t.rect)
            
        #centro = (baserect.width / 6) * 3 - (postrect[nrec].width / 2) + (size[0]-baserect.width)/2
        #z = (x /6) * 3 - (y/2) + ((w-y)/2)
        #z = (x /2)  - (y/2) + w/2 -y/2
        #z = (x /2)  - y + w/2 

        discos = [disk(ndisk) for ndisk in range(6,-1,-1)]
        self.monta_torre(torres[1], discos)
        pygame.display.flip()
    
    def monta_torre(self, torre, discos):
        area = self.piso.y
        for d in discos:
            disk_position = torre.center()[0] - d.width / 2
            altura = area - (len(discos) - (len(discos) - discos.index(d) - 1)) * d.height
            d.move((disk_position, altura))
            self.screen.blit(d.picture, d.rect)
            torre.add_disk(d)
                                        
    def run_game(self):
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
           
if __name__ == '__main__':
    game = Hanoi()
    game.run_game()
