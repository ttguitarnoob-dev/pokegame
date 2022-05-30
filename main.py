import pygame, sys
import requests

# Initialize Pygame
pygame.init()

# Variables

# Player Movement Variables
moving_right = False
moving_left = False

# When searching for a poke, do an api call with URL and concatenate the user inputted name at the end
URL = 'https://pokeapi.co/api/v2/pokemon/'
clock = pygame.time.Clock()
poke = 'charmander'
response = requests.get(URL + poke)
data = response.json()
poke_image_url = data['sprites']['other']['official-artwork']['front_default']
# print(image)

# Game Window
screen = pygame.display.set_mode((800, 480))
pygame.display.set_caption("Hazel's Pokegame")

# Background
background = pygame.image.load('background.png')


# Sprite Classes wooooo let's hope I can make this work as a noob

class Player(pygame.sprite.Sprite):
    def __init__(self, image, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]


# Sprite Groups
player_sprite = pygame.sprite.Group()
player = Player('pikachu.png', 100, 100)
player_sprite.add(player)
        
        

# Game Loop
run = True
while run:

    # Drawing the Screen
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    player_sprite.draw(screen)
    pygame.display.flip()
    clock.tick(60)

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        # Keyboard Events
        if event.type == pygame.KEYDOWN:

            # Keyboard Press
            if event.key == pygame.K_LEFT:
                moving_left = True
            if event.key == pygame.K_RIGHT:
                moving_right = True
            
            # Quit Game
            if event.key == pygame.K_ESCAPE:
                run = False



        # Keyboard Release
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                moving_left = False
            if event.key == pygame.K_RIGHT:
                moving_right = False


    

    