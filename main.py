import pygame
import food
import snake

pygame.init()

screen_x = 800
screen_y = 800
endgame = False
vel_food = 10
vel_snake = 4

screen = pygame.display.set_mode((screen_x, screen_y))
clock = pygame.time.Clock()

# Colours
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
red = (255, 0, 0)

food = food.Food(red, screen, screen_x, screen_y, vel_food)
snake = snake.Snake(green, screen, screen_x, screen_y, vel_snake, food)

pygame.display.set_caption('Snake Game')

while not endgame:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                exit()
    food.move(events)
    snake.move()
    screen.fill(black)
    food.draws()
    snake.draws()
    pygame.display.update()
    clock.tick(30)
    if snake.check_collision():
        endgame = True
    vel_snake *= 1.00004


pygame.quit()
quit()
