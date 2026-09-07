import pygame

pygame.init()

#font
font = pygame.font.SysFont(None, 150)
font_2 = pygame.font.SysFont(None, 50)

#sound and music
pygame.mixer.init()

pygame.mixer.music.load("music.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.5)
jump_sound = pygame.mixer.Sound("jump.mp3")


screen = pygame.display.set_mode((1200, 800))

#caption and icon
pygame.display.set_caption("...T-rex...")
icon = pygame.image.load("dino.png")
pygame.display.set_icon(icon)

#craete player
player_img = pygame.image.load("dino.png")
player_img = pygame.transform.scale(player_img, (80, 80))
player_x = 100
player_y = 500
jump = False
fall = False
game_over = False


#cactus
cactus_img = pygame.image.load("Cactus.webp")
cactus_img = pygame.transform.scale(cactus_img, (30, 90))

cactus = [[600, 500, 1], [1000, 500, 1]]

#main loop
running = True
while running:
    event = pygame.event.get()
    for e in event:
        if e.type == pygame.QUIT:
            running = False

    #timer
    if not game_over:
        ticks = pygame.time.get_ticks()
    millis = ticks % 1000
    seconds = int(ticks/1000 % 60)
    minutes = int(ticks/60000 % 24)
    out ='{minutes:02d}:{seconds:02d}'.format(minutes=minutes, seconds=seconds)

    if seconds > 30:
        time = font_2.render(out, True, (0, 0, 0))
    else:
        time = font_2.render(out, True, (255, 255, 255))


    dino_rect = player_img.get_rect(topleft = (player_x, player_y))

    #jump
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and not jump and not game_over:
        jump = True
        jump_sound.play()

    if jump and not fall and not game_over:
        player_y -= 1
        if player_y <= 310:
            fall = True
    
    if jump and fall and not game_over:
        player_y += 1
        if player_y >= 500:
            fall = False
            jump = False
    #background
    if seconds > 30:
        game_over_txt = font.render(f"Game Over", True, (255, 255, 255))
    else:
        game_over_txt = font.render(f"Game Over", True, (0, 0, 0))
    for i in cactus:
        cactus_rect = cactus_img.get_rect(topleft = (i[0], i[1] + 25))
        i[0] -= i[2]

        if dino_rect.colliderect(cactus_rect):
            break

        if i[0] < -20:
            i[0] = 1200

    #game over
    if dino_rect.colliderect(cactus_rect):
        if seconds > 30: 
            game_over_txt = font.render(f"Game Over", True, (0, 0, 0))
        else:
            game_over_txt = font.render(f"Game Over", True, (255, 255, 255))
        
        
        for i in cactus:
            i[2] = 0
            game_over = True
    
    
    #screen
    if seconds > 30:
        screen.fill((255, 255, 255))
    else:
        screen.fill((0, 0, 0))
    screen.blit(time, (800, 40))
    screen.blit(player_img, (player_x, player_y))
    for i in cactus:
        screen.blit(cactus_img, (i[0], i[1]))
    screen.blit(game_over_txt, (300, 200))

    
    pygame.display.update()