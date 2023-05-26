import pygame, sys
from settings import *
from level import Level
from game_data import level_0
from overworld import Overworld
from ui import UI
from button import Button

class Game:
	def	__init__(self):

		#game atribut 
		self.max_level = 4
		self.max_health = 100
		self.cur_health = 100
		self.coins = 0

		# audio 
		self.level_bg_music = pygame.mixer.Sound('audio/level_music.wav')
		self.overworld_bg_music = pygame.mixer.Sound('audio/overworld_music.wav')

		#overworld
		self.overworld = Overworld(0, self.max_level, screen,self.create_level)
		self.status = 'overworld'
		self.overworld_bg_music.play(loops = -1)

		#user interface
		self.ui = UI(screen)

	def create_level(self,current_level):
		self.level = Level(current_level, screen, self.create_overworld, self.change_coins, self.change_health)
		self.status = 'level'
		self.overworld_bg_music.stop()
		self.level_bg_music.play(loops=-1)

	def create_overworld(self,current_level,new_max_level):
		if new_max_level > self.max_level:
			self.max_level = new_max_level
		self.overworld = Overworld(current_level,self.max_level,screen,self.create_level)
		self.status = 'overworld'
		self.overworld_bg_music.play(loops = -1)
		self.level_bg_music.stop()

	def	change_coins(self,amount):
		self.coins += amount

	def change_health(self,amount):
		self.cur_health += amount

	def check_game_over(self):
		if self.cur_health <= 0:
			self.cur_health = 100
			self.coins = 0
			self.max_level = 0
			self.overworld = Overworld(0, self.max_level, screen,self.create_level)
			self.status = 'overworld'

	def run(self):
		if self.status == 'overworld':
			self.overworld.run()
		else:
			self.level.run()
			self.ui.show_health(self.cur_health,self.max_health)
			self.ui.show_coins(self.coins)
			self.check_game_over()

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Jungle Dash")
clock = pygame.time.Clock()
game = Game()

def play():
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
		
		screen.fill('grey')
		game.run()
		
		pygame.display.update()
		clock.tick(60)

BG = pygame.image.load('assets/daw.png')

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        screen.fill("white")

        OPTIONS_TEXT = get_font(25).render("Menu Ini dalam tahap pengembangan.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        screen.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def main_menu():
    while True:
        screen.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("Jungle Dash", True, "#58C6CA")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 70))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 180), 
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 300), 
                            text_input="SETTING", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        LEVEL_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 420), 
                            text_input="LEVEL", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        ABOUT_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 540), 
                            text_input="ABOUT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 660), 
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        screen.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON, LEVEL_BUTTON, ABOUT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if LEVEL_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if ABOUT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()