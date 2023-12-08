import pygame
from button import Button, AnimatedButton
from utils import get_text_size, get_image_size, update_assets, count_child_folders
from car import Car

# Menu
def main_menu(self, game):
    #Background
    self.game = game
    self.display.blit(pygame.transform.scale(self.assets['background'], (self.width, self.height)), (0,0))
    
    #Variable
    self.mouse_pos = pygame.mouse.get_pos()
    self.base_color = "BLACK"
    self.hovering_color = "#e2446c"

    #Game name
    self.game_name = self.Arcade_font.render("Gearheads&Gamblers", False, self.base_color)
    self.game_name_rect = self.game_name.get_rect(center = (self.width / 2, self.height * 0.1))
    self.display.blit(self.game_name, self.game_name_rect)
    
    #Choose map and load button
    button_load(self)
    if self.RIGHTBUTTON.checkForInput(self.mouse_pos):
        choose_map_right(self)
    if self.LEFTBUTTON.checkForInput(self.mouse_pos):
        choose_map_left(self)
    if self.MAP_SIZE.checkForInput(self.mouse_pos):
        choose_map_size(self, self.game)
    map_load(self)
    check_button_pressed(self)
     
def credits_menu(self):
    #Background
    self.display.blit(pygame.transform.scale(self.assets['background'], (self.width, self.height)), (0,0))
    
    #Text
    self.line_1 = self.LightPixel_font.render("PROJECT END-TERM", False, "YELLOW")
    self.line_2_1 = self.LightPixel_font.render("PROJECT MANAGER:", False, "WHITE")
    self.line_2_2 = self.LightPixel_font.render("NGUYEN QUANG DUY", False, "RED")
    self.line_3_1 = self.LightPixel_font.render("BUSINESS ANALYST:", False, "WHITE")
    self.line_3_2 = self.LightPixel_font.render("VAN DINH HIEU", False, "RED")
    self.line_4 = self.LightPixel_font.render("DEVELOPER:", False, "WHITE")
    self.line_5 = self.LightPixel_font.render("NGUYEN QUANG HUY", False, "RED")
    self.line_6 = self.LightPixel_font.render("VAN DINH HIEU", False, "RED")
    self.line_7 = self.LightPixel_font.render("LUU TRONG HIEU", False, "RED")
    self.line_8 = self.LightPixel_font.render("TRAN DAI HIEP", False, "RED")
    self.line_9 = self.LightPixel_font.render("NGUYEN MANH HIEN", False, "RED")
    
    #Create text rect
    self.line_1_rect = self.line_1.get_rect(center = (self.width/2, self.height*0.1))
    self.line_2_1_rect = self.line_2_1.get_rect(center = ((self.width/2 - get_text_size(self,"PROJECT MANAGER:")[0] * 0.55), self.height*0.2))
    self.line_2_2_rect = self.line_2_2.get_rect(center = ((self.width/2 + get_text_size(self,"NGUYEN QUANG DUY")[0] * 0.55), self.height*0.2))
    self.line_3_1_rect = self.line_3_1.get_rect(center = ((self.width/2 - get_text_size(self,"BUSINESS ANALYST:")[0] * 0.55), self.height*0.3))
    self.line_3_2_rect = self.line_3_2.get_rect(center = ((self.width/2 + get_text_size(self,"VAN DINH HIEU")[0] * 0.55), self.height*0.3))
    self.line_4_rect = self.line_4.get_rect(center = (self.width/2, self.height*0.4))
    self.line_5_rect = self.line_5.get_rect(center = (self.width/2, self.height*0.5))
    self.line_6_rect = self.line_6.get_rect(center = (self.width/2, self.height*0.6))
    self.line_7_rect = self.line_7.get_rect(center = (self.width/2, self.height*0.7))
    self.line_8_rect = self.line_8.get_rect(center = (self.width/2, self.height*0.8))
    self.line_9_rect = self.line_9.get_rect(center = (self.width/2, self.height*0.9))
    
    #Display rect
    self.display.blit(self.line_1, self.line_1_rect)
    self.display.blit(self.line_2_1, self.line_2_1_rect)
    self.display.blit(self.line_2_2, self.line_2_2_rect)
    self.display.blit(self.line_3_1, self.line_3_1_rect)
    self.display.blit(self.line_3_2, self.line_3_2_rect)
    self.display.blit(self.line_4, self.line_4_rect)
    self.display.blit(self.line_5, self.line_5_rect)
    self.display.blit(self.line_6, self.line_6_rect)
    self.display.blit(self.line_7, self.line_7_rect)
    self.display.blit(self.line_8, self.line_8_rect)
    self.display.blit(self.line_9, self.line_9_rect)
    
    self.RETURNBUTTON = Button(image = None, pos = (self.width * 0.15, self.height * 0.9), text_input = "<Return>",
                               font = self.LightPixel_font, base_color = self.base_color, hovering_color = self.hovering_color)

    for button in [self.RETURNBUTTON]:
        button.changeColor(self.mouse_pos)
        button.update(self.display)
        
    if self.RETURNBUTTON.checkForInput(self.mouse_pos):
        if pygame.mouse.get_pressed()[0] == 1 and self.credits_state == 1:
            self.credits_state = 0
            self.main_menu_state = 1

