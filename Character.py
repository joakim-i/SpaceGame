from pygame import Surface, draw, sprite, image
from Renderer import RenderableObject, Layer


class Characters():
    players = []

    @classmethod
    def update(cls):
        for player in cls.players:
            player.move()

class Player(RenderableObject):

    def __init__(self, pos: tuple):
        super().__init__(Layer.PLAYER)
        Characters.players.append(self)

        #self.spritegroup_core = sprite.Group()
        
        self.sprite_core_hull = sprite.Sprite()
        self.sprite_core_hull.image = image.load('sprites/player/hullcore.png')

        #self.spritegroup_core.add(self.sprite_core_hull)

        self.x = pos[0]
        self.y = pos[1]
        self.x_vel_cap = 2
        self.y_vel_cap = 2
        self.x_vel = 0
        self.y_vel = 0
        self.hp = 1000
    


    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel

    def draw(self, surface):
        surface.blit(self.sprite_core_hull.image,(self.x, self.y))
