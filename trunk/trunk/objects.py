# -*- Mode: Python; coding: utf-8 -*-
# vi:si:et:sw=4:sts=4:ts=4

"""Gerenciador de objetos do jogo torre de hanoi

Autor:
 - Bruno
"""
import sys, pygame

class base:
    def __init__(self, posicao = (0,0)):
        self.load_picture("images/base.gif")
        self.posicao = posicao
        
    def get_picture(self):
        return self.picture
        
    def load_picture(self, new_picture):
        self.picture = pygame.image.load(new_picture)
        self.rect = self.picture.get_rect()

    def move(self,speed):
        self.posicao = speed
        self.rect = self.rect.move(speed)
        
    @property
    def width(self):
        return(self.rect.width)

    @property
    def height(self):
        return(self.rect.height)

    def get_x(self):
        return(self.posicao[0])
        
    def move_x(self, value):
        self.posicao[0] = value
        self.rect = self.rect.move(self.speed)

    x = property(get_x,move_x)

    def get_y(self):
        return(self.posicao[1])
        
    def move_y(self, value):
        self.posicao[1] = value
        self.rect = self.rect.move(self.speed)

    y = property(get_y,move_y)
    
    def center(self):
        x = self.x + self.width / 2
        y = self.y + self.height / 2
        return (x, y)


class disk(base):
    """Disco da torre de hanoi
    
    gerencia diamentros, posicao x e y
    verifica se poder assumir possicao
    """
    def __init__(self, diametro, posicao=(0,0)):
        self.load_picture("images/disk0%s.gif" %diametro)
        self.posicao = posicao
        self.diametro = diametro

    def __lt__(self, other):
        return self.diametro < other.diametro    
        
class torre(base):
    def __init__(self, numero, altura = 8, posicao = (0,0)):
        self.load_picture("images/post.gif")
        self.numero = numero
        self.resize(altura)
        self.posicao = posicao
        self.stack = stack()
    
    def resize(self, altura):
        self.picture = pygame.transform.scale(self.picture, (self.rect.width, self.rect.height * altura))
        self.picture.convert()
        self.rect = self.picture.get_rect()
    
    def add_disk(self, disk):
        self.stack.push(disk)
        
    def remove_disk(self):
        disk = self.stack.pop()
        return disk
        
    def is_valid_disk(self, disk):
        return (disk < self.stack.read())
               
class stack:
    def __init__(self):
          self.stack = []

    def push(self, object):
        self.stack.append(object)

    def pop(self):
        if len(self.stack) == 0:
            raise "Error", "stack is empty"
        obj = self.stack[-1]
        del self.stack[-1]
        return obj
        
    def read(self):
        if not self.is_empty:
            return self.stack[-1]
        raise "Error", "stack is empty"

    def is_empty(self):
        if len(self.stack) == 0:
            return 1
        return 0

    def num_elements(self):
        return len(self.stack)

    def dump_stack(self):
        print "Top of stack is last element in list (number 1)"
        n = len(self.stack)
        fmt = "  %%%dd  %%s" % len(`n + 1`)
        for ix in xrange(n):
            print fmt % (n - ix, self.stack[ix])
            
