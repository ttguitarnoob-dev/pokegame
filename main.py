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
image = data['sprites']['other']['official-artwork']['front_default']
# print(image)

# Game Window
screen = pygame.display.set_mode((800, 480))
pygame.display.set_caption("Hazel's Pokegame")

# Background
background = pygame.image.load('background.png')


# function

# Game Loop

running = True
while True:
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    # Drawing the Screen
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    pygame.display.flip()
    clock.tick(60)

    