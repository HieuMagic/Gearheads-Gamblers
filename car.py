import pygame
from utils import update_assets
from random import uniform

class Car(pygame.sprite.Sprite):
    def __init__(self,game,set,type,status, pos):
        super().__init__()
        self.game = game
        self.player_index = type
        self.player_status = status
        self.player_set = set
        self.acceleration = 0.2
        self.max_speed = 12
        self.speed = 2
        self.pos = pos
        self.x_pos = self.pos[0]
        self.y_pos = self.pos[1]
        self.index = 0
        self.reached_finish_line = False
        self.rank = None
        self.triggered = False
        self.image = pygame.transform.scale(self.game.assets['cars'][int(self.index % len(self.game.assets['cars']))], (100, 50))
        self.rect = self.image.get_rect(center = self.pos)
        self.finish_fx = pygame.mixer.Sound('data/sounds/finish.wav')
        self.finish_fx.set_volume(0.5)
        self.count = 0
        self.stop = False
        
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
        if self.rect.x > self.game.finish_line_x:
            self.speed = 0
            self.rect.x = self.game.finish_line_x
        
        if self.game.race_started == False:
            self.speed = 0
        
        if self.stop and self.delay(5):
            self.speed = 0
            
        #Update the position
        self.rect.x += abs(self.speed)
            
    def update(self):
        if self.game.race_started:
            self.movement()
        update_assets(self, self.game.assets)
        if self.rect.x > self.game.finish_line_x and self.triggered == False:
            self.finish_fx.play()
            self.reached_finish_line = True
            self.triggered = True
        self.index += 0.25
        self.image = pygame.transform.scale(self.game.assets['cars'][int(self.index % len(self.game.assets['cars']))], (120, 50))
        self.game.display.blit(self.image, self.rect)
    
    def update_pos(self, game):
            self.game = game
            height_ratio = {
                'SMALL': [0.52, 0.62, 0.72, 0.82, 0.9],
                'MEDIUM': [0.47, 0.56, 0.69, 0.8, 0.9],
                'LARGE': [0.32, 0.45, 0.6, 0.74, 0.88],
                'NHO': [0.52, 0.62, 0.72, 0.82, 0.9],
                'VUA': [0.47, 0.56, 0.69, 0.8, 0.9],
                'LON': [0.32, 0.45, 0.6, 0.74, 0.88],
            }
            
            if self.game.map_size == self.get_text('Small'):
                self.game.finish_line_x = self.game.width * 0.9
            elif self.game.map_size == self.get_text('Medium'):
                self.game.finish_line_x = self.game.width * 0.9
            elif self.game.map_size == self.get_text('Large'):
                self.game.finish_line_x = self.game.width * 0.94 
                
            ratios = height_ratio.get(self.game.map_size)
            if ratios:
                for i, car in enumerate(self.game.car_group.sprites()):
                    car.rect.y = self.game.height * ratios[i]
          
    def reset(self):
        self.player_index = type
        self.player_set = set
        self.acceleration = 0.2
        self.max_speed = 7
        self.speed = 0
        self.pos = (self.x_pos, self.y_pos)
        self.index = 0
        self.reached_finish_line = False
        self.rank = None
        self.triggered = False
        self.image = pygame.transform.scale(self.game.assets['cars'][int(self.index % len(self.game.assets['cars']))], (100, 50))
        self.rect = self.image.get_rect(center = self.pos)

    def delay(self, duration):
        if self.count == None:
            self.count = 0
        self.count += 0.1
        if self.count < duration:
            return True
        else:
            self.count = 0
            self.stop = False
            return False
        