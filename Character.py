from pygame import Surface, draw, sprite, image
from Renderer import RenderableObject, Layer


class Characters():
    players = []

    @classmethod
    def update(cls):
        for player in cls.players:
            player.move()

class Module(RenderableObject):
    

    def __init__(self, player):
        super().__init__(Layer.PLAYER)
        Characters.players.append(player)

        self.sprite_core_hull = sprite.Sprite()
        self.sprite_core_hull.image = image.load('sprites/player/hullcore.png')

        self.x = player.x
        self.y = player.y
    

    def draw(self, surface):
        surface.blit(self.sprite_core_hull.image,(self.x, self.y))

class Player():

    def __init__(self, pos: tuple):

        self.x = pos[0]
        self.y = pos[1]
        self.x_vel_cap = 2
        self.y_vel_cap = 2
        self.x_vel = 0
        self.y_vel = 0
        self.hp = 1000
        self.lenght = 3
        self.width = 3
        self.modules = [ [Module(self), Module(self), Module(self)], [Module(self)], [Module(self),Module(self),Module(self)] ]
        Characters.players.append(self)
        

    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel
        for gridx, modulerow in enumerate(self.modules):
            for gridy, module in enumerate(modulerow):
                module.x = self.x + (gridx*32)
                module.y = self.y - (gridy*32)