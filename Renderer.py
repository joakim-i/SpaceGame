import abc
from enum import Enum


class Layer(Enum):

    MAIN_MENU = 7
    UI = 6
    PLAYER = 5
    ENEMY = 4
    BULLETS = 3
    PARTICLES = 2
    DECORATION = 1
    BACKGROUND = 0

class RenderableObject(metaclass=abc.ABCMeta):

    def __init__(self, layer: Layer):
        self.layer = layer.value
        Renderer.add_to_renderlist(self, layer)

    @abc.abstractmethod
    def draw(self, surface):
        pass

    @abc.abstractmethod
    def destroy(self):
        #Remove yourself from Renderer.renderList
        pass

class Renderer:

    renderList = [[], [], [], [], [], [], [], []]

    @classmethod
    def add_to_renderlist(cls, source_object: RenderableObject, layer: Layer):
        cls.renderList[layer.value].append(source_object)

    @classmethod
    def draw_all(cls, screen):
        for layer in cls.renderList:
            for renderable_object in layer:
                renderable_object.draw(screen)

    @classmethod
    def draw_background(cls, screen):
        for renderable_object in cls.renderList[Layer.BACKGROUND.value]:
            renderable_object.draw(screen)

    @classmethod
    def draw_particles(cls, screen):
        for renderable_object in cls.renderList[Layer.PARTICLES.value]:
            renderable_object.draw(screen)
        print(len(cls.renderList[2]))

    @classmethod
    def draw_main_menu(cls, screen):
        for renderable_object in cls.renderList[Layer.MAIN_MENU.value]:
            renderable_object.draw(screen)

    @classmethod
    def draw_player(cls, screen):
        for renderable_object in cls.renderList[Layer.PLAYER.value]:
            renderable_object.draw(screen)

    @classmethod
    def draw_enemies(cls, screen):
        for renderable_object in cls.renderList[Layer.ENEMY.value]:
            renderable_object.draw(screen)

    @classmethod
    def draw_decorations(cls, screen):
        for renderable_object in cls.renderList[Layer.DECORATION.value]:
            renderable_object.draw(screen)

    @classmethod
    def draw_bullets(cls, screen):
        for renderable_object in cls.renderList[Layer.BULLETS.value]:
            renderable_object.draw(screen)

    @classmethod
    def draw_UI(cls, screen):
        for renderable_object in cls.renderList[Layer.UI.value]:
            renderable_object.draw(screen)


class ExampleClass(RenderableObject):
    #Example of bare bones class with autorendering!
    #No need to call draw() method, it is done automaticly in correct order!

    def __init__(self):
        super().__init__(Layer.ENEMY)

    def draw(self, surface):
        #Can use conditional stuff here like return if u mom gay
        pass