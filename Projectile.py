from pygame import draw


class Projectile():

    def __init__(self, posx, posy, xspeedvar, yspeedvar, damagevar=100):
        self.x = posx
        self.y = posy
        self.xspeed = xspeedvar
        self.yspeed = yspeedvar
        self.damage = damagevar

    def move(self):
        self.x += self.xspeed
        self.y += self.yspeed

    def destroy(self):
        pass

    def draw(self, screen):
        draw.circle(screen, (150, 150, 150), (self.x, self.y), 5)
