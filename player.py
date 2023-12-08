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
        self.image = self.game.assets['players'][int(self.index % len(self.game.assets['players']))]
        self.rect = self.image.get_rect(center = self.pos)
        
    def update(self):
        update_assets(self, self.game.assets)
        self.index += 0.1
        self.image = self.game.assets['players'][int(self.index % len(self.game.assets['players']))]
        self.rect = self.image.get_rect(center = self.pos)
        self.game.display.blit(self.image, self.rect)
        
    def update_pos(self):
        positions = [self.width * 0.2, self.width * 0.35, self.width * 0.5, self.width * 0.65, self.width * 0.8]
        for i, player in enumerate([self.player1, self.player2, self.player3, self.player4, self.player5]):
            player.pos = (positions[i], self.height / 2)

            