import pygame
import sys
from random import randint as rd

x = 400
y = 600
jump = False
jc = 10
li = [[400, 700], [200, 650], [600, 550], [400, 450], [200, 350], [400, 250], [600, 150], [400, 50]]
pygame.init()

bg = pygame.image.load("Phon.PNG")
platform = pygame.image.load("platform.png")
mask_plat = pygame.mask.from_surface(platform)
pers = pygame.image.load("pers.png")
mask_pers = pygame.mask.from_surface(pers)
scale = pygame.transform.scale(platform, (150, 30))
scale2 = pygame.transform.scale(pers, (100, 100))
sc = pygame.display.set_mode((840, 840))
clock = pygame.time.Clock()
pygame.mixer.music.load('music.mp3')
font = pygame.font.Font(None, 50)
pygame.mixer.music.play(-1)

while True:
    if y > 750:
        text = font.render("Проигрыш!", True, (100, 255, 100))
        sc.blit(text, (400, 400))
        continue
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
    sc.blit(bg, [0, 0])
    for i in li:
        sc.blit(scale, [i[0], i[1]])
    sc.blit(scale2, [x, y])
    pygame.display.update()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x >= 0 and not jump:
        x -= 3
    elif keys[pygame.K_LEFT] and x >= 0:
        x -= 6
    elif keys[pygame.K_RIGHT] and x <= 760 and not jump:
        x += 3
    elif keys[pygame.K_RIGHT] and x <= 760:
        x += 6
    kl1 = 0
    kl2 = 0
    for i in li:
        if i[0] - 50 <= x <= i[0] + 110 and i[1] - 110 < y < i[1] - 70:
            kl1 = 1
            break
        elif not jump and i[1] - 110 < y < i[1] - 70 and not (i[0] - 50 <= x <= i[0] + 110):
            print("yeah")
            print(x, y)
            print(i)
            kl2 += 1
        if i[1] > 800:
            li.remove(i)
            x1 = rd(int(li[len(li) - 1][0] - 170), int(li[len(li) - 1][0]) + 170)
            y1 = int(li[len(li) - 1][1] - 170)
            if x1 < 100:
                x1 = li[len(li) - 1][0] + 170
            elif x1 > 750:
                x1 = li[len(li) - 1][0] - 170
            li.append([x1, y1])
    if not kl1 and kl2:
        jump = True
        jc = 0
    if keys[pygame.K_UP] and y >= 50:
        jump = True
    if jump is True:
        if y > 750:
            jump = False
            y = 749
            jc = 10
        elif jc >= -20:
            if jc < 0:
                y += (jc ** 2) // 2
            else:
                y -= (jc ** 2) // 2
            jc -= 1
            m = 110
            for i in li:
                if i[0] - 50 <= x <= i[0] + 110 and i[1] - 110 < y < i[1] - 70:
                    print(x, y)
                    jump = False
                    jc = 10
        else:
            print(x, y)
            print(jc)
            jump = False
            jc = 10
    for i in range(len(li)):
        li[i][1] += 1.5
    y += 1.5
    clock.tick(60)
