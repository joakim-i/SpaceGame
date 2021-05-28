from Particles import Effect
from pygame import Surface, draw, sprite, image, locals
from pygame.key import get_pressed
from Renderer import RenderableObject, Layer, Renderer
from Projectile import Projectile
import pygame

class Characters():
    players = []

    @classmethod
    def update(cls, events):
        

        for player in cls.players:

            #if (not get_pressed()[pygame.K_a]) and (not get_pressed()[pygame.K_d]):
            #    if player.x_vel > 0:
            #        player.x_vel -= player.x_vel_cap/180
            #        if player.x_vel < 0:
            #          player.x_vel = 0      
            #    elif player.x_vel < 0:
            #     player.x_vel += player.x_vel_cap/180
            #     if player.x_vel > 0:
            #          player.x_vel = 0

            player.x_vel_cap = 1
            player.y_vel_cap = 1
            for gridx, modulerow in enumerate(player.modules): #row
                for gridy, module in enumerate(modulerow): #column
                    if (type(module) == WingJetModule) or (type(module) == NoseModule):
                        player.x_vel_cap += module.xspeedstat
                        player.y_vel_cap += module.yspeedstat               




            if (not get_pressed()[pygame.K_a]) and (not get_pressed()[pygame.K_d]): #Halt movement in X if not moving left or right 
                player.x_vel = 0      
            if (not get_pressed()[pygame.K_w]) and (not get_pressed()[pygame.K_s]): #Halt movement in Y if not moving up or down 
                player.y_vel = 0      
   

            if get_pressed()[pygame.K_d]:
                player.x_vel = player.x_vel_cap
            if get_pressed()[pygame.K_a]:
                player.x_vel = -player.x_vel_cap
            if get_pressed()[pygame.K_a] and get_pressed()[pygame.K_d]:
                player.x_vel = 0
            
            if get_pressed()[pygame.K_w]:
                player.y_vel = -player.y_vel_cap
            if get_pressed()[pygame.K_s]:
                player.y_vel = player.y_vel_cap
            if get_pressed()[pygame.K_w] and get_pressed()[pygame.K_s]:
                player.y_vel = 0   
            player.move()



        for event in events:
            if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_SPACE):
                for gridx, modulerow in enumerate(player.modules): #row
                    for gridy, module in enumerate(modulerow): #column
                        if type(module) is GunModule:
                            Projectile((module.x, module.y), 0, -8)
                        if module is not None:
                            module.hp -= 40
                            if module.hp <= 0:
                                module.destroy()


class Module(RenderableObject):
    

    def __init__(self, player):
        super().__init__(Layer.PLAYER)
        self.player = player
        self.moduleSprite = sprite.Sprite()
        self.moduleSprite.image = image.load('sprites/player/hullcore.png')
        self.x = player.x
        self.y = player.y
        self.hp = 1600
        self.hpmax = 1600
    

    def draw(self, surface):
        surface.blit(self.moduleSprite.image,(self.x, self.y))

        colorMin = pygame.Color(0, 255, 0)
        colorMax = pygame.Color(255, 0, 0)
        colorHPrender = colorMax.lerp(colorMin, self.getHPpercent())
        pygame.draw.line(surface, colorHPrender, (self.x, (self.y+(self.getHPpercent()*32))), (self.x, self.y), 2)
        
    def destroy(self):
        for gridy, modulerow in enumerate(self.player.modules): #row
            for gridx, module in enumerate(modulerow): #column
                if module == self:
                    Effect.testEffect([self.x, self.y])
                    if self in Renderer.renderList[self.layer]:
                        Renderer.renderList[self.layer].remove(self)
                    self.player.modules[gridy][gridx] = None
    
    def getHPpercent(self):
        return self.hp / self.hpmax




class GunModule(Module):
    

    def __init__(self, player):
        super(GunModule, self).__init__(player)
        self.moduleSprite.image = image.load('sprites/player/gunmodule.png')
        self.hp = 1200
        self.hpmax = 1200

class WingJetModule(Module):
    

    def __init__(self, player, flipped: bool):
        super(WingJetModule, self).__init__(player)
        self.hp = 800
        self.hpmax = 800
        self.xspeedstat = 1
        self.yspeedstat = 1
        if flipped:
            self.moduleSprite.image = image.load('sprites/player/wingjetmodule.png')
        else:
            self.moduleSprite.image = image.load('sprites/player/wingjetmoduleinverted.png')

class NoseModule(Module):

    def __init__(self, player):
        super(NoseModule, self).__init__(player)
        self.hp = 600
        self.hpmax = 600
        self.xspeedstat = 1
        self.yspeedstat = 1
        self.moduleSprite.image = image.load('sprites/player/nosemodule.png')

class Player():

    def __init__(self, pos: tuple):

        Characters.players.append(self)

        self.x = pos[0]
        self.y = pos[1]
        self.x_vel_cap = 1
        self.y_vel_cap = 1
        self.x_vel = 0
        self.y_vel = 0
        self.lenght = 3
        self.width = 3
        self.modules = [ [None, NoseModule(self), None], [None, Module(self), None], [WingJetModule(self,False),GunModule(self),WingJetModule(self,True)] ] # Grid
        # self.modules, bla bla bla serialize from preset, aka json?
        

    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel
        for gridy, modulerow in enumerate(self.modules): #row
            for gridx, module in enumerate(modulerow): #column
                if module is not None:
                    module.x = self.x + (gridx*-32)
                    module.y = self.y - (gridy*-32)
