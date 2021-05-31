from Particles import Effect
from Renderer import RenderableObject, Layer, Renderer
import gc,sys
from pygame import Surface, draw, sprite, image


class Projectiles:
    projectiles = []

    @classmethod
    def update(cls):
        for projectile in cls.projectiles[:]:
            if projectile.is_ready_to_die():
                projectile.destroy()
            else:
                projectile.update()

class Projectile(RenderableObject):

    def __init__(self, pos: tuple, xspeed, yspeed, damage, range_remaining):
        super().__init__(Layer.PROJECTILES)
        Projectiles.projectiles.append(self)
        self.x = pos[0]
        self.y = pos[1]
        self.xspeed = xspeed
        self.yspeed = yspeed
        self.damage = damage
        self.range_remaining = range_remaining
        self.sprite = sprite.Sprite()
        self.sprite.image = None
        self.emitter = None
        self.x_offset = 0
        self.y_offset = 0

    def update(self):
        self.x += self.xspeed
        self.y += self.yspeed
        self.range_remaining -= abs(self.yspeed)
        if self.emitter is not None:
            self.emitter.update((self.x + self.x_offset, self.y + self.y_offset))

    def is_ready_to_die(self):
        if self.range_remaining <= 0:
            self.destroy()

    def draw(self, screen):
        screen.blit(self.sprite.image, (self.x, self.y))

    def destroy(self):
        Projectiles.projectiles.remove(self)
        Renderer.renderList[Layer.PROJECTILES.value].remove(self)


class Bullet(Projectile):
    def __init__(self, pos: tuple, xspeed=0, yspeed=-12, damage=1, range_remaining=600):
        super(Bullet, self).__init__(pos, xspeed, yspeed, damage, range_remaining)
        self.sprite.image = image.load('sprites/projectiles/bullet.png')

class Rocket(Projectile):
    def __init__(self, pos: tuple, xspeed=0, yspeed=-4, damage=1, range_remaining=350):
        super(Rocket, self).__init__(pos, xspeed, yspeed, damage, range_remaining)
        self.x_offset = 5
        self.y_offset = 40
        self.sprite.image = image.load('sprites/projectiles/rocket.png')
        self.emitter = Effect.emitter((self.x, self.y), (0, 1), delta_varians=.2, reductionRate=.1)

    def destroy(self):
        Effect.explosion((self.x, self.y), 800, 0.02, 2.5)
        Projectiles.projectiles.remove(self)
        Renderer.renderList[Layer.PROJECTILES.value].remove(self)
