import pygame, sys

class Button:
	def __init__(self, image, pos, text_input, font, base_color, hovering_color):
		self.image = image
		self.x_pos = pos[0]
		self.y_pos = pos[1]
		self.font = font
		self.base_color, self.hovering_color = base_color, hovering_color
		self.text_input = text_input
		self.text = self.font.render(self.text_input, True, self.base_color)
		if self.image is None:
			self.image = self.text
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
    