def minigame_menu(self, game):
    self.game = game
    #background
    self.display.blit(pygame.transform.scale(self.assets['background'], (self.width, self.height)), (0,0))

    #Text
    self.limit_text = self.LightPixel_font.render("! LIMIT FOR MINIGAME: 100 !", False, self.base_color)
    self.limit_text_rect = self.limit_text.get_rect(center = (self.width / 2, self.height * 0.1))
    
    #Variable
    self.mouse_pos = pygame.mouse.get_pos()
    self.base_color = "BLACK"
    self.hovering_color = "#e2446c"
    
    #Create button
    if self.game.money < 100:
        self.money_text = "+1"
    else:
        self.money_text = "+0"
    self.button1 = AnimatedButton(self,self.money_text,200,200,(self.width / 2 - 100, self.height / 2 - 100),5)
    
    #Update
    self.button1.draw()
    self.display.blit(self.limit_text, self.limit_text_rect)
    
    #Button
    self.MONEY = Button(image = None, pos = ((self.width * 0.05 + get_text_size(self, f"MONEY {self.money}")[0] * 0.55), self.height * 0.5), text_input = f"MONEY {self.money}",
                        font = self.LightPixel_font, base_color = self.hovering_color, hovering_color = self.hovering_color)
    self.RETURNBUTTON = Button(image = None, pos = (self.width * 0.15, self.height * 0.9), text_input = "<Return>",
                               font = self.LightPixel_font, base_color = self.base_color, hovering_color = self.hovering_color)
    
    #Button update
    for button in [self.RETURNBUTTON, self.MONEY]:
        button.changeColor(self.mouse_pos)
        button.update(self.display)
    
    #Check if return button is pressed
    if self.RETURNBUTTON.checkForInput(self.mouse_pos):
        if pygame.mouse.get_pressed()[0] == 1 and self.minigame_state == 1:
            self.minigame_state = 0
            self.main_menu_state = 1

