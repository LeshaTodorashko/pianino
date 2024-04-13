import pygame
pygame.init()

win_w = 1300
win_h = 550
WHITE = 255, 255, 255
GREY = 128, 128, 128
GREYB = 50, 50, 50
GREYS = 175, 175, 175
BLACK = 0, 0, 0
FPS = 60
clock = pygame.time.Clock()



class Button:
    def __init__(self, x, y, w, h, color, color2, sound, key):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = color
        self.key = key
        self.color2 = color2
        self.color1 = color
        self.count = 14
        self.sound = pygame.mixer.Sound(sound)
    def update(self):
        pygame.draw.rect(window, self.color, self.rect)
        self.animited()
    def click(self, event):
        if event.key == self.key:
            self.count = 14
            self.color = self.color2
            self.sound.play()
    def animited(self):
        if self.count > 0:
            self.count -= 1
            if self.count == 0:
                self.color = self.color1

btn = Button(50, 350, 50, 200, WHITE, GREY,"snd/do.ogg", pygame.K_q)
btn1 = Button(105, 350, 50, 200, WHITE, GREY, "snd/re.ogg",pygame.K_w)
btn2 = Button(160, 350, 50, 200, WHITE, GREY, "snd/mi.ogg", pygame.K_e)
btn3 = Button(215, 350, 50, 200, WHITE, GREY, "snd/fa.ogg", pygame.K_r)
btn4 = Button(270, 350, 50, 200, WHITE, GREY, "snd/sol.ogg", pygame.K_t)
btn5 = Button(325, 350, 50, 200, WHITE, GREY, "snd/lya.ogg", pygame.K_y)
btn6 = Button(380, 350, 50, 200, WHITE, GREY, "snd/si.ogg", pygame.K_u)

btn7 = Button(85, 350, 35, 150, BLACK, GREYB, "snd/do.ogg", pygame.K_1)
btn8 = Button(140, 350, 35, 150, BLACK, GREYB, "snd/do.ogg", pygame.K_2)
btn9 = Button(250, 350, 35, 150, BLACK, GREYB, "snd/do.ogg", pygame.K_3)


window = pygame.display.set_mode((win_w, win_h))


game = True
while game:
    window.fill(GREYS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN:
            btn.click(event)
            btn1.click(event)
            btn2.click(event)
            btn3.click(event)
            btn4.click(event)
            btn5.click(event)
            btn6.click(event)
            btn7.click(event)
            btn8.click(event)
            btn9.click(event)
    btn.update()
    btn1.update()
    btn2.update()
    btn3.update()
    btn4.update()
    btn5.update()
    btn6.update()
    btn7.update()
    btn8.update()
    btn9.update()
    pygame.display.update()
    clock.tick(FPS)
 