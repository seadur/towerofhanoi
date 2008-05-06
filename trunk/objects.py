# -*- Mode: Python; coding: utf-8 -*-
# vi:si:et:sw=4:sts=4:ts=4

"""Gerenciador de objetos do jogo torre de hanoi

Autor:
 - Bruno Santos <bsanto@gmail.com>
 - Bruno Gomes <bgomes@s1solucoes.com.br>
"""
import sys, pygame

class base:
    def __init__(self, top=0 , left=0 ,picture="images/base.gif"):
        self.load_picture(picture)

    def load_picture(self, new_picture):
        self.picture = pygame.image.load(new_picture)
        self.rect = self.picture.get_rect()

    def move(self,left,top):
        self.rect.top = top
        self.rect.left = left
        
    @property
    def width(self):
        return(self.rect.width)

    @property
    def height(self):
        return(self.rect.height)

    def get_x(self):
        return(self.rect.left)
        
    def move_x(self, value):
        self.rect.left = value

    x = property(get_x,move_x)

    def get_y(self):
        return(self.rect.top)
        
    def move_y(self, value):
        self.rect.top = value
        
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
    def __init__(self, diametro, left=0, top=0):
        self.diametro = diametro
        base.__init__(self, left = left, top = top, picture="images/disk0%s.gif" % self.diametro)

    def __lt__(self, other):
        return self.diametro < other.diametro
    
    def __repr__(self):
        return "Disk %s instance" % self.diametro

    def load_picture(self,picture=None):
        base.load_picture(self,"images/disk0%s.gif" %self.diametro)

    def hover_picture(self):
        base.load_picture(self,"images/disk0%s_h.gif" %self.diametro)

class stack:
    def __init__(self):
          self.stack = []

    def push(self, disk):
        if disk:
            self.stack.append(disk)

    def pop(self):
        if len(self.stack) == 0:
            return False
        return self.stack.pop()
        
    def read(self):
        if len(self.stack) == 0:
            return False
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack)

    @property
    def num_elements(self):
        return len(self.stack)

    def dump_stack(self):
        print "Top of stack is last element in list (number 1)"
        n = len(self.stack)
        fmt = "  %%%dd  %%s" % len(`n + 1`)
        for ix in xrange(n):
            print fmt % (n - ix, self.stack[ix])

class torre(stack,base):
    def __init__(self, numero, nivel , left = 0, top =0):
        stack.__init__(self)
        base.__init__(self,left=left,top=top,picture="images/post.gif")
        self.numero = numero
        self.nivel = nivel+2
        self.resize()
    
    def resize(self):
        self.picture = pygame.transform.scale(self.picture, (self.width, self.height * self.nivel))
        self.picture.convert()
        self.rect = self.picture.get_rect()

    def is_valid_disk(self, disk):
        return (disk < self.read())
