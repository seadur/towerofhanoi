# -*- coding: utf-8 -*-
# vi:si:et:sw=4:sts=4:ts=4

"""
by:
    Bruno dos Santos
    Bruno Gomes
"""
import sys, pygame
from objects import Disk, Base, Torre
from pygame.locals import *

class Hanoi:
    """Jogo baseado em torres de hanoi.
    
    Este jogo tem a finalidade de estudo da biblioteca pygame
    """
    def __init__(self, nivel=4, width=800, height=600, cor = (255, 255, 255) ):
        pygame.init()
        self.nivel = nivel
        self.size = width, height
        self.cor = cor
        self.key = None
        self.torre_atual = 1

        #Criando objetos
        print "Criando interface..."
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("Torre de Hanoi")

        print "Criando piso..."
        self.criar_piso()
        
        print "Criando torres..."
        self.criar_torres(n=3)
        
        print "Adicionando discos na torre do meio"
        for ndisk in range(self.nivel, -1, -1):
            self.torres[self.torre_atual].push(Disk(ndisk))

        #Imprimindo objetos na tela
        self.monta_tela()

    def monta_tela(self):
        #Cor de fundo
        self.screen.fill(self.cor)

        #Exibe piso
        self.screen.blit(self.piso.picture, self.piso.rect)

        #Exibe torres
        for torre in self.torres:
            self.screen.blit(torre.picture, torre.rect)
            
            if torre.numero == self.torre_atual:
                #Seleciona disco da torre atual
                d = self.torres[self.torre_atual].read()
                if d:
                    d.hover_picture()
                
            #Montando discos nas torre
            self.monta_torre(torre)

        
        pygame.display.flip()

    def criar_piso(self):
        self.piso = Base()
        #Colocando a base no centro
        self.piso.move((self.size[0] / 2) - (self.piso.width / 2), self.size[1] - self.piso.height)

    def criar_torres(self, n=3):
        self.torres = [Torre(nivel=self.nivel, numero = nt) for nt in range(n)]
        for torre in self.torres:
            #Dividindo o espaco do piso em n pedacos para as torres
            left = ((self.piso.width * (2 * torre.numero - 2)) \
                                      - n * torre.width + n * self.size[0]) / 6
            top = self.piso.y - torre.height
            torre.move(left, top)

    def monta_torre(self, torre, discos=[]):
        """Monta os discos na torre"""
    
        #Remove todos os discos para colocar uma nova pilha de discos
        while discos and torre.pop():
            pass

        #Adiciona os discos na torre
        for d in discos:
            torre.push(d)
            print "Adicionando: %s " % d

        ds = torre.stack
        area = self.piso.y
        for d in ds:
            left = torre.center()[0] - d.width / 2
            top = area - (len(ds) - (len(ds) - ds.index(d) - 1)) * d.height
            d.move(left, top)
            self.screen.blit(d.picture, d.rect)

    def valida_torre_atual(self):
        if self.torre_atual < 0: self.torre_atual = len(self.torres)-1
        if self.torre_atual > len(self.torres)-1: self.torre_atual = 0

    def move_torre(self,at):
        self.valida_torre_atual()
        d = self.torres[self.torre_atual].read()
        if d and d < self.torres[at].read() :
            self.torre_atual = at
        else:
            d = self.torres[at].pop()
            self.torres[self.torre_atual].push(d)

    def move_prox_torre(self, at):
        self.torre_atual += 1
        self.move_torre(at)

    def move_ante_torre(self, at):
        self.torre_atual -= 1
        self.move_torre(at)
    
    def seleciona_prox_torre(self):
        self.torre_atual += 1
        self.valida_torre_atual()
        if self.torres[self.torre_atual].num_elements == 0:
            self.seleciona_prox_torre()

    def seleciona_ante_torre(self):
        self.torre_atual -= 1
        self.valida_torre_atual()
        if self.torres[self.torre_atual].num_elements == 0:
            self.seleciona_ante_torre()

    def game(self, k):
        d = self.torres[self.torre_atual].read()
        if d:
            d.load_picture()
            
        if k == K_RIGHT:
            self.move_prox_torre(self.torre_atual)

        elif k == K_LEFT:
            self.move_ante_torre(self.torre_atual)

        elif k == K_UP:
            self.seleciona_prox_torre()
            
        elif k ==  K_DOWN:
            self.seleciona_ante_torre()

        self.monta_tela()

    def run_game(self):
        """ Main loop of game."""
        
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == KEYUP:
                    if event.key == K_RIGHT or event.key == K_LEFT \
                       or event.key == K_UP or event.key == K_DOWN:
                        self.game(event.key)

if __name__ == '__main__':
    game = Hanoi()
    game.run_game()
