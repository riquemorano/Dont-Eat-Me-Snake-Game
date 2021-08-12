import pygame


class Snake:
    def __init__(self, color, screen, x, y, vel, food):
        self.color = color
        self.x = x/2 - 50
        self.y = y/2 - 50
        self.vel_x = 0
        self.vel_y = 0
        self.vel = vel
        self.screen = screen
        self.screen_x = screen.get_width()
        self.screen_y = screen.get_height()
        self.food = food

    def move(self):
        self.x_diff = self.x - self.food.x
        self.y_diff = self.y - self.food.y
        if abs(self.y_diff) >= abs(self.x_diff):
            if self.y_diff < 0:
                self.vel_x = 0
                self.vel_y = self.vel
            else:
                self.vel_x = 0
                self.vel_y = -self.vel

        elif(abs(self.y_diff) <= abs(self.x_diff)):
            if self.x_diff > 0:
                self.vel_x = -self.vel
                self.vel_y = 0
            else:
                self.vel_x = self.vel
                self.vel_y = 0

        pygame.display.update()

        if self.x + self.vel_x >= 0 and self.x + self.vel_x < self.screen_x:
            self.x += self.vel_x

        if self.y + self.vel_y >= 0 and self.y + self.vel_y < self.screen_y:
            self.y += self.vel_y

    def draws(self):
        pygame.draw.rect(self.screen, self.color, [self.x, self.y, 10, 10])

    def check_collision(self):
        if abs(round(self.x_diff)) <= 2 and abs(round(self.y_diff)) <= 2:
            return True
        else:
            return False
