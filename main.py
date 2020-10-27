import pygame

W, H = 800, 600
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

pygame.init()
pygame.display.set_caption('Техт')
screen = pygame.display.set_mode((W, H))
pygame.mouse.set_visible(False)

font = pygame.font.SysFont('Arial', 50, True, False)
font1 = pygame.font.SysFont('Arial', 20, True, False)
font_render = font.render('Всем привет', True, WHITE)
font_render1 = font1.render('задание на урок', True, YELLOW)
font_rect = font_render.get_rect(center=(400, 300))
font_rect1 = font_render1.get_rect(center=(W // 2, H // 2 + 30))

sq = pygame.Surface((50, 50))
sq_rect = sq.get_rect(center=(W // 2, H // 2 - 50))

bg = pygame.Surface((W, H))
bg_rect = bg.get_rect(topleft=(0, 0))

run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
        elif e.type == pygame.K_ESCAPE:
            run = False
    screen.blit(bg, bg_rect)
    screen.blit(sq, sq_rect)
    screen.blit(font_render, font_rect)
    screen.blit(font_render1, font_rect1)
    sq.fill(RED)
    bg.fill(BLUE)
    pygame.display.update()