def choose_player_set_menu(self):
    #Background
    button_animation(self)
    self.display.blit(pygame.transform.scale(self.assets['background'], (self.width, self.height)), (0,0))
    self.text_surf = self.LightPixel_font.render(self.choose_player_set_text, False, self.base_color)
    self.text_rect = self.text_surf.get_rect(center = (self.width / 2, self.height * 0.1))
    self.display.blit(self.text_surf, self.text_rect)
    
    self.NEXT_BUTTON = Button(image = None, pos = (self.width * 0.9, self.height * 0.9), text_input = "NEXT>",
                              font = self.LightPixel_font, base_color = self.base_color, hovering_color = self.hovering_color)
    self.PREV_BUTTON = Button(image = None, pos = (self.width * 0.1, self.height * 0.9), text_input = "<PREV",
                              font = self.LightPixel_font, base_color = self.base_color, hovering_color = self.hovering_color)
    self.CONFIRM_BUTTON = Button(image = None, pos = (self.width * 0.5, self.height * 0.9), text_input = self.confirm_text,
                               font = self.LightPixel_font, base_color = self.base_color, hovering_color = self.hovering_color)
    self.BACK_BUTTON = Button(image = None, pos = (self.width * 0.05, self.height * 0.05), text_input = "<BACK>",
                              font = self.LightPixel_font, base_color = self.base_color, hovering_color = self.hovering_color)
    for button in [self.NEXT_BUTTON, self.PREV_BUTTON, self.CONFIRM_BUTTON, self.BACK_BUTTON]:
        button.changeColor(self.mouse_pos)
        button.update(self.display)
    
    if self.BACK_BUTTON.checkForInput(self.mouse_pos) and pygame.mouse.get_pressed()[0] == 1:
        self.game_state = 2

    if self.NEXT_BUTTON.checkForInput(self.mouse_pos):
        if pygame.mouse.get_pressed()[0] == 1:
            self.button_pressed = True
        elif pygame.mouse.get_pressed()[0] == 0 and self.button_pressed == True:
            self.player_set += 1
            if self.player_set == 6:
                self.player_set = 1
            self.button_pressed = False
    
    if self.PREV_BUTTON.checkForInput(self.mouse_pos):
        if pygame.mouse.get_pressed()[0] == 1:
            self.button_pressed = True
        elif pygame.mouse.get_pressed()[0] == 0 and self.button_pressed == True:
            self.player_set -= 1
            if self.player_set == 0:
                self.player_set = 5
            self.button_pressed = False

    # if self.CONFIRM_BUTTON.checkForInput(self.mouse_pos) and pygame.mouse.get_pressed()[0] == 1:
    #     self.game_state = 4
    
    for player in [self.player1, self.player2, self.player3, self.player4, self.player5]:
        player.player_set = self.player_set
        player.update()
    
    self.temp = 0
    
    if self.CONFIRM_BUTTON.checkForInput(self.mouse_pos):
        if pygame.mouse.get_pressed()[0] == 1:
            self.button_pressed = True
        elif pygame.mouse.get_pressed()[0] == 0:
            if self.button_pressed == True:
                self.game_state = 4
                self.button_pressed = False 
            
def choose_player_menu(self):
    #Background
    button_animation(self)
    self.display.blit(pygame.transform.scale(self.assets['background'], (self.width, self.height)), (0,0))
    self.text_surf = self.LightPixel_font.render(self.choose_player_text, False, self.base_color)
    self.text_rect = self.text_surf.get_rect(center = (self.width / 2, self.height * 0.1))
    self.display.blit(self.text_surf, self.text_rect)
    
    self.NEXT_BUTTON = Button(image = None, pos = (self.width * 0.9, self.height * 0.9), text_input = "NEXT>",
                              font = self.LightPixel_font, base_color = self.base_color, hovering_color = self.hovering_color)
    self.PREV_BUTTON = Button(image = None, pos = (self.width * 0.1, self.height * 0.9), text_input = "<PREV",
                              font = self.LightPixel_font, base_color = self.base_color, hovering_color = self.hovering_color)
    self.CONFIRM_BUTTON = Button(image = None, pos = (self.width * 0.5, self.height * 0.9), text_input = self.confirm_text,
                               font = self.LightPixel_font, base_color = self.base_color, hovering_color = self.hovering_color)
    self.BACK_BUTTON = Button(image = None, pos = (self.width * 0.05, self.height * 0.05), text_input = "<BACK>",
                              font = self.LightPixel_font, base_color = self.base_color, hovering_color = self.hovering_color)
    
    for button in [self.NEXT_BUTTON, self.PREV_BUTTON, self.CONFIRM_BUTTON, self.BACK_BUTTON]:
        button.changeColor(self.mouse_pos)
        button.update(self.display)
    
    if self.BACK_BUTTON.checkForInput(self.mouse_pos):
        if pygame.mouse.get_pressed()[0] == 1:
            self.button_pressed = True
        elif pygame.mouse.get_pressed()[0] == 0 and self.button_pressed == True:
            self.game_state = 3
            self.button_pressed = False

    if self.NEXT_BUTTON.checkForInput(self.mouse_pos):
        if pygame.mouse.get_pressed()[0] == 1:
            self.button_pressed = True
        elif pygame.mouse.get_pressed()[0] == 0 and self.button_pressed == True:
            self.player_index += 1
            if self.player_index == 6:
                self.player_index = 1
            self.button_pressed = False
    
    if self.PREV_BUTTON.checkForInput(self.mouse_pos):
        if pygame.mouse.get_pressed()[0] == 1:
            self.button_pressed = True
        elif pygame.mouse.get_pressed()[0] == 0 and self.button_pressed == True:
            self.player_index -= 1
            if self.player_index == 0:
                self.player_index = 5
            self.button_pressed = False

    if self.CONFIRM_BUTTON.checkForInput(self.mouse_pos):
        if pygame.mouse.get_pressed()[0] == 1:
            self.button_pressed = True
        elif pygame.mouse.get_pressed()[0] == 0:
            if self.button_pressed == True:
                self.game_state = 5
                self.button_pressed = False
    
    self.player.player_set = self.player_set    
    self.player.player_index = self.player_index
    self.player.update()

