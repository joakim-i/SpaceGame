from pygame import Surface, draw, sprite, image, locals
from pygame.key import get_pressed
from Renderer import RenderableObject, Layer
from Projectile import Projectile
import pygame

class Characters():
    players = []

    @classmethod
    def update(cls, events):
        

        for player in cls.players:

            if (not get_pressed()[pygame.K_a]) and (not get_pressed()[pygame.K_d]):
                if player.x_vel > 0:
                    player.x_vel -= player.x_vel_cap/180
                    if player.x_vel < 0:
                      player.x_vel = 0      
                elif player.x_vel < 0:
                 player.x_vel += player.x_vel_cap/180
                 if player.x_vel > 0:
                      player.x_vel = 0   

            if get_pressed()[pygame.K_d]:
                if player.x_vel <= player.x_vel_cap:
                    player.x_vel += player.x_vel_cap/240
            if get_pressed()[pygame.K_a]:
                if player.x_vel >= -(player.x_vel_cap):
                    player.x_vel -= player.x_vel_cap/240
            player.move()


        for event in events:
            if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_SPACE):
                for gridx, modulerow in enumerate(player.modules): #row
                    for gridy, module in enumerate(modulerow): #column
                        Projectile((module.x, module.y), 0, -8)

        

class Module(RenderableObject):
    

    def __init__(self, player):
        super().__init__(Layer.PLAYER)

        self.sprite_core_hull = sprite.Sprite()
        self.sprite_core_hull.image = image.load('sprites/player/hullcore.png')

        self.x = player.x
        self.y = player.y
    

    def draw(self, surface):
        surface.blit(self.sprite_core_hull.image,(self.x, self.y))

    def destroy(self):
        pass

class Player():

    def __init__(self, pos: tuple):

        Characters.players.append(self)

        self.x = pos[0]
        self.y = pos[1]
        self.x_vel_cap = 2
        self.y_vel_cap = 2
        self.x_vel = 0
        self.y_vel = 0
        self.hp = 1000
        self.lenght = 3
        self.width = 3
        self.modules = [ [Module(self), Module(self), Module(self)], [Module(self)], [Module(self),Module(self),Module(self)] ] # Grid
        # self.modules, bla bla bla serialize from preset, aka json?
        

    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel
        for gridx, modulerow in enumerate(self.modules): #row
            for gridy, module in enumerate(modulerow): #column
                module.x = self.x + (gridx*32)
                module.y = self.y - (gridy*32)
