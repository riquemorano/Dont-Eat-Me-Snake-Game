import pygame
import food
import snake

pygame.init()

screen_x = 300
screen_y = 300
screen = pygame.display.set_mode((screen_x, screen_y))

clock = pygame.time.Clock()
endgame = False
pygame.display.set_caption('Snake Game')

count = 0

# Difficulties

zen = {'vel': (0, 2, 4, 6, 8),
       'size': 1,
       'time': 60}
easy = {'vel': (0, 1, 3, 6, 7, 9),
        'size': 3,
        'time': 30}
medium = {'vel': (0, 1, 3, 4, 6, 7, 9),
          'size': 5,
          'time': 25}
hard = {'vel': (0, 2, 3, 4, 5, 6, 7, 9),
        'size': 7,
        'time': 20}
expert = {'vel': (0, 1, 2, 3, 4, 6, 7, 8, 9),
          'size': 9,
          'time': 15}
insane = {'vel': (0, 1, 2, 3, 4, 5, 6, 7, 8, 9),
          'size': 10,
          'time': 10}

difficulty = expert
vel = difficulty['vel']
size = difficulty['size']
time = difficulty['time'] * 10

# Velocity
vel_food = 10
vel_snake = 10

# Colours
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
red = (255, 0, 0)

# Objects
food = food.Food(red, screen, screen_x, screen_y, vel_food)
snake = snake.Snake(green, screen, screen_x, screen_y, vel_snake, food)

while not endgame:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                exit()

    food.move(events, snake)
    snake.move(count, vel)
    snake.grow(count, size, time)

    if snake.check_collision():
        endgame = True

    screen.fill(black)
    food.draw()
    snake.draw()
    pygame.display.update()
    clock.tick(10)
    count += 1


pygame.quit()
quit()
