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
        self.image = pygame.transform.scale(self.game.assets['cars'][int(self.index % len(self.game.assets['cars']))], (120, 50))
        self.game.display.blit(pygame.transform.scale(self.image, (100,50)), self.rect)
    
    def update_pos(self, game):
            self.game = game
            height_ratio = {
                'SMALL': [0.52, 0.62, 0.72, 0.82, 0.9],
                'MEDIUM': [0.47, 0.56, 0.69, 0.8, 0.9],
                'LARGE': [0.32, 0.45, 0.6, 0.74, 0.88]
            }
            ratios = height_ratio.get(self.game.map_size)
            if ratios:
                for i, car in enumerate([self.car1, self.car2, self.car3, self.car4, self.car5]):
                    car.rect.y = self.game.height * ratios[i]
        

        
        
        