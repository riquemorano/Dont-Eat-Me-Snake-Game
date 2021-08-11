import pygame

pygame.init()
screen_x = 400
screen_y = 300
screen = pygame.display.set_mode((screen_x, screen_y))
clock = pygame.time.Clock()

endgame = False

#Colours
white = (255,255,255)
black = (0,0,0)
blue = (0,0,255)
green = (0,255,0)
red = (255,0,0)

food_x = screen_x/2
food_y = screen_y/2

vel_x = 0
vel_y = 0

pygame.display.set_caption('Snake Game')

while not endgame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            endgame = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                vel_x = -10
                vel_y = 0
            elif event.key == pygame.K_RIGHT:
                vel_x = 10
                vel_y = 0
            elif event.key == pygame.K_UP:
                vel_x = 0
                vel_y = -10
            elif event.key == pygame.K_DOWN:
                vel_x = 0
                vel_y = 10
            elif event.key == pygame.K_ESCAPE:
                endgame = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                vel_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                vel_y = 0
        if food_x <= 0:
            food_x = 0
        if food_x >= screen_x:
            food_x = screen_x - 10
        if food_y <= 0:
            food_y = 0
        if food_y >= screen_y:
            food_y = screen_y - 10
            
        pygame.display.update()
        #print(event)
    food_x += vel_x
    food_y += vel_y
    screen.fill(black)
    pygame.draw.rect(screen, red,[food_x,food_y,10,10]) #Food
    pygame.display.update()

    clock.tick(30)

pygame.quit()
quit()