import pygame
pygame.init()

win_w = 1300
win_h = 600
WHITE = 255, 255, 255
GREY = 128, 128, 128
BLACK = 0, 0, 0



class Button:
    def __init__(self, x, y, w, h, color, sound):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = color
        self.sound = pygame.mixer.Sound(sound)
    def update(self):
        pygame.draw.rect(window, self.color, self.rect)
    def click(self, x, y):
        if self.rect.collidepoint(x, y):
            self.sound.play()

btn = Button(50, 350, 50, 200, WHITE, "snd/do.ogg")
btn1 = Button(105, 350, 50, 200, WHITE, "snd/re.ogg")
btn2 = Button(160, 350, 50, 200, WHITE, "snd/mi.ogg")
btn3 = Button(215, 350, 50, 200, WHITE, "snd/fa.ogg")
btn4 = Button(270, 350, 50, 200, WHITE, "snd/sol.ogg")
btn5 = Button(325, 350, 50, 200, WHITE, "snd/lya.ogg")
btn6 = Button(380, 350, 50, 200, WHITE, "snd/si.ogg")
#btn7 = Button(435, 350, 50, 200, WHITE, snd/do)


window = pygame.display.set_mode((win_w, win_h))


game = True
while game:
    window.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            btn.click(event.pos[0], event.pos[1])
            btn1.click(event.pos[0], event.pos[1])
            btn2.click(event.pos[0], event.pos[1])
            btn3.click(event.pos[0], event.pos[1])
            btn4.click(event.pos[0], event.pos[1])
            btn5.click(event.pos[0], event.pos[1])
            btn6.click(event.pos[0], event.pos[1])
    btn.update()
    btn1.update()
    btn2.update()
    btn3.update()
    btn4.update()
    btn5.update()
    btn6.update()
    pygame.display.update()
 