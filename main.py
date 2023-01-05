def play(player="pers.png"):
    import pygame
    import sys
    from random import randint as rd

    x = 400
    y = 585
    jump = False
    jc = 10
    li = [[400, 700], [600, 550], [400, 450], [400, 250], [600, 150], [400, 50]]
    li2 = li[:]
    pr = 0.5
    helper = 49
    now_help = 0
    score = 0
    max_score = 0
    pygame.init()

    bg = pygame.image.load("Phon.PNG")
    platform = pygame.image.load("platform.png")
    pers = pygame.image.load(player)
    butterfly = pygame.image.load("butterfly.png")
    scale = pygame.transform.scale(platform, (150, 30))
    scale2 = pygame.transform.scale(pers, (80, 120))
    scale3 = pygame.transform.scale(butterfly, (100, 100))
    sc = pygame.display.set_mode((840, 840))
    clock = pygame.time.Clock()
    pygame.mixer.music.load('music.mp3')
    font = pygame.font.Font(None, 60)
    font2 = pygame.font.Font(None, 50)
    # pygame.mixer.music.play(-1)

    while True:
        text_lives = font.render(f"Жизни: {now_help}", True, (0, 255, 0))
        sc.blit(text_lives, (0, 0))
        text_score = font.render(f"Счет: {int(score)}", True, (255, 255, 0))
        sc.blit(text_score, (0, 40))
        pygame.display.flip()
        if y > 750 and now_help == 0:
            if score > max_score:
                max_score = score
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    sys.exit()
            text = font.render("Проигрыш!", True, (255, 50, 50))
            text2 = font2.render("Чтобы начать заново, нажмите пробел.", True, (255, 50, 50))
            sc.blit(text, (320, 300))
            sc.blit(text2, (100, 400))
            pygame.display.flip()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                print("nu i huyi")
                li = li2
                try:
                    x, y = li[1][0], li[1][1] - 100
                except:
                    x, y = 400, 500
                jump = False
                jc = 10
                pr = 0.5
                score = 0
            continue
        elif y > 750:
            now_help -= 1
            x, y = li[-1][0], li[-1][1]
            print("coords")
            print(x, y)
            pr = 0.5
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                sys.exit()
        sc.blit(bg, [0, 0])
        for i in li:
            if len(i) == 2:
                sc.blit(scale, [i[0], i[1]])
            else:
                sc.blit(scale, [i[0], i[1]])
                try:
                    sc.blit(scale3, [i[0] + 30, i[1] - 90])
                except:
                    None
        sc.blit(scale2, [x, y])
        pygame.display.flip()
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
                if helper >= 50:
                    li.append([x1, y1, 1])
                    helper = 0
                else:
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
                        helper += 1
                        if len(i) == 3 and i[2] == 1:
                            now_help += 1
                            i[2] = 0
                            try:
                                del scale3
                            except:
                                None
            else:
                print(x, y)
                print(jc)
                jump = False
                jc = 10
        for i in range(len(li)):
            li[i][1] += pr
        y += pr
        score += 0.02
        pr += 0.001
        clock.tick(60)
