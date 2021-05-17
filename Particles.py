import random
from pygame import draw, Surface
from Renderer import Layer, RenderableObject

class Effect():
    particles = []

    @classmethod
    def explosion(cls, pos, particleAmount, reductionRate=0.1, speed=2):

        for x in range(0, particleAmount):
            cls.particles.append(_Particle(pos, reductionRate, speed))

    @classmethod
    def bullet_hit(cls, pos, speed, directionalVector):

        for x in range(0, 20):
            cls.particles.append(_Particle(pos, 0.2, speed, directionalVector))

    @classmethod
    def testEffect(cls, pos, particleAmount=250, reductionRate=0.08, speed=3):
        outerColor = (204, 0, 0)
        middleColor = (230, 153, 0)
        innerColor = (235, 235, 71)
        distribution = [0.2, 0.3, 0.5]
        for x in range(0, int(particleAmount*distribution[0])):
            cls.particles.append(_Particle(
                pos, reductionRate, speed/3,
                color=innerColor, radiusMin=3, radiusMax=7))

        for x in range(0, int(particleAmount*distribution[1])):
            cls.particles.append(_Particle(
                pos, reductionRate, speed/1.25,
                color=middleColor, radiusMin=2, radiusMax=6))

        for x in range(0, int(particleAmount*distribution[2])):
            cls.particles.append(_Particle(
                pos, reductionRate, speed*1.25,
                color=outerColor, radiusMin=2, radiusMax=4))


    @classmethod
    def update(cls):
        for particle in cls.particles:
            particle.update()
            if particle.isReadyToDie():
                cls.particles.remove(particle)
                del particle


class _Particle(RenderableObject):

    def __init__(self, pos, reductionRate, speed, directionalVector = None,
                 radiusMin=2, radiusMax=5,
                 color=(200, 150, 150)):
        super().__init__(Layer.PARTICLES)
        self.radius = random.randint(radiusMin, radiusMax)
        self.pos = pos
        self.reductionRate = reductionRate
        self.speed = random.uniform(0.5, 1.2)*speed
        self.color = color
        if directionalVector == None:
            self.directionalVector = (random.uniform(-1, 1), random.uniform(-1, 1))
        else:
            self.directionalVector = directionalVector

    def update(self):
        self.radius -= self.reductionRate
        self.pos = (self.pos[0] + self.speed*self.directionalVector[0],
                    self.pos[1] + self.speed*self.directionalVector[1])


    def isReadyToDie(self):
        if self.radius <= 0:
            return True
        else:
            return False


    def draw(self, surface):
        if self.radius > 0:
            draw.circle(surface, self.color, (int(self.pos[0]), int(self.pos[1])), int(self.radius))