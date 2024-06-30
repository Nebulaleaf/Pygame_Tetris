# main.py
import pygame, sys
from game import Game
from colors import Colors

pygame.init()

title_font = pygame.font.Font(None, 40)
score_surface = title_font.render("Score", True, Colors.black)
next_surface = title_font.render("Next", True, Colors.black)
rows_surface = title_font.render("Rows", True, Colors.black)
game_over_surface = pygame.font.Font(None, 40).render("GAME OVER", True, Colors.white)

# Rectangles for the score, next block, and rows cleared displays
score_rect = pygame.Rect(320, 55, 170, 60)
next_rect = pygame.Rect(320, 190, 170, 90)
rows_rect = pygame.Rect(320, 360, 170, 60)

screen = pygame.display.set_mode((500, 620))
pygame.display.set_caption("Python Tetris")

clock = pygame.time.Clock()

game = Game()

GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 200)

# Variables to control continuous movement
move_left_timer = 0
move_right_timer = 0
move_down_timer = 0
key_press_interval = 100  # Interval in milliseconds

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if game.game_over:
                game.game_over = False
                game.reset()
            if event.key == pygame.K_LEFT and not game.game_over:
                game.move_left()
                move_left_timer = pygame.time.get_ticks()
            if event.key == pygame.K_RIGHT and not game.game_over:
                game.move_right()
                move_right_timer = pygame.time.get_ticks()
            if event.key == pygame.K_DOWN and not game.game_over:
                game.move_down()
                move_down_timer = pygame.time.get_ticks()
            if event.key == pygame.K_UP and not game.game_over:
                game.rotate()
        if event.type == GAME_UPDATE and not game.game_over:
            game.move_down()

    # Check for continuous movement
    keys = pygame.key.get_pressed()
    current_time = pygame.time.get_ticks()

    if keys[pygame.K_LEFT] and current_time - move_left_timer > key_press_interval:
        game.move_left()
        move_left_timer = current_time

    if keys[pygame.K_RIGHT] and current_time - move_right_timer > key_press_interval:
        game.move_right()
        move_right_timer = current_time

    if keys[pygame.K_DOWN] and current_time - move_down_timer > key_press_interval:
        game.move_down()
        move_down_timer = current_time

    # Drawing
    score_value_surface = title_font.render(str(game.score), True, Colors.white)
    rows_value_surface = title_font.render(str(game.rows_cleared), True, Colors.white)

    screen.fill(Colors.dark_grey)
    screen.blit(score_surface, (365, 20))
    screen.blit(next_surface, (365, 155))
    screen.blit(rows_surface, (365, 330))

    if game.game_over:
        screen.blit(game_over_surface, (320, 500))

    pygame.draw.rect(screen, Colors.grey, score_rect, 0, 10)
    screen.blit(score_value_surface, score_value_surface.get_rect(centerx=score_rect.centerx,
        centery=score_rect.centery))
    pygame.draw.rect(screen, Colors.grey, next_rect, 0, 10)
    pygame.draw.rect(screen, Colors.grey, rows_rect, 0, 10)
    screen.blit(rows_value_surface, rows_value_surface.get_rect(centerx=rows_rect.centerx,
        centery=rows_rect.centery))

    game.draw(screen)

    pygame.display.update()
    clock.tick(60)
