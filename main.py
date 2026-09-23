import pygame

pygame.init()

# Font
font = pygame.font.SysFont(None, 150)
font_2 = pygame.font.SysFont(None, 50)

# Sound and music
pygame.mixer.init()

pygame.mixer.music.load("music.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.5)

jump_sound = pygame.mixer.Sound("jump.mp3")

# Screen
screen = pygame.display.set_mode((1200, 800))

# Caption and icon
pygame.display.set_caption("...T-rex...")

icon = pygame.image.load("dino.png")
pygame.display.set_icon(icon)

# Player
player_img = pygame.image.load("dino.png")
player_img = pygame.transform.scale(player_img, (80, 80))

player_x = 100
player_y = 500

# Jump settings
jump = False
jump_velocity = 0
gravity = 0.65
jump_power = -18

# Game settings
game_over = False
game_over_time = 0

# Cactus
cactus_img = pygame.image.load("Cactus.webp")
cactus_img = pygame.transform.scale(cactus_img, (30, 90))

cactus = [
    [600, 500],
    [1000, 500]
]

# Timer
start_time = pygame.time.get_ticks()
ticks = 0

# Clock
clock = pygame.time.Clock()

# Main loop
running = True

while running:

    # Events
    for e in pygame.event.get():

        if e.type == pygame.QUIT:
            running = False

        # Jump
        if e.type == pygame.KEYDOWN:

            if e.key == pygame.K_SPACE:

                if not jump and not game_over:

                    jump = True
                    jump_velocity = jump_power

                    jump_sound.play()

    # Timer
    if not game_over:
        ticks = pygame.time.get_ticks() - start_time

    total_seconds = ticks // 1000

    minutes = total_seconds // 60
    seconds = total_seconds % 60

    out = f"{minutes:02d}:{seconds:02d}"

    # Timer color
    if total_seconds > 30:
        time = font_2.render(
            out,
            True,
            (0, 0, 0)
        )
    else:
        time = font_2.render(
            out,
            True,
            (255, 255, 255)
        )

    # --------------------------------
    # GAME SPEED
    # --------------------------------

    game_speed = 4

    # Increase speed every 10 seconds
    game_speed += total_seconds // 10

    # Maximum speed
    if game_speed > 12:
        game_speed = 12

    # --------------------------------
    # JUMP
    # --------------------------------

    if jump and not game_over:

        player_y += jump_velocity
        jump_velocity += gravity

        # Land
        if player_y >= 500:

            player_y = 500
            jump = False
            jump_velocity = 0

    # Player rectangle
    dino_rect = player_img.get_rect(
        topleft=(player_x, player_y)
    )

    # --------------------------------
    # CACTUS
    # --------------------------------

    for i in cactus:

        cactus_rect = cactus_img.get_rect(
            topleft=(i[0], i[1] + 25)
        )

        # Move cactus
        if not game_over:
            i[0] -= game_speed

        # Reset cactus
        if i[0] < -50 and not game_over:
            i[0] = 1200

        # Collision
        if not game_over and dino_rect.colliderect(cactus_rect):

            game_over = True

            game_over_time = pygame.time.get_ticks()

            # Stop dinosaur movement
            jump = False
            jump_velocity = 0

            # Stop music
            pygame.mixer.music.stop()

    # --------------------------------
    # GAME OVER TEXT
    # --------------------------------

    if total_seconds > 30:

        game_over_txt = font.render(
            "Game Over",
            True,
            (0, 0, 0)
        )

    else:

        game_over_txt = font.render(
            "Game Over",
            True,
            (255, 255, 255)
        )

    # --------------------------------
    # BACKGROUND
    # --------------------------------

    if total_seconds > 30:

        screen.fill((255, 255, 255))

    else:

        screen.fill((0, 0, 0))

    # Timer
    screen.blit(
        time,
        (1050, 40)
    )

    # Player
    screen.blit(
        player_img,
        (player_x, player_y)
    )

    # Cactus
    for i in cactus:

        screen.blit(
            cactus_img,
            (i[0], i[1])
        )

    # Game Over
    if game_over:

        screen.blit(
            game_over_txt,
            (300, 200)
        )

        # Close game after 2 seconds
        if pygame.time.get_ticks() - game_over_time >= 2000:

            running = False

    pygame.display.update()

    # 60 FPS
    clock.tick(60)

pygame.quit()
