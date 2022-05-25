import pygame
import requests

# Variables
# When searching for a poke, do an api call with URL and concatenate the name at the end
URL = 'https://pokeapi.co/api/v2/pokemon/'

poke = 'charmander'
response = requests.get(URL + poke)
data = response.json()
image = data['sprites']['other']['official-artwork']['front_default']
# print(image)

# Game Window
screen = pygame.display.set_mode((800, 480))

# Background
background = pygame.image.load('background.png')


# function

# Game Loop

running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))