import pygame

class Button:
	def __init__(self, image, pos, text_input, font, base_color, hovering_color):
		self.image = image
		self.x_pos = pos[0]
		self.y_pos = pos[1]
		self.font = font
		self.base_color, self.hovering_color = base_color, hovering_color
		self.text_input = text_input
		self.text = self.font.render(self.text_input, True, self.base_color)
		if image is None:
			self.image = self.text
		else:
			self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
			self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))
			self.image = pygame.transform.scale(image, (self.text_rect.width + 50, self.text_rect.height + 30))
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))
		

	def update(self, screen):
		if self.image is not None:
			screen.blit(self.image, self.rect)  
		screen.blit(self.text, self.text_rect)

	def checkForInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			return True
		return False

	def changeColor(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = self.font.render(self.text_input, True, self.hovering_color)
		else:
			self.text = self.font.render(self.text_input, True, self.base_color)

class CustomButton:
	def __init__(self, game, text, img1, img2, pos, type = None):
		#Core attributes
		self.game = game
		self.original_y_pos = pos[1]
		self.type = type
		self.pos = pos
		self.click_fx = pygame.mixer.Sound('data/sounds/click.wav')
		self.click_fx.set_volume(0.5)
		#Unclicked image
		self.img1 = img1
		self.img1_rect = self.img1.get_rect(center = pos)
		self.current_img = self.img1

		#Clicked image
		self.img2 = img2
		self.img2_rect = self.img2.get_rect(center = pos)

		#Text
		self.text = self.game.LightPixel_font.render(text, True, '#FFFFFF')
		self.text_rect = self.text.get_rect(center = pos)
				
	def update(self):
		#Idea
		#---#
		mouse_pos = pygame.mouse.get_pos()
		self.current_img_rect = self.current_img.get_rect(center = self.pos)
		if self.current_img_rect.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0] == 1:
			self.current_img = self.img2
			self.current_img_rect = self.current_img.get_rect(center = self.pos)
			self.game.button_pressed = True
		elif self.current_img_rect.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0] == 0 and self.game.button_pressed == True:
			self.current_img = self.img2
			self.current_img_rect = self.current_img.get_rect(center = self.pos)
			self.button_logic()
			self.game.button_pressed = False
		self.game.display.blit(self.current_img, self.current_img_rect)
  
	def button_logic(self):
		self.click_fx.play()
		if self.type == 'bet_plus':
			if self.game.bet + 20 <= self.game.money:
				self.game.bet += 20
		elif self.type == 'bet_minus':
			if self.game.bet > 100 and self.game.bet - 20 >= 100:
				self.game.bet -= 20
		elif self.type == 'bet_all':
			if self.game.money >= 100:
				self.game.bet = self.game.money
		elif self.type == 'bet_50':
			if self.game.money >= 100 and self.game.bet <= self.game.money * 0.5:
				self.game.bet += int(self.game.money / 2)
		elif self.type == 'bet +20':
			if self.game.money >= 100 and self.game.bet <= self.game.money * 0.8:
				self.game.bet += int(self.game.money / 5)
		elif self.type == 'bet +10' and self.game.bet <= self.game.money * 0.9:
			if self.game.money >= 100:
				self.game.bet += int(self.game.money / 10)
		elif self.type == 'bet -20':
			if self.game.money >= 100 and self.game.bet - int(self.game.money / 5) > 100:
				self.game.bet -= int(self.game.money / 5)
		elif self.type == 'bet -10':
			if self.game.money >= 100 and self.game.bet - int(self.game.money / 10) > 100:
				self.game.bet -= int(self.game.money / 10)
		elif self.type == 'choose_map_left':
			self.game.map_state -= 1
			self.game.map_index -= 1
			if self.game.map_state == -1:
				self.game.map_state = 4
				self.game.map_index = 5
		elif self.type == 'choose_map_right':
			self.game.map_state += 1
			self.game.map_index += 1
			if self.game.map_state == 5:
				self.game.map_index = 1
				self.game.map_state = 0
		elif self.type == 'how_left':
			self.game.how_index -= 1
			if self.game.how_index == -1:
				self.game.how_index = 2
		elif self.type == 'how_right':
			self.game.how_index += 1
			if self.game.how_index == 3:
				self.game.how_index = 0
class AnimatedButton:
	pressed = False
	def __init__(self,game,text,width,height,pos,elevation):
		#Core attributes
		self.game = game
		self.elevation = elevation
		self.dynamic_elecation = elevation
		self.original_y_pos = pos[1]
  
		# top rectangle 
		self.top_rect = pygame.Rect(pos,(width,height))
		self.top_color = '#475F77'

		# bottom rectangle
		self.bottom_rect = pygame.Rect(pos,(width,height))
		self.bottom_color = '#354B5E'

		#text
		self.text_surf = self.game.LightPixel_font.render(text,True,'#FFFFFF')
		self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)

	def draw(self):
		# elevation logic
		self.check_click()
		self.top_rect.y = self.original_y_pos - self.dynamic_elecation
		self.text_rect.center = self.top_rect.center 
		
		self.bottom_rect.midtop = self.top_rect.midtop
		self.bottom_rect.height = self.top_rect.height + self.dynamic_elecation
  
		pygame.draw.rect(self.game.display,self.bottom_color, self.bottom_rect,border_radius = 100)
		pygame.draw.rect(self.game.display,self.top_color, self.top_rect,border_radius = 100)
		self.game.display.blit(self.text_surf, self.text_rect)


	def check_click(self):
		mouse_pos = pygame.mouse.get_pos()
		if self.top_rect.collidepoint(mouse_pos):
			self.top_color = "#D74B4B"
			if pygame.mouse.get_pressed()[0]:
				AnimatedButton.pressed = True
				self.dynamic_elecation = 0
			else:
				self.dynamic_elecation = self.elevation
				if AnimatedButton.pressed == True:
					if self.game.money < 100:
						self.game.money += 1
					AnimatedButton.pressed = False
		else:
			self.dynamic_elecation = self.elevation
			self.top_color = '#475F77'
