import pygame as pg

# button class
class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pg.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self,surface):  # add surface argument here for 'screen'.blit
        action = False
        # get mouse position
        pos = pg.mouse.get_pos()
        # check mouseover and clicked conditions
        # mouseget_pressed()[i]: 0:left mouse, 1:middle, 2:right mouse btn
        if self.rect.collidepoint(pos):
            if pg.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
            if pg.mouse.get_pressed()[0] == 0:
                self.clicked = False

        # draw button on screen
        surface.blit(self.image, (self.rect.x, self.rect.y))
        return action
