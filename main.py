import pygame, sys
import requests

# Initialize Pygame
pygame.init()

# Variables
# When searching for a poke, do an api call with URL and concatenate the user inputted name at the end
URL = 'https://pokeapi.co/api/v2/pokemon/'
clock = pygame.time.Clock()
poke = 'charmander'
response = requests.get(URL + poke)
data = response.json()
poke_image = data['sprites']['other']['official-artwork']['front_default']
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
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Drawing the Screen
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    player_sprite.draw(screen)
    pygame.display.flip()
    clock.tick(60)

    