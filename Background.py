import random
from pygame import draw, gfxdraw
import math
from Renderer import RenderableObject, Layer, Renderer

class ScrollingBG:

    stars = []

    def __init__(self, size, starAmount, screen, color=(200, 230, 220)):
        self.size = size
        self.starAmount = starAmount
        self.screen = screen
        self.screenW, self.screenH = screen.get_size()
        for x in range(starAmount):
            self.stars.append(Star(
                math.floor(random.random() * self.screenW),
                math.floor(random.random() * self.screenH),
                self.screenH,
                self.screenW,
                color
            ))

    def update(self, speedMultiplier=1):
        for star in self.stars:
            star.move(speedMultiplier)



class Star(RenderableObject):
    x, y = 300, 500

    def __init__(self, x, y, screenH, screenW, color):
        super().__init__(Layer.BACKGROUND)
        self.radius = random.randrange(-3, 4)
        self.x = x
        self.y = y
        self.screenH = screenH
        self.screenW = screenW
        self.speed = self.radius / 15
        self.color = color

    def draw(self, screen):
        if self.radius > 0:
            gfxdraw.aacircle(screen, int(self.x), int(self.y), self.radius, self.color)
            gfxdraw.filled_circle(screen, int(self.x), int(self.y), self.radius, self.color)
        else:
            draw.rect(screen, self.color, (int(self.x), int(self.y), 1, 1))

    def move(self, speedMultiplier=1):
        if self.radius > 0:
            self.y += self.speed * speedMultiplier
            if self.y > self.screenH:
                self.y = -self.radius*2
                self.x = math.floor(random.random() * self.screenW)

    def destroy(self):
        pass