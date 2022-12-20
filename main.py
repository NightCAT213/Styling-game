import pygame
import sys

x = 750
y = 750
jump = False
jc = 10
li = [(400, 700), (200, 600), (500, 500)]
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
#pygame.mixer.music.play(-1)

while True:
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
        x -= 5
    elif keys[pygame.K_RIGHT] and x <= 760 and not jump:
        x += 3
    elif keys[pygame.K_RIGHT] and x <= 760:
        x += 5
    for i in li:
        if not jump and i[1] - 110 < y < i[1] - 70 and not (i[0] - 50 <= x <= i[0] + 110):
            print("yeah")
            jump = True
            jc = -5
    if keys[pygame.K_UP] and y >= 50:
        jump = True
    if jump is True:
        if y > 750:
            jump = False
            y = 749
            jc = 10
        elif jc >= -10:
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
            print(jump)
        else:
            jump = False
            jc = 10
    clock.tick(60)
