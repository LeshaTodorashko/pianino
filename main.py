import pygame
import os
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

# f1 = pygame.font.Font(None, 36)

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

                

# 1 октава
btn = Button(50, 350, 50, 200, WHITE, GREY,"snd/1.mp3", pygame.K_q)
btn1 = Button(105, 350, 50, 200, WHITE, GREY, "snd/2.mp3",pygame.K_w)
btn2 = Button(160, 350, 50, 200, WHITE, GREY, "snd/3.mp3", pygame.K_e)
btn3 = Button(215, 350, 50, 200, WHITE, GREY, "snd/4.mp3", pygame.K_r)
btn4 = Button(270, 350, 50, 200, WHITE, GREY, "snd/5.mp3", pygame.K_t)
btn5 = Button(325, 350, 50, 200, WHITE, GREY, "snd/6.mp3", pygame.K_y)
btn6 = Button(380, 350, 50, 200, WHITE, GREY, "snd/7.mp3", pygame.K_u)

# 2 октава
btn12 = Button(435, 350, 50, 200, WHITE, GREY, "snd/8.ogg", pygame.K_a)
btn13 = Button(490, 350, 50, 200, WHITE, GREY, "snd/9.ogg", pygame.K_s)
btn14 = Button(545, 350, 50, 200, WHITE, GREY, "snd/10.ogg", pygame.K_d)
btn15 = Button(600, 350, 50, 200, WHITE, GREY, "snd/11.ogg", pygame.K_f)
btn16 = Button(655, 350, 50, 200, WHITE, GREY, "snd/12.ogg", pygame.K_g)
btn17 = Button(710, 350, 50, 200, WHITE, GREY, "snd/13.ogg", pygame.K_h)
btn18 = Button(765, 350, 50, 200, WHITE, GREY, "snd/14.ogg", pygame.K_j)

# 3 октава
btn24 = Button(820, 350, 50, 200, WHITE, GREY, "snd/15.mp3", pygame.K_z)
btn25 = Button(875, 350, 50, 200, WHITE, GREY, "snd/16.mp3", pygame.K_x)
btn26 = Button(930, 350, 50, 200, WHITE, GREY, "snd/17.mp3", pygame.K_c)
btn27 = Button(985, 350, 50, 200, WHITE, GREY, "snd/18.mp3", pygame.K_v)
btn28 = Button(1040, 350, 50, 200, WHITE, GREY, "snd/19.mp3", pygame.K_b)
btn29 = Button(1095, 350, 50, 200, WHITE, GREY, "snd/20.mp3", pygame.K_n)
btn30 = Button(1150, 350, 50, 200, WHITE, GREY, "snd/21.mp3", pygame.K_m)

#диезы     1 октава
btn7 = Button(85, 350, 35, 150, BLACK, GREYB, "snd/8.ogg", pygame.K_1)
btn8 = Button(140, 350, 35, 150, BLACK, GREYB, "snd/8.ogg", pygame.K_2)
btn9 = Button(250, 350, 35, 150, BLACK, GREYB, "snd/8.ogg", pygame.K_3)
btn10 = Button(305, 350, 35, 150, BLACK, GREYB, "snd/8.ogg", pygame.K_4)
btn11 = Button(360, 350, 35, 150, BLACK, GREYB, "snd/8.ogg", pygame.K_5)

#          2 октавва
btn19 = Button(470, 350, 35, 150, BLACK, GREYB, "snd/8.ogg", pygame.K_6)
btn20 = Button(525, 350, 35, 150, BLACK, GREYB, "snd/8.ogg", pygame.K_7)
btn21 = Button(635, 350, 35, 150, BLACK, GREYB, "snd/8.ogg", pygame.K_8)
btn22 = Button(690, 350, 35, 150, BLACK, GREYB, "snd/8.ogg", pygame.K_9)
btn23 = Button(745, 350, 35, 150, BLACK, GREYB, "snd/8.ogg", pygame.K_0)

#          3 октава
btn31 = Button(855, 350, 35, 150, BLACK, GREYB, "snd/8.ogg", pygame.K_i)
btn32 = Button(910, 350, 35, 150, BLACK, GREYB, "snd/8.ogg", pygame.K_o)
btn33 = Button(1020, 350, 35, 150, BLACK, GREYB, "snd/8.ogg", pygame.K_p)
btn34 = Button(1075, 350, 35, 150, BLACK, GREYB, "snd/8.ogg", pygame.K_k)
btn35 = Button(1130, 350, 35, 150, BLACK, GREYB, "snd/8.ogg", pygame.K_l)


window = pygame.display.set_mode((win_w, win_h))



# text1 = f1.render('Клавиши расположены в таком порядке: Q W E R T Y U A S D F G H J Z X C V B N M', 1, (180, 0, 0))
# text2 = f1.render('Диезные клавиши расположены в таком порядке; 1 2 3 4 5 6 7 8 9 0 I O P K L', 1, (180, 0, 0))

game = True
while game:
    # window.blit(text1, (300, 550))
    # window.blit(text2, (10, 50))
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
            btn10.click(event)
            btn11.click(event)
            btn12.click(event)
            btn13.click(event)
            btn14.click(event)
            btn15.click(event)
            btn16.click(event)
            btn17.click(event)
            btn18.click(event)
            btn19.click(event)
            btn20.click(event)
            btn21.click(event)
            btn22.click(event)
            btn23.click(event)
            btn24.click(event)
            btn25.click(event)
            btn26.click(event)
            btn27.click(event)
            btn28.click(event)
            btn29.click(event)
            btn30.click(event)
            btn31.click(event)
            btn32.click(event)
            btn33.click(event)
            btn34.click(event)
            btn35.click(event)
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
    btn10.update()
    btn11.update()
    btn12.update()
    btn13.update()
    btn14.update()
    btn15.update()
    btn16.update()
    btn17.update()
    btn18.update()
    btn19.update()
    btn20.update()
    btn21.update()
    btn22.update()
    btn23.update()
    btn24.update()
    btn25.update()
    btn26.update()
    btn27.update()
    btn28.update()
    btn29.update()
    btn30.update()
    btn31.update()
    btn32.update()
    btn33.update()
    btn34.update()
    btn35.update()
    pygame.display.update()
    clock.tick(FPS)
 