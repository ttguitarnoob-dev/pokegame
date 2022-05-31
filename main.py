import random
import pygame, sys, shutil, os
import requests

# Initialize Pygame
pygame.init()

# Variables
clock = pygame.time.Clock()
poke_list = []
current_poke = ''
dest = (100, 100)

# Player Movement Variables
moving_right = False
moving_left = False
moving_up = False
moving_down = False

# Poke list populate

poke_url = 'https://pokeapi.co/api/v2/pokemon/?limit=770'
resp = requests.get(poke_url)
data = resp.json()
for i in data['results']:
    poke_list.append(i['name'])


# New Poke
def new_poke(poke):
    global current_poke
    URL = 'https://pokeapi.co/api/v2/pokemon/'
    response = requests.get(URL + poke)
    data = response.json()
    poke_image_url = data['sprites']['other']['official-artwork']['front_default']
    filename = poke + '.png'
    dl = requests.get(poke_image_url, stream = True)
    dl.raw.decode_content = True
    with open(filename, 'wb') as f:
        shutil.copyfileobj(dl.raw, f)
    current_poke = filename

# Quit Game
def quit_game():
    global run
    if current_poke != '':
        os.remove(current_poke)
    run = False


# Game Window
screen = pygame.display.set_mode((1255, 900))
pygame.display.set_caption("Hazel's Pokegame")


# Background
background = pygame.image.load('background.png')


# Sprite Classes wooooo let's hope I can make this work as a noob
class Player(pygame.sprite.Sprite):
    def __init__(self, image, pos_x, pos_y, speed):
        super().__init__()
        self.speed = speed
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.center = (pos_x, pos_y)

    def move(self, moving_left, moving_right, moving_up, moving_down):
        # Movement Variables
        dx = 0
        dy = 0

        # Assign movement left or right up or down
        if moving_left:
            dx = -self.speed
        if moving_right:
            dx = self.speed
        if moving_up:
            dy = -self.speed
        if moving_down:
            dy = self.speed

        # Update rectangle position
        self.rect.x += dx
        self.rect.y += dy

# Sprite Groups
player_sprite = pygame.sprite.Group()
player = Player('pikachu.png', 100, 100, 5)
player_sprite.add(player)
        
        

# Game Loop
run = True
while run:

    # Drawing the Screen
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    player_sprite.draw(screen)
    if current_poke != '':
        poke_load = pygame.image.load(current_poke)
        screen.blit(poke_load, dest)
    player.move(moving_left, moving_right, moving_up, moving_down)
    pygame.display.flip()
    clock.tick(60)

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game()
        
        # Keyboard Events
        if event.type == pygame.KEYDOWN:

            # Player Movement
            if event.key == pygame.K_LEFT:
                moving_left = True
            if event.key == pygame.K_RIGHT:
                moving_right = True
            if event.key == pygame.K_UP:
                moving_up = True
            if event.key == pygame.K_DOWN:
                moving_down = True
            
            # Quit Game
            if event.key == pygame.K_ESCAPE:
                quit_game()

            # Summon poke
            if event.key == pygame.K_t:
                if current_poke != '':
                    os.remove(current_poke)
                new_poke(poke_list[random.randrange(len(poke_list))])


        # Keyboard Release
        if event.type == pygame.KEYUP:

            # Player Movement
            if event.key == pygame.K_LEFT:
                moving_left = False
            if event.key == pygame.K_RIGHT:
                moving_right = False
            if event.key == pygame.K_UP:
                moving_up = False
            if event.key == pygame.K_DOWN:
                moving_down = False


    

    