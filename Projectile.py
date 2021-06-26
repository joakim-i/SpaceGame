from pygame import Rect, draw
import pygame
from Particles import Effect
from Renderer import RenderableObject, Layer, Renderer


class Projectiles():

    ### STATIC ###

    projectiles = []

    @classmethod
    def update(cls):
        for projectile in cls.projectiles[:]:
            if projectile.rangeremaining > 0:
                projectile.move()
            else:
                projectile.destroy()



    ### INIT ###

class Projectile(RenderableObject):

    def __init__(self, pos: tuple, xspeedvar, yspeedvar, source, damagevar=100):
        super().__init__(Layer.PROJECTILES)
        Projectiles.projectiles.append(self)
        self.x = pos[0]
        self.y = pos[1]
        self.xspeed = xspeedvar
        self.yspeed = yspeedvar
        self.damage = damagevar
        self.rangeremaining = 350
        self.source = source
        self.team = source.team
        self.size = 8
        self.crudeHitbox = Rect(int(self.x-(self.size)), int(self.y-(self.size)), self.size*2, self.size*2)

    ### MOVE ###

    def move(self):
        self.x += self.xspeed
        self.y += self.yspeed
        self.rangeremaining -= abs(self.yspeed)

    ### DRAW ###

    def draw(self, screen):
        self.crudeHitbox = Rect(int(self.x-(self.size)), int(self.y-(self.size)), self.size*2, self.size*2)
        
        draw.circle(screen, (150, 150, 150, 20), (int(self.x), int(self.y)), self.size)
        pygame.draw.rect(screen, (0, 100, 255), self.crudeHitbox, 1)  # width 1 = outline


    ### DESTROY (MANDATORY) ###

    def destroy(self):
            Effect.testEffect([self.x, self.y])
            Renderer.renderList[self.layer].remove(self)
            Projectiles.projectiles.remove(self)