import pygame
from utils import update_assets
from random import randint, uniform

class Car(pygame.sprite.Sprite):
    def __init__(self,game,set,type,status, x_pos, y_pos):
        super().__init__()
        self.game = game
        self.player_index = type
        self.player_status = status
        self.player_set = set
        self.acceleration = 0.2
        self.max_speed = 8
        self.speed = 1
        self.pos = (x_pos, y_pos)
        self.index = 0
        self.image = pygame.transform.scale(self.game.assets['cars'][int(self.index % len(self.game.assets['cars']))], (100, 50))
        self.rect = self.image.get_rect(center = self.pos)
        
    def movement(self):
        #Generate random speed
        self.acceleration = uniform(-1, 1)
        
        #Apply smoothing algorithm
        smoothing_factor = 0.05
        self.acceleration = smoothing_factor * self.acceleration + (1 - smoothing_factor) * self.acceleration
        
        #Update the speed by adding the acceleration
        self.speed += self.acceleration
        
        #Limit the speed to the maximum value
        self.speed = min(abs(self.speed), self.max_speed)
         
        #Check if the car reached the finish line
        if self.rect.x > self.game.width * 0.9:
            self.speed = 0
            
        #Update the position
        self.rect.x += abs(self.speed)
            
    def update(self):
        self.movement()
        update_assets(self, self.game.assets)
        self.image = pygame.transform.scale(self.game.assets['cars'][int(self.index % len(self.game.assets['cars']))], (100, 50))
        self.game.display.blit(pygame.transform.scale(self.image, (100,50)), self.rect)
    
    def update_pos(self, game):
        self.game = game
        if self.game.map_size == 'SMALL':
            self.car1.y_pos = (self.game.height * 0.55)
            self.car2.y_pos = (self.game.height * 0.65)
            self.car3.y_pos = (self.game.height * 0.75)
            self.car4.y_pos = (self.game.height * 0.85)
            self.car5.y_pos = (self.game.height * 0.94)
        elif self.game.map_size == 'MEDIUM':
            self.car1.y_pos = (self.game.height * 0.5)
            self.car2.y_pos = (self.game.height * 0.6)
            self.car3.y_pos = (self.game.height * 0.7)
            self.car4.y_pos = (self.game.height * 0.8)
            self.car5.y_pos = (self.game.height * 0.9)
        elif self.game.map_size == 'LARGE':
            self.car1.y_pos = (self.game.height * 0.55)
            self.car2.y_pos = (self.game.height * 0.65)
            self.car3.y_pos = (self.game.height * 0.75)
            self.car4.y_pos = (self.game.height * 0.85)
            self.car5.y_pos = (self.game.height * 0.94)
        

        
        
        