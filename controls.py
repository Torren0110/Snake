import pygame
from texts import *

class tickBox:
    correction = 10

    def __init__(self, WIN, colors, pos, text = "", initialVal = False, side = 20):
        self.WIN = WIN
        self.pColor, self.sColor, self.tColor = colors
        self.fg, self.bg = self.pColor, self.sColor
        self.x, self.y = pos
        self.side = side
        self.text = text
        renderText = H2.render(text, True, self.pColor)
        textRect = renderText.get_rect()
        self.length = textRect.size[0] + side
        self.val = initialVal
        self.mouseCng = pygame.mouse.get_pressed()[0]

    def show(self):
        renderText = H2.render(self.text, True, self.fg)
        textRect = renderText.get_rect()
        textRect.center = (self.x + self.side + self.correction, self.y)
        self.WIN.blit(renderText, textRect)
        pygame.draw.rect(self.WIN, self.fg, [self.x - (self.length / 2) + (self.side / 2) - self.correction, self.y - self.side / 2, self.side, self.side])
        temp = pygame.draw.rect(self.WIN, self.bg, [self.x - (self.length / 2) + (self.side / 2) - self.correction + 1, self.y - (self.side / 2) + 1, self.side - 2, self.side - 2])
        if(self.val):
            pygame.draw.circle(self.WIN, self.fg, temp.center, (self.side / 2) - 2)

    def onWidge(self):
        mousePosx, mousePosy = pygame.mouse.get_pos()

        if(mousePosx >= self.x - self.length / 2 - self.correction and mousePosx <= self.x + self.length / 2 + self.correction and mousePosy >= self.y - self.side and mousePosy <= self.y + self.correction):
            return True
        
        return False

    def update(self):
        currMouse = pygame.mouse.get_pressed()[0]
        if(self.onWidge()):
            self.fg = self.tColor
            if(self.mouseCng and not currMouse):
                self.val = not self.val
        else:
            self.fg = self.pColor
        
        self.mouseCng = currMouse


class slider:
    def __init__(self, WIN, colors, pos, length, span, initialVal = None, label = ""):
        self.WIN = WIN
        self.pColor, self.sColor = colors
        self.fg, self.bg = colors
        self.x, self.y = pos
        self.length = length
        self.begin, self.end = span

        if(initialVal == None or initialVal < self.begin or initialVal > self.end):
            self.val = self.begin + (self.end - self.begin) / 2
        else:
            self.val = initialVal

        self.pos = self.x + ((self.length / self.end - self.begin) * self.val - self.begin)

        self.label = label

    def set_color(self, ncolor):
        self.pColor, self.sColor = ncolor

    def show(self):
        renderLabel = H2.render(self.label, True, self.pColor)
        labelRect = renderLabel.get_rect()
        labelRect.center = (self.x + (self.length / 2), self.y - 30)

        renderVal = H2.render(str(int(self.val)), True, self.pColor)
        valRect = renderVal.get_rect()
        valRect.center = (self.x + (self.length / 2), self.y + 35)

        pygame.draw.rect(self.WIN, self.pColor, [self.x, self.y, self.length, 5], border_radius = 50)
        self.cir = pygame.draw.circle(self.WIN, self.fg, [self.pos, self.y + 2.5], 10)
        pygame.draw.circle(self.WIN, self.bg, [self.pos, self.y + 2.5], 8)
        pygame.draw.circle(self.WIN, self.fg, [self.pos, self.y + 2.5], 6)
        self.WIN.blit(renderLabel, labelRect)
        self.WIN.blit(renderVal, valRect)

        
    def update(self):
        x, y = pygame.mouse.get_pos()
        if(self.cir.collidepoint(x, y)):
            self.fg = self.sColor
            self.bg = self.pColor
        else:
            self.fg = self.pColor
            self.bg = self.sColor

        if(pygame.mouse.get_pressed()[0] and x >= self.x and x <= self.x + self.length + 1 and y >= self.y - 20 and y <= self.y + 20):
            self.pos = x
            self.val = self.begin + ((self.pos - self.x) / (self.x + self.length - self.x)) * (self.end - self.begin)

    def getVal(self):
        return int(self.val)


class button:
    def __init__(self, WIN, colors, dim, text = ""):
        self.WIN = WIN
        self.pColor, self.sColor = colors
        self.x , self.y, self.l, self.b = dim
        self.bg = self.pColor
        self.fg = self.sColor
        self.text = text

        self.renderText = H2.render(self.text, True, self.fg)
        self.textRect = self.renderText.get_rect()
        self.textRect.center = (self.x + (self.l / 2), self.y + (self.b / 2))

        self.state = False
    
    def show(self):
        pygame.draw.rect(self.WIN, self.bg, [self.x, self.y, self.l, self.b])
        pygame.draw.rect(self.WIN, self.fg, [self.x + 2, self.y + 2, self.l - 4, self.b - 4])
        pygame.draw.rect(self.WIN, self.bg, [self.x + 4, self.y + 4, self.l - 8, self.b - 8])
        self.WIN.blit(self.renderText, self.textRect)
    
    def onButton(self):
        mouse_pos = pygame.mouse.get_pos()
        if(mouse_pos[0] >= self.x and mouse_pos[0] <= self.x + self.l and mouse_pos[1] >= self.y and mouse_pos[1] <= self.y + self.b):
            return True
        return False

    def update(self):
        if(self.onButton()):
            self.fg = self.pColor
            self.bg = self.sColor
        else:
            self.fg = self.sColor
            self.bg = self.pColor
        
        self.renderText = H2.render(self.text, True, self.fg)
        self.textRect = self.renderText.get_rect()
        self.textRect.center = (self.x + (self.l / 2), self.y + (self.b / 2))
    
    def clicked(self):
        if(self.onButton() and not pygame.mouse.get_pressed()[0] and self.state):
            self.state = pygame.mouse.get_pressed()[0]
            return True
        self.state = pygame.mouse.get_pressed()[0]
        return False

class pauseButton(button):
    paused = False

    def show(self):
        pygame.draw.rect(self.WIN, self.bg, [self.x, self.y, self.l, self.b])
        pygame.draw.rect(self.WIN, self.fg, [self.x + 2, self.y + 2, self.l - 4, self.b - 4])
        pygame.draw.rect(self.WIN, self.bg, [self.x + 4, self.y + 4, self.l - 8, self.b - 8])

        if(self.paused):
            pygame.draw.polygon(self.WIN, self.fg, [[self.x + 12, self.y + 10], [self.x + self.b - 12, self.y + (self.l / 2)], [self.x + 12, self.y + self.b - 10]])
        else:
            pygame.draw.rect(self.WIN, self.fg, [self.x + 8, self.y + 8, self.l / 4, self.b - 16])
            pygame.draw.rect(self.WIN, self.fg, [self.x + self.l - 8 - self.l / 4, self.y + 8, self.l / 4, self.b - 16])
        
    def clicked(self):
        if(self.onButton() and not pygame.mouse.get_pressed()[0] and self.state):
            self.state = pygame.mouse.get_pressed()[0]
            self.paused = not self.paused

            return True
        self.state = pygame.mouse.get_pressed()[0]
        return False
