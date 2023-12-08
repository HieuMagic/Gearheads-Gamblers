import pygame
from sys import exit
from utils import load_image, load_images
from menu import *
from player import Player
from car import Car

class Game:     
    def __init__(self):
        pygame.init()
        #Sreen and surface...
        self.screen_size = [1400, 700]
        self.screen = pygame.display.set_mode((self.screen_size[0], self.screen_size[1]))
        self.width = self.screen.get_width()
        self.height = self.screen.get_height()
        self.display = pygame.Surface(((self.screen.get_width(), self.screen.get_height())))
        pygame.display.set_caption('Gearheads&Gamblers')

        #Clock, font... 
        self.clock = pygame.time.Clock()
        self.LightPixel_font = pygame.font.Font('data/font/LightPixel.ttf', 30)
        self.SoftnBig_font = pygame.font.Font('data/font/Pixeltype.ttf', 50)
        self.Arcade_font = pygame.font.Font('data/font/Arcade.ttf', 50)
        self.DIRECTION_font = pygame.font.Font('data/font/LightPixel.ttf', 100)
        
        #user's variable
        self.player_name = "ChuHieuMagic"
        self.money = 90        
        
        #Game varible
        self.player_set = 1
        self.player_index = 1
        self.player_status = 1
        #---#
        self.map_index = 1    
        self.map_size = "SMALL"  
        
        #Assets
        self.assets = {
            'loadgame' : load_image('data/graphics/interface/BACKGROUND_2.png'),
            'background' : load_image('data/graphics/background/Background4.png'),
            'players' : load_images(f'data/player/{self.player_set}/{self.player_index}/{self.player_status}/'),
            'map_preview' : load_images("data/map/preview"),
            'map' : load_image(f'data/map/{self.map_index}/{self.map_size}.png'),
            'cars' : load_images(f'data/graphics/car/{self.player_set}/{self.player_index}'),
        }
        
        #Game control variable
        self.game_running = True
        self.game_state = 1 
        self.main_menu_state = 1
        self.size_state = 0
        self.credits_state = 0
        self.minigame_state = 0
        
        self.player_state = 0
        self.map_state = 0
        self.button_pressed = False
        self.text_state = 0

        #Player 
        # (Set, Type, Status) #
        self.player1 = Player(self,self.player_set,1,self.player_status,(self.width * 0.2, self.height / 2))
        self.player2 = Player(self,self.player_set,2,self.player_status,(self.width * 0.35, self.height / 2))
        self.player3 = Player(self,self.player_set,3,self.player_status,(self.width * 0.5, self.height / 2))
        self.player4 = Player(self,self.player_set,4,self.player_status,(self.width * 0.65, self.height / 2))
        self.player5 = Player(self,self.player_set,5,self.player_status,(self.width * 0.8, self.height / 2))
        self.player = Player(self,self.player_set,3,self.player_status,(self.width * 0.5, self.height / 2))
            
        #Car
        # (Set, Type, Status) #
        self.car1 = Car(self,self.player.player_set,1,self.player.player_status,100, self.height * 0.55)
        self.car2 = Car(self,self.player.player_set,2,self.player.player_status,100, self.height * 0.65)
        self.car3 = Car(self,self.player.player_set,3,self.player.player_status,100, self.height * 0.75)
        self.car4 = Car(self,self.player.player_set,4,self.player.player_status,100, self.height * 0.85)
        self.car5 = Car(self,self.player.player_set,5,self.player.player_status,100, self.height * 0.94)
        
    def run(self):
        while self.game_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        exit()
                
            #Update variable
            self.width = self.screen.get_width()
            self.height = self.screen.get_height()
            self.mouse_pos = pygame.mouse.get_pos()
            self.display = pygame.Surface(((self.width, self.height)))
            
            #State 1
            if self.game_state == 1:
                button_animation(self)
                self.display.blit(pygame.transform.scale(self.assets['loadgame'], (self.width, self.height)), (0, 0))
                self.startgame_surface = self.LightPixel_font.render(self.startgame_text, 0, (111, 196, 169))
                self.startgame_rect = self.startgame_surface.get_rect(center = (self.display.get_width() / 2, self.display.get_height() * 0.875))
                self.display.blit(self.startgame_surface, self.startgame_rect)
                if pygame.key.get_pressed()[pygame.K_SPACE]:
                    self.game_state = 2
            
            #State 2
            elif self.game_state == 2:
                if self.main_menu_state == 1:
                    main_menu(self, self)
                if self.credits_state == 1:
                    credits_menu(self)
                if self.minigame_state == 1:
                    minigame_menu(self, self)
                                
            #State 3
            elif self.game_state == 3:
                Player.update_pos(self)
                choose_player_set_menu(self)
                
            #State 4
            elif self.game_state == 4:
                choose_player_menu(self)
                
            #State 5
            elif self.game_state == 5:
                Car.update_pos(self, self)
                game_play(self)
                
            #Scale n update
            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0,0))        
            pygame.display.update()           
            self.clock.tick(60)
            
Game().run()