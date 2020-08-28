import random
from pygame import draw
import math

class ScrollingBG:

    stars = []

    def __init__(self, size, starAmount, screen):
        self.size = size
        self.starAmount = starAmount
        self.screen = screen
        self.screenW, self.screenH = screen.get_size()
        for x in range(starAmount):
            self.stars.append(Star(
                math.floor(random.random() * self.screenW),
                math.floor(random.random() * self.screenH),
                self.screenH,
                self.screenW
            ))


    def Scroll(self):
        for star in self.stars:
            star.draw(self.screen)
            star.move()
        pass



class Star:
    x, y = 300, 500
    color = (200, 230, 220)

    def __init__(self, x, y, screenH, screenW):
        self.radius = random.randrange(1, 8)
        self.speed = self.radius / 10
        self.x = x
        self.y = y
        self.screenH = screenH
        self.screenW = screenW

    def draw(self, screen):
        draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius, 0)

    def move(self):
        self.y += self.speed
        if self.y > self.screenH:
            self.y = -self.radius*2
            self.x = math.floor(random.random() * self.screenW)