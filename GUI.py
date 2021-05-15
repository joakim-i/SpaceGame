from pygame import Rect, draw, Surface, font
import pygame
from Renderer import Layer, RenderableObject

class MainMenu:
    buttonW = 200
    buttonH = 45
    origin = (600, 250)
    components = []
    active = True

    def __init__(self, screen: Surface):
        self.screen = screen
        self.buttonResume = Button(screen,
                                   self.buttonW, self.buttonH,
                                   self.origin[0] - int(self.buttonW/4), self.origin[1],
                                   text="Resume",
                                   layer=Layer.MAIN_MENU)
        self.buttonResume.setPressedEvent(lambda: self.setActive(False))
        self.components.append(self.buttonResume)

        self.buttonSave = Button(screen,
                                   self.buttonW, self.buttonH,
                                   self.origin[0] - int(self.buttonW/4), self.origin[1] + self.buttonH + 20,
                                   text="Save",
                                   layer=Layer.MAIN_MENU)
        self.buttonSave.setPressedEvent(lambda: print("NOT IMPLEMENTED"))
        self.components.append(self.buttonSave)

        self.buttonLoad = Button(screen,
                                 self.buttonW, self.buttonH,
                                 self.origin[0] - int(self.buttonW/4), self.origin[1] + self.buttonH * 2 + 40,
                                 text="Load",
                                 layer=Layer.MAIN_MENU)
        self.buttonLoad.setPressedEvent(lambda: print("NOT IMPLEMENTED"))
        self.components.append(self.buttonLoad)

        self.buttonOptions = Button(screen,
                                   self.buttonW, self.buttonH,
                                   self.origin[0] - int(self.buttonW/4), self.origin[1] + self.buttonH * 3 + 60,
                                   text="Options",
                                   layer=Layer.MAIN_MENU)
        self.buttonOptions.setPressedEvent(lambda: print("NOT IMPLEMENTED"))
        self.components.append(self.buttonOptions)

        self.buttonExit = Button(screen,
                                    self.buttonW, self.buttonH,
                                    self.origin[0] - int(self.buttonW/4), self.origin[1] + self.buttonH * 4 + 80,
                                    text="Exit",
                                    layer=Layer.MAIN_MENU)
        self.buttonExit.setPressedEvent(lambda: pygame.quit())
        self.components.append(self.buttonExit)

    def update(self, mousePos: tuple, leftMBIsPressed: bool = False):
        for component in self.components:
            component.update(mousePos, leftMBIsPressed)

    def draw(self):
        for component in self.components:
            component.draw()

    def testFunction(self):
        print("testFunction broder")

    def setActive(self, bool: bool):
        self.active = bool

    def isActive(self):
        return self.active

    def getComponentsList(self):
        return self.components

class Button(RenderableObject):
    hoverColor = (30, 30, 150)
    normalColor = (50, 50, 50)
    currentColor = normalColor

    def __init__(self, screen:Surface, width, height, x=0, y=0, color=(50,50,50), text="not set", fontSize=32, layer=Layer.UI):
        super().__init__(layer)
        self.screen = screen
        self.event = None
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.normalColor = color
        self.currentColor = self.normalColor
        self.buttonRect = Rect(self.x, self.y, self.width, self.height)
        self.font = font.SysFont(None, fontSize)
        self.text = text
        self.textRender = self.font.render(self.text, True, (255, 255, 255))

    def press(self):
        if self.event is not None:
            self.event()

    def update(self, mousePos: tuple, leftMBIsPressed: bool = False):
        if self.buttonRect.collidepoint(mousePos[0], mousePos[1]):
            self.useHoverColor()
            if leftMBIsPressed:
                self.press()
        else:
            self.useNormalColor()

    def draw(self, surface):
        draw.rect(surface, self.currentColor, self.buttonRect)
        surface.blit(self.textRender, (self.x + self.getTextOffsetX(), self.y + self.getTextOffsetY()))

    def setPressedEvent(self, lambdaFunction):
        self.event = lambdaFunction

    def setText(self, text):
        self.text = text
        self.textRender = self.font.render(self.text, True, (255, 255, 255))

    def getText(self):
        return self.text

    def getTextOffsetX(self):
        return (self.width - self.font.size(self.text)[0]) / 2

    def getTextOffsetY(self):
        return (self.height - self.font.size(self.text)[1]) / 2

    def useHoverColor(self):
        self.currentColor = self.hoverColor

    def useNormalColor(self):
        self.currentColor = self.normalColor
