import pygame
import random
from car import Car

#Random rate, pos, type of the buff
# Idea # 
# Define every effect of the buff
# 1. Random type of the buff
    # Create a list of buff
    # Choose a random buff from the list
# 2. Random appear rate of the buff
    # Create a timer
    # If the timer reach the rate, then start create a buff
    # Reset the timer
# 3. Random position of the buff
    # Choose a random line to spawn the buff
    # Spawn the buff 150-200 pixel to the right of the car
    # If the buff is out of the screen, then delete it
    # If the buff is collide with the car, then delete it 
#---#
class Buff(pygame.sprite.Sprite):
    def __init__(self,game):
        super().__init__()
        self.game = game

    def update(self):
        pass
            
    def return_to_start(self):
        pass
    
    def sleep(self):
        pass
    
    def speed_up(self):
        pass
    
    def slow_down(self):
        pass
    
    def teleport(self):
        pass
    
    def teleport_to_finish_line(self):
        pass
    