import random
from pygame import draw, Surface
from Renderer import Layer, RenderableObject, Renderer


class Effect():
    particles = []

    @classmethod
    def explosion_test(cls, pos, particleAmount, reductionRate=0.1, speed=2):

        for x in range(0, particleAmount):
            cls.particles.append(_Particle(pos, reductionRate, speed))

    @classmethod
    def bullet_hit(cls, pos, speed, directionalVector):

        for x in range(0, 20):
            cls.particles.append(_Particle(pos, 0.2, speed, directionalVector))

    #HowTo: instansiate emitter and update it, ex: emitter = Effect.emitter. emitter.update()
    @classmethod
    def emitter(cls, pos, direction, emittion_amount=1, particle_amount=2, speed=2, reductionRate = 0.02, colors=None, delta_varians=.2):
        return _Emitter(pos, direction, emittion_amount, particle_amount, speed, reductionRate, colors, delta_varians)

    @classmethod
    def explosion(cls, pos, particleAmount=250, reductionRate=0.08, speed=3):
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
                particle.destroy()


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

    def destroy(self):
        if self in Renderer.renderList[self.layer]:
            Renderer.renderList[self.layer].remove(self)
        if self in Effect.particles:
            Effect.particles.remove(self)



    def draw(self, surface):
        if self.radius > 0:
            draw.circle(surface, self.color, (int(self.pos[0]), int(self.pos[1])), int(self.radius))


class _Emitter:
    def __init__(self, pos, direction, emittion_amount=1, particle_amount=2, speed=2, reductionRate = 0.05, colors=None, delta_varians=0.2):
        if colors is None:
            self.colors = [(204, 0, 0), (230, 153, 0), (235, 235, 71)]
        else:
            self.colors = colors

        self.direction = direction
        self.particle_amount = particle_amount
        self.pos = pos
        self.reductionRate = reductionRate
        self.speed = speed
        self.emittion_amount = emittion_amount
        self.delta_varians = delta_varians

    @property
    def direction(self):
        return self._direction

    @direction.setter
    def direction(self, value):
        if len(value) < 2 or len(value) > 2:
            raise ValueError("direction needs to be tuple of size 2")
        if value[0] < -1 or value[0] > 1 or value[1] < -1 or value[1] > 1:
            raise ValueError("direction needs to be between -1 and 1. example: (-1, .5)")
        self._direction = value

    def update(self, pos):
        for x in range(0, self.emittion_amount):
            Effect.particles.append(_Particle(
                pos, self.reductionRate, self.speed,
                color=random.choice(self.colors), radiusMin=3, radiusMax=7, directionalVector=(self.direction[0] + random.uniform(-self.delta_varians, self.delta_varians), self.direction[1])))
