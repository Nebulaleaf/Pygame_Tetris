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

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if game.game_over == True:
                game.game_over = False
                game.reset()
            if event.key == pygame.K_LEFT and game.game_over == False:
                game.move_left()
            if event.key == pygame.K_RIGHT and game.game_over == False:
                game.move_right()
            if event.key == pygame.K_DOWN and game.game_over == False:
                game.move_down()
            if event.key == pygame.K_UP and game.game_over == False:
                game.rotate()
        if event.type == GAME_UPDATE and game.game_over == False:
            game.move_down()

    # Drawing
    score_value_surface = title_font.render(str(game.score), True, Colors.white)
    rows_value_surface = title_font.render(str(game.rows_cleared), True, Colors.white)

    screen.fill(Colors.dark_grey)
    screen.blit(score_surface, (365, 20))
    screen.blit(next_surface, (365, 155))
    screen.blit(rows_surface, (365, 330))

    if game.game_over == True:
        screen.blit(game_over_surface, (320, 500))

    pygame.draw.rect(screen, Colors.grey, score_rect, 0, 10)  # Change rectangle color to grey
    screen.blit(score_value_surface, score_value_surface.get_rect(centerx=score_rect.centerx,
        centery=score_rect.centery))
    pygame.draw.rect(screen, Colors.grey, next_rect, 0, 10)  # Change rectangle color to grey
    pygame.draw.rect(screen, Colors.grey, rows_rect, 0, 10)  # Change rectangle color to grey
    screen.blit(rows_value_surface, rows_value_surface.get_rect(centerx=rows_rect.centerx,
        centery=rows_rect.centery))

    game.draw(screen)

    pygame.display.update()
    clock.tick(60)
