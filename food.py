import pygame


class Food:
    def __init__(self, color, screen, x, y, vel):
        self.color = color
        self.x = x/2 + 40
        self.y = y/2 + 40
        self.vel_x = 0
        self.vel_y = 0
        self.vel = vel
        self.screen = screen
        self.screen_x = screen.get_width()
        self.screen_y = screen.get_height()

    def move(self, events, snake):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.vel_x = -self.vel
                    self.vel_y = 0
                elif event.key == pygame.K_RIGHT:
                    self.vel_x = self.vel
                    self.vel_y = 0
                elif event.key == pygame.K_UP:
                    self.vel_x = 0
                    self.vel_y = -self.vel
                elif event.key == pygame.K_DOWN:
                    self.vel_x = 0
                    self.vel_y = self.vel

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    self.vel_x = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    self.vel_y = 0
                    
            
        if self.x + self.vel_x >= 0 and self.x + self.vel_x < self.screen_x:
            self.x += self.vel_x

        if self.y + self.vel_y >= 0 and self.y + self.vel_y < self.screen_y:
            self.y += self.vel_y

        for snake.x, snake.y in snake.body:
            if self.x == snake.x and self.y == snake.y:
                self.x = self.x - self.vel_x
                self.y = self.y - self.vel_y

    def draw(self):
        pygame.draw.rect(self.screen, self.color, [self.x, self.y, 10, 10])