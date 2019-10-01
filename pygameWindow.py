import pygame
import constants

class PYGAME_WINDOW:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((constants.pygameWindowDepth,constants.pygameWindowWidth))

    def Prepare(self):
        self.screen.fill((255, 255, 255))

    def Reveal(self):
        pygame.display.update()

    def Draw_Black_Circle(self,x, y):
        pygame.draw.circle(self.screen, (0,0,0), (x, y), 10, 10)

    def Draw_Black_Line(self, xBase, yBase, xTip,yTip, b):
        if b == 0:
            pygame.draw.line(self.screen, (0,0,0), (xBase, yBase), (xTip, yTip), 4)
        elif b == 1:
            pygame.draw.line(self.screen, (0, 0, 0), (xBase, yBase), (xTip, yTip), 3)
        elif b == 2:
            pygame.draw.line(self.screen, (0, 0, 0), (xBase, yBase), (xTip, yTip), 2)
        else:
            pygame.draw.line(self.screen, (0, 0, 0), (xBase, yBase), (xTip, yTip), 1)