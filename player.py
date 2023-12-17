import pygame
from utils import update_assets

class Player(pygame.sprite.Sprite):
    def __init__(self,game,set,type,status,pos):
        super().__init__()
        self.game = game
        self.player_index = type
        self.player_status = status
        self.player_set = set
        self.index = 0
        self.pos = pos
        self.image = pygame.transform.rotozoom(self.game.assets['players'][int(self.index % len(self.game.assets['players']))], 0, 1.5)
        self.rect = self.image.get_rect(center = self.pos)
        self.player_name = self.game.player_names[f'{self.player_set + 1}'][self.player_index - 1]
        
    def update(self):
        update_assets(self, self.game.assets)
        if self.player_set == 5:
            self.player_set = 0
        self.player_name = self.game.player_names[f'{self.player_set + 1}'][self.player_index - 1]
        self.index += 0.1
        self.rect = self.image.get_rect(center = self.pos)
        self.game.display.blit(self.image, self.rect)
        
    def update_pos(self):
        positions = [self.width * 0.2, self.width * 0.35, self.width * 0.5, self.width * 0.65, self.width * 0.8]
        for i, player in enumerate(self.game.player_group.sprites()):
            player.pos = (positions[i], self.height / 2)
            
    def update_img(self):
        update_assets(self, self.game.assets)
        self.index += 0.1
        self.image = pygame.transform.rotozoom(self.game.assets['players'][int(self.index % len(self.game.assets['players']))], 0, 1.5) 
            