#Main game
def game_play(self):
    #Display the map
    self.display.fill("#3A9BDC")
    self.display.blit(pygame.transform.scale(pygame.image.load(f'data/map/{self.map_index}/{self.map_size}.png'), (self.width, self.height)), (0,0))
    #Display the cars
    self.car1.player_set = self.player1.player_set
    self.car1.player_index = self.player1.player_index
    self.car1.update()
    self.car2.player_set = self.player2.player_set
    self.car2.player_index = self.player2.player_index
    self.car2.update()
    self.car3.player_set = self.player3.player_set
    self.car3.player_index = self.player3.player_index
    self.car3.update()
    self.car4.player_set = self.player4.player_set
    self.car4.player_index = self.player4.player_index
    self.car4.update()
    self.car5.player_set = self.player5.player_set
    self.car5.player_index = self.player5.player_index
    self.car5.update()
    
#Button    
def button_load(self):
    button_animation(self)
    self.START = Button(image = None ,pos = (self.width / 2, self.height * 0.85),text_input = f"{self.select_map_text}", 
                        font = self.LightPixel_font, base_color = self.base_color, hovering_color = self.hovering_color)
    self.LANGUAGE = Button(image = None, pos = ((self.width * 0.95 - get_text_size(self, "<LANGUAGE>")[0] / 2), (self.height * 0.3)),text_input = "<LANGUAGE>", 
                           font = self.LightPixel_font, base_color = self.base_color, hovering_color = self.hovering_color)
    self.HISTORY = Button(image = None, pos = ((self.width * 0.95 - get_text_size(self, "<HISTORY>")[0] / 2),(self.height * 0.4)),text_input = "<HISTORY>", 
                          font = self.LightPixel_font, base_color = self.base_color, hovering_color = self.hovering_color)
    self.MUSIC = Button(image = None, pos = ((self.width * 0.95 - get_text_size(self, "<MUSIC>")[0] / 2),(self.height * 0.5)), text_input = "<MUSIC>",
                        font = self.LightPixel_font, base_color = self.base_color, hovering_color = self.hovering_color)
    self.SIZE = Button(image = None, pos = ((self.width * 0.95 - get_text_size(self, "<SIZE>")[0] / 2),(self.height * 0.6)), text_input = "<SIZE>",
                       font = self.LightPixel_font, base_color = self.base_color, hovering_color = self.hovering_color)
    self.CREDITS = Button(image = None, pos = ((self.width * 0.95 - get_text_size(self, "<CREDITS>")[0] / 2),(self.height * 0.7)), text_input = "<CREDITS>",
                          font = self.LightPixel_font, base_color = self.base_color, hovering_color = self.hovering_color)
    self.MINIGAME = Button(image = None, pos = ((self.width * 0.95 - get_text_size(self, "<MINIGAME>")[0] / 2),(self.height * 0.8)), text_input = "<MINIGAME>",
                           font = self.LightPixel_font, base_color = self.base_color, hovering_color = self.hovering_color)
    self.MONEY = Button(image = None, pos = ((self.width * 0.05 + get_text_size(self, f"MONEY {self.money}")[0] * 0.55), self.height * 0.4), text_input = f"MONEY {self.money}",
                        font = self.LightPixel_font, base_color = self.hovering_color, hovering_color = self.hovering_color)
    self.NAME = Button(image = None , pos = ((self.width * 0.05 + get_text_size(self, f"Hi {self.player_name}!")[0] * 0.55), self.height * 0.3), text_input = f"Hi {self.player_name}!",
                       font = self.LightPixel_font, base_color = self.hovering_color, hovering_color = self.hovering_color)
    self.LEFTBUTTON = Button(image = None, pos = (self.width * 0.3,self.height * 0.55), text_input = "<",
                            font = self.DIRECTION_font, base_color = self.base_color, hovering_color = self.hovering_color)
    self.RIGHTBUTTON = Button(image = None, pos = (self.width * 0.71,self.height * 0.55), text_input = ">",
                            font = self.DIRECTION_font, base_color = self.base_color, hovering_color = self.hovering_color)
    self.QUIT = Button(image = None, pos = ((self.width * 0.05 + get_text_size(self, f"<QUIT>")[0] * 0.55), self.height * 0.95), text_input = "<QUIT>",
                       font = self.LightPixel_font, base_color = self.base_color, hovering_color = self.hovering_color)
    self.MAP_SIZE = Button(image = None, pos = (self.width / 2, self.height * 0.7), text_input = f"MAP SIZE: {self.map_size}",
                           font = self.LightPixel_font, base_color = self.base_color, hovering_color = self.base_color)
    #Button update
    for button in [self.START, self.LANGUAGE, self.HISTORY, self.MUSIC, self.LEFTBUTTON,
                   self.RIGHTBUTTON, self.SIZE, self.CREDITS, self.MINIGAME, self.QUIT, self.MAP_SIZE]:
        button.changeColor(self.mouse_pos)
        button.update(self.display)
    
    for button in [self.MONEY, self.NAME]:
        button.update(self.display)

