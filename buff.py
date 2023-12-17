import pygame 
from random import randint, choice
from utils import load_images

class Buff(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.stop_duration = 5000
        self.click_fx = pygame.mixer.Sound('data/sounds/click.wav')
        self.click_fx.set_volume(0.5)
        self.index = 0
        
        #randomly choose a buff
        self.buff_type = choice(['backward','return','forward', 'speed','win','stop'])
        self.assets = load_images(f'data/magic/{self.buff_type}')
        self.image = self.assets[self.index]
        #randomly choose a car and create a buff 200 pixel to the right of the car
        cars = [car for car in self.game.car_group.sprites()]
        self.chosen_car = choice(cars)
        self.pos = (self.chosen_car.rect.right + 150, self.chosen_car.rect.y + 20)
        self.rect = self.image.get_rect(center = self.pos)

    def update(self):
        self.index += 0.25
        if self.index >= len(self.assets):
            self.index = 1
        self.image = self.assets[int(self.index)]
        if self.chosen_car != None:
            self.game.display.blit(self.image, self.rect)
            #check if the buff is picked up
            if pygame.sprite.spritecollide(self, self.game.car_group, False):
                self.apply_buff()
                self.kill()
            #check if the buff is out of the screen or the buff is behind the car
            if self.rect.x < self.chosen_car.rect.x or self.rect.x >= self.game.finish_line_x:
                self.kill()

    def apply_buff(self):
        self.click_fx.play()
        if self.buff_type == 'speed':
            self.chosen_car.speed += 10
        elif self.buff_type == 'return':
            self.chosen_car.rect.x = 100
        elif self.buff_type == 'stop':
            self.chosen_car.stop = True
        elif self.buff_type == 'win':
            self.chosen_car.rect.x = self.game.finish_line_x * 0.98
        elif self.buff_type == 'backward':
            self.chosen_car.speed = 0
            self.chosen_car.rect.x -= 200
        elif self.buff_type == 'forward':
            self.chosen_car.rect.x += 200
            
    
        
        
        