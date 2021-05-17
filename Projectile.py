from pygame import draw
from Particles import Effect
from Renderer import RenderableObject, Layer, Renderer
import gc,sys


class Projectiles():
    projectiles = []

    @classmethod
    def update(cls):
        for projectile in cls.projectiles[:]:
            if projectile.rangeremaining > 0:
                projectile.move()
            else:
                Effect.testEffect((projectile.x, projectile.y))
                cls.projectiles.remove(projectile)
                Renderer.renderList[4].remove(projectile)

class Projectile(RenderableObject):

    def __init__(self, pos: tuple, xspeedvar, yspeedvar, damagevar=100):
        super().__init__(Layer.PROJECTILES)
        Projectiles.projectiles.append(self)
        self.x = pos[0]
        self.y = pos[1]
        self.xspeed = xspeedvar
        self.yspeed = yspeedvar
        self.damage = damagevar
        self.rangeremaining = 500

    def move(self):
        self.x += self.xspeed
        self.y += self.yspeed
        self.rangeremaining -= abs(self.yspeed)

    def draw(self, screen):
        draw.circle(screen, (150, 150, 150), (int(self.x), int(self.y)), 5)

    def destroy(self):
        pass
    
