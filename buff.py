import pygame 
from random import randint, choice

class Buff(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.stop_duration = 5000
        
        #randomly choose a buff
        self.type = choice(['speed_up', 'return', 'stop', 'teleport','win','sleep'])
        if self.type == 'speed_up':
            self.image = (pygame.image.load('data/magic/speed_up.png'))
        elif self.type == 'return':
            self.image = (pygame.image.load('data/magic/return.png'))
        elif self.type == 'stop':
            self.image = (pygame.image.load('data/magic/stop.png'))
        elif self.type == 'win':
            self.image = (pygame.image.load('data/magic/win.png'))
        elif self.type == 'sleep':
            self.image = (pygame.image.load('data/magic/sleep.png'))
        elif self.type == 'teleport':
            self.image = (pygame.image.load('data/magic/teleport.png'))
            
        #randomly choose a car and create a buff 200 pixel to the right of the car
        cars_not_reached_finish = [car for car in self.game.car_group.sprites() if not car.triggered]
        if cars_not_reached_finish != []:
            self.chosen_car = choice(cars_not_reached_finish)
            self.pos = (self.chosen_car.rect.x + 200, self.chosen_car.rect.y + 20)
            self.rect = self.image.get_rect(center = self.pos)
        else:
            self.chosen_car = None

    
    def update(self):
        if self.chosen_car != None:
            self.game.display.blit(self.image, self.rect)
        #check if the buff is picked up
            if pygame.sprite.spritecollide(self, self.game.car_group, False):
                self.apply_buff()
                self.kill()

    def apply_buff(self):
        if self.type == 'speed_up':
            self.chosen_car.speed += 20
        elif self.type == 'return':
            self.chosen_car.rect.x = 100
        elif self.type == 'stop':
            if self.stop_duration:
                self.chosen_car.speed = -1
                self.stop_duration -= 100
        elif self.type == 'win':
            self.chosen_car.rect.x = self.game.finish_line_x * 0.95
        elif self.type == 'sleep':
            if self.stop_duration:
                self.chosen_car.speed = -1
                self.stop_duration -= 100
            self.chosen_car.rect.x -= 200
        elif self.type == 'teleport':
            self.chosen_car.rect.x += 200
    
        
        
        