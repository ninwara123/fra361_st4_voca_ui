import pygame as pg
import cv2
pg.init()

eng_alphabet = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']

regis_success = 0
class Text():
    def __init__(self, x, y,size,font,color,type,text):
        self.color = color
        self.font = font
        self.x = x
        self.y = y
        self.type = type
        self.size = size
        self.text = text
    def draw(self,screen):
        font = pg.font.SysFont(self.font,self.size)
        text = font.render(self.text,True,self.color)
        if self.type == 1:
            textRect = (self.x,self.y)
            screen.blit(text,textRect)
        if self.type == 2:
            textRect = text.get_rect()
            textRect.center = (self.x//2, self.y//2)
            screen.blit(text, textRect)
    def ison(self,screen):
        (poX, poY) = pg.mouse.get_pos()
        if poX in range(self.x, self.x + 200) and poY in range(self.y, self.y + 150):

            if pg.mouse.get_pressed()[0] == 0:
                self.color = (255,33,73)
                font = pg.font.SysFont(self.font, self.size)
                text = font.render(self.text, True, self.color)
                textRect = (self.x, self.y)
                screen.blit(text, textRect)
                screen.blit(text, textRect)
    def submit(self):
        (poX, poY) = pg.mouse.get_pos()
        if poX in range(self.x, self.x + 200) and poY in range(self.y, self.y + 150) and pg.mouse.get_pressed()[0] == 1:
            return True




class Button():
    def __init__(self,x=0,y=0,w=0,h=0):
        self.x = x # Position X
        self.y = y # Position Y
        self.w = w # Width
        self.h = h # Height
        self.rect = pg.Rect(x, y, w, h)
    # def __init__(self, x=0, y=0, w=0, h=0):
    #     Rec.__init__(self, x, y, w, h)
        self.status = False
    def mouse_on(self):
        (pos_x, pos_y) = pg.mouse.get_pos()
        if self.x <= pos_x <= self.x + self.w and self.y <= pos_y <= self.y + self.h:
            self.status = True
        else:
            self.status = False
        return self.status
class InputBox:

    def __init__(self, x, y, w, h, fontsize ,space_in_y,text='  '):
        self.rect = pg.Rect(x, y, w, h)
        self.color = (0,0,0)  # inactive color
        self.text = text
        self.fontsize = fontsize
        self.space_in_y = space_in_y
        # self.font = pg.font.SysFont("comicsans", fontsize)
        self.font = pg.font.SysFont("browallianewbold", fontsize)
        self.txt_surface = self.font.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):

        if event.type == pg.MOUSEBUTTONDOWN:  # ทำการเช็คว่ามีการคลิก Mouse หรือไม่
            if self.rect.collidepoint(event.pos):  # ทำการเช็คว่าตำแหน่งของ Mouse อยู่บน InputBox นี้หรือไม่
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False

            self.color = pg.Color('dodgerblue2') if self.active else pg.Color((0,0,0))  # เปลี่ยนสีของ InputBox

        if event.type == pg.KEYDOWN:
            if self.active:

                if event.key == pg.K_RETURN:
                    self.active = not self.active
                    self.color = pg.Color('lightskyblue3') if self.active else pg.Color('dodgerblue2')

                if event.key == pg.K_BACKSPACE:
                    if len(self.text)>2:
                        self.text = self.text[:-1]
                else:
                    if len(self.text)<= 18:
                        if event.unicode.isdigit():
                            self.text += event.unicode
                        if event.unicode in eng_alphabet:
                            self.text += event.unicode
                # Re-render the text.
                self.txt_surface = self.font.render(self.text, True, pg.Color("black"))
                pg.display.update()

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width())
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x, self.rect.y+self.space_in_y))
        # Blit the rect.
        pg.draw.rect(screen, self.color, self.rect, 2)
    

    

