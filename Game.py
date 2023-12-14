import pygame
from sys import exit
from utils import load_image, load_images
from menu import main_menu, choose_player_set_menu, choose_player_menu, credits_menu, minigame_menu, game_play, button_animation, leaderboard
from player import Player
from car import Car
from buff import Buff

class Game:     
    def __init__(self):
        pygame.init()
        #Sreen and surface...
        self.screen_size = [1400, 700]
        self.screen = pygame.display.set_mode((self.screen_size[0], self.screen_size[1]))
        self.width = self.screen.get_width()
        self.height = self.screen.get_height()
        self.display = pygame.Surface(((self.screen.get_width(), self.screen.get_height())))
        self.cursor_point = pygame.transform.scale2x(pygame.image.load('data/cursor/cursor_point.png'))
        self.cursor_click = pygame.transform.scale2x(pygame.image.load('data/cursor/cursor_click.png'))
        pygame.display.set_caption('Gearheads&Gamblers')

        #Clock, font... 
        self.clock = pygame.time.Clock()
        self.LightPixel_font = pygame.font.Font('data/font/LightPixel.ttf', 30)
        self.SmallerLightPixel_font = pygame.font.Font('data/font/LightPixel.ttf', 20)
        self.BiggerLightPixel_font = pygame.font.Font('data/font/LightPixel.ttf', 40)
        self.SoftnBig_font = pygame.font.Font('data/font/Pixeltype.ttf', 50)
        self.Arcade_font = pygame.font.Font('data/font/Arcade.ttf', 60)
        self.DIRECTION_font = pygame.font.Font('data/font/LightPixel.ttf', 100)
        
        #User's variable
        self.player_name = "ChuHieuMagic"
        self.money = 999      
        self.bet = 200
        
        #Game variable
        self.player_set = 1
        self.player_index = 1
        self.player_status = 1
        self.race_started = False
        
        #Map variable
        self.map_index = 1
        self.map_size = "SMALL"
        
        #Assets
        self.assets = {
            'loadgame' : load_image('data/graphics/interface/BACKGROUND_2.png'),
            'background' : load_image('data/graphics/background/background.png'),
            'players' : load_images(f'data/player/{self.player_set}/{self.player_index}/{self.player_status}/'),
            'map_preview' : load_images("data/map/preview"),
            'map' : load_image(f'data/map/{self.map_index}/{self.map_size}.png'),
            'cars' : load_images(f'data/graphics/car/{self.player_set}/{self.player_index}'),
            'buffs' : load_images('data/magic')
        }
        
        #Image
        self.button_image = pygame.image.load('data/small.png')
        self.dialogue_image = pygame.image.load('data/dialogue.png')
        self.long_button_image = pygame.image.load('data/long.png')
        
        #Game control variable
        self.game_running = True
        self.game_state = 2
        self.main_menu_state = 1
        self.size_state = 0
        self.credits_state = 0
        self.minigame_state = 0
        
        self.player_state = 0
        self.map_state = 0
        self.button_pressed = False
        self.text_state = 0
        self.finish_line_x = self.width * 0.9
        self.rank = 0

        #Player 
        # (Set, Type, Status) #
        self.player_group = pygame.sprite.Group()
        self.player1 = self.player_group.add(Player(self,self.player_set,1,self.player_status,(self.width * 0.2, self.height / 2)))
        self.player2 = self.player_group.add(Player(self,self.player_set,2,self.player_status,(self.width * 0.35, self.height / 2)))
        self.player3 = self.player_group.add(Player(self,self.player_set,3,self.player_status,(self.width * 0.5, self.height / 2)))
        self.player4 = self.player_group.add(Player(self,self.player_set,4,self.player_status,(self.width * 0.65, self.height / 2)))
        self.player5 = self.player_group.add(Player(self,self.player_set,5,self.player_status,(self.width * 0.8, self.height / 2)))
        self.player =  Player(self,self.player_set,self.player_index,self.player_status,(self.width * 0.3, self.height / 2))
        
        #Car
        # (Set, Type, Status) #
        self.car_group = pygame.sprite.Group()
        self.car1 = self.car_group.add(Car(self,self.player_set,1,self.player_status,100, self.height * 0.55))
        self.car2 = self.car_group.add(Car(self,self.player_set,2,self.player_status,100, self.height * 0.65))
        self.car3 = self.car_group.add(Car(self,self.player_set,3,self.player_status,100, self.height * 0.75))
        self.car4 = self.car_group.add(Car(self,self.player_set,4,self.player_status,100, self.height * 0.85))
        self.car5 = self.car_group.add(Car(self,self.player_set,5,self.player_status,100, self.height * 0.94))
        self.car = Car(self,self.player_set,self.player_index,self.player_status,self.width * 0.6, self.height / 2)

        #Timer
        self.buff_group = pygame.sprite.Group()
        self.buff_timer = pygame.USEREVENT + 1
        pygame.time.set_timer(self.buff_timer, 2000)
        self.start_time = 0
        
    def current(self):
        self.current_time = pygame.time.get_ticks() - self.start_time
        return self.current_time
            
    def run(self):
        while self.game_running:
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
                self.start_time = pygame.time.get_ticks()
                
            #State 5
            elif self.game_state == 5:
                Car.update_pos(self, self)
                game_play(self)
                
                for event in pygame.event.get():
                    if event.type == self.buff_timer and self.race_started:
                        self.buff_group.add(Buff(self))
                self.buff_group.update()
                
                if self.current() < 3000:
                    self.count_down_text = self.BiggerLightPixel_font.render(str(3 - int(self.current() / 1000)), 0, (111, 196, 169))
                    self.count_down_rect = self.count_down_text.get_rect(center = (self.display.get_width() / 2, self.display.get_height() / 2))
                    self.display.blit(self.count_down_text, self.count_down_rect)
                elif self.current() >= 3000 and self.current() < 4000:
                    self.count_down_text = self.BiggerLightPixel_font.render("GO!", 0, (111, 196, 169))
                    self.count_down_rect = self.count_down_text.get_rect(center = (self.display.get_width() / 2, self.display.get_height() / 2))
                    self.display.blit(self.count_down_text, self.count_down_rect)
                if self.current() >= 3000:
                    self.game.race_started = True
                    
            #State 6
            elif self.game_state == 6:
                leaderboard(self)
                
            #Mouse cursor
            pygame.mouse.set_visible(False)
            if pygame.mouse.get_pressed()[0]:
                self.display.blit(self.cursor_click, (self.mouse_pos[0] - 10, self.mouse_pos[1] - 10))
            else:
                self.display.blit(self.cursor_point, (self.mouse_pos[0] - 10, self.mouse_pos[1] - 10))
            
            #Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        exit()            
                        
            #Update screen
            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0,0))        
            pygame.display.update()           
            self.clock.tick(60)
            
Game().run()