def check_button_pressed(self):
    #Check if start button is pressed
    if self.START.checkForInput(self.mouse_pos) and pygame.mouse.get_pressed()[0] == 1:
        if pygame.mouse.get_pressed()[0] == 1:
            self.game_state = 3

    #Change screen size
    if self.SIZE.checkForInput(self.mouse_pos):
        if pygame.mouse.get_pressed()[0] == 1:
            self.button_pressed = True
        elif pygame.mouse.get_pressed()[0] == 0 and self.button_pressed == True:
            if self.size_state == 0:
                self.screen_size = [1200, 600]
                self.screen = pygame.display.set_mode((self.screen_size[0], self.screen_size[1]))
                self.size_state = 1
            elif self.size_state == 1:
                self.screen_size = [1400, 700]
                self.screen = pygame.display.set_mode((self.screen_size[0], self.screen_size[1]))
                self.size_state = 2
            elif self.size_state == 2:
                self.screen_size = [1920, 1080]
                self.screen = pygame.display.set_mode((self.screen_size[0], self.screen_size[1]), pygame.FULLSCREEN)
                self.size_state = 0
            self.button_pressed = False
        
    #Check if credits button is pressed
    if self.CREDITS.checkForInput(self.mouse_pos):
        if pygame.mouse.get_pressed()[0] == 1 and self.credits_state == 0:
            self.main_menu_state = 0
            self.credits_state = 1

    #Check if minigame button is pressed
    if self.MINIGAME.checkForInput(self.mouse_pos):
        if pygame.mouse.get_pressed()[0] == 1 and self.minigame_state == 0:
            self.main_menu_state = 0
            self.minigame_state = 1
            
    #Check if quit button is pressed
    if self.QUIT.checkForInput(self.mouse_pos):
        if pygame.mouse.get_pressed()[0] == 1:
            pygame.quit()
            exit()
    
    
