import pygame

W, H = 800, 600
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
start = 1

pygame.init()
pygame.display.set_caption('Техт')
screen = pygame.display.set_mode((W, H))
pygame.mouse.set_visible(False)

font = pygame.font.SysFont('Arial', 50, True, False)
font1 = pygame.font.SysFont('Arial', 20, True, False)
font_render = font.render('Всем привет', True, WHITE)
font_render1 = font1.render('задание на урок', True, YELLOW)
font_rect = font_render.get_rect(center=(400, 300))
font_rect1 = font_render1.get_rect(center=(W // 2, H // 2 + 50))

sq = pygame.Surface((50, 50))
sq_rect = sq.get_rect(center=(W // 2, H // 2 - 50))

bg = pygame.Surface((W, H))
bg_rect = bg.get_rect(topleft=(0, 0))

sq.fill(RED)
bg.fill(BLUE)

run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                run = False

    if start == 1:
        sq_rect.move_ip(1, 0)
        if sq_rect.x >= 700:
            start = 0
    if start == 0:
        sq_rect.move_ip(0, -1)
        if sq_rect.y <= 50:
            start = 2
    if start == 2:
        sq_rect.move_ip(-1, 0)
        if sq_rect.x <= 100:
            start = 3
    if start == 3:
        sq_rect.move_ip(0, 1)
        if sq_rect.y >= 200:
            start = 4
    if start == 4:
        sq_rect.move_ip(1, 0)
        if sq_rect.x > 700:
            start = 1
    pygame.time.wait(1)
    screen.blit(bg, bg_rect)
    screen.blit(sq, sq_rect)
    screen.blit(font_render, font_rect)
    screen.blit(font_render1, font_rect1)
    pygame.display.update()