#Animation
def button_animation(self):
    self.select_map_texts = [">SELECT THIS MAP<", "> SELECT THIS MAP <"]
    self.startgame_texts = [">Press SPACE to start<", "> Press SPACE to start <"]
    self.choose_player_set_texts = [">Choose your player set<", "> Choose your player set <"]
    self.choose_player_texts = [">Choose your player<", "> Choose your player <"]
    self.confirm_texts = ["<CONFIRM>", "< CONFIRM >"]
    self.text_state += 0.03
    self.select_map_text = self.select_map_texts[(int(self.text_state) % 2)] 
    self.startgame_text = self.startgame_texts[(int(self.text_state) % 2)] 
    self.choose_player_set_text = self.choose_player_set_texts[(int(self.text_state) % 2)]    
    self.confirm_text = self.confirm_texts[(int(self.text_state) % 2)]
    self.choose_player_text = self.choose_player_texts[(int(self.text_state) % 2)]
#Choose Map
def map_load(self):
    self.map_surface = self.assets['map_preview'][int(self.map_state) % len(self.assets['map_preview'])]
    self.map_rect = self.map_surface.get_rect(center = (self.width / 2, self.height * 0.525))
    self.display.blit(pygame.transform.rotozoom(self.map_surface, 0, 1), self.map_rect)  

def choose_map_right(self):
    if pygame.mouse.get_pressed()[0] == 1:
        self.button_pressed = True
    elif pygame.mouse.get_pressed()[0] == 0 and self.button_pressed == True:
            self.map_state += 1
            self.map_index += 1
            if self.map_state == len(self.assets['map_preview']):
                self.map_index = 1
                self.map_state = 0
            self.button_pressed = False

def choose_map_left (self):
    if pygame.mouse.get_pressed()[0] == 1:
        self.button_pressed = True
    elif pygame.mouse.get_pressed()[0] == 0 and self.button_pressed == True:
            self.map_state -= 1
            self.map_index -= 1
            if self.map_state == 0:
                self.map_state = len(self.assets['map_preview'])
            if self.map_index == 0:
                self.map_index = 5
            self.button_pressed = False

def choose_map_size(self, game):
    self.game = game
    if pygame.mouse.get_pressed()[0] == 1:
        self.button_pressed = True
    elif pygame.mouse.get_pressed()[0] == 0 and self.button_pressed == True:
        if self.game.map_size == "SMALL":
            self.game.map_size = "MEDIUM"
        elif self.game.map_size == "MEDIUM":
            self.game.map_size = "LARGE"
        elif self.game.map_size == "LARGE":
            self.game.map_size = "SMALL"
        self.map_size = self.game.map_size
        self.button_pressed = False
        
#Choose Player Set    
def player_load(self):
    update_assets(self, self.assets)
    self.player_state += 0.05
    self.player_surface = self.assets['players'][int(self.player_state) % len(self.assets['players'])]
    self.player_size = get_image_size(self,self.player_surface)
    self.player_rect = self.player_surface.get_rect(bottomright = (self.width / 2 - self.player_size[0], self.height / 2 - self.player_size[1]))
    self.display.blit(pygame.transform.rotozoom(self.player_surface, 0, 5), self.player_rect)

def choose_player_right(self):
    if pygame.mouse.get_pressed()[0] == 1:
        self.button_pressed = True
    elif pygame.mouse.get_pressed()[0] == 0 and self.button_pressed == True:
            self.player_index += 1
            if self.player_index == count_child_folders('data/player/') + 1:
                self.player_index = 1
            self.button_pressed = False
            
def choose_player_left(self):
    if pygame.mouse.get_pressed()[0] == 1:
        self.button_pressed = True
    elif pygame.mouse.get_pressed()[0] == 0 and self.button_pressed == True:
            self.player_index -= 1
            if self.player_index == 0:
                self.player_index = count_child_folders('data/player/')
            self.button_pressed = False

        