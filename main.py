import random
import pygame, sys, shutil, os
import requests

# Initialize Pygame
pygame.init()

#############
# Variables #
#############

# Global
clock = pygame.time.Clock()
poke_list = []
current_poke = None
wind_width = 1255
wind_height = 900
spawn_x = random.randrange(wind_width)
spawn_y = random.randrange(wind_height)
dest = (spawn_x, spawn_y)
black = pygame.color.Color('#000000')
font = pygame.font.Font(None, 40)
message = 'Pikachu is here'
enemy_stats = []


# Game Window
screen = pygame.display.set_mode((wind_width, wind_height))
pygame.display.set_caption("Hazel's Pokegame")


# Background
background = pygame.image.load('background.png')
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

#############
# FUNCTIONS #
#############

# New Poke
def new_poke(poke):
    global current_poke, enemy, enemy_stats
    URL = 'https://pokeapi.co/api/v2/pokemon/'
    response = requests.get(URL + poke)
    data = response.json()
    poke_image_url = data['sprites']['other']['official-artwork']['front_default']
    filename = poke + '.png'
    dl = requests.get(poke_image_url, stream = True)
    dl.raw.decode_content = True
    with open(filename, 'wb') as filex:
        shutil.copyfileobj(dl.raw, filex)
    current_poke = filename
    stats = data['stats']
    abilities = data['abilities']
    name = data['name']
    enemy = Enemy(current_poke, spawn_x, spawn_y, stats, abilities, name)
    enemy_sprite.add(enemy)
    enemy_stats = []
    enemy.display_stats()
    

# Quit Game
def quit_game():
    global run
    if current_poke != '':
        os.remove(current_poke)
    print('Thanks for playing!')
    run = False





#################
# SPRITE CLASSES #
 ################

# Player
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

# Enemy
class Enemy(pygame.sprite.Sprite):
    def __init__(self, image, pos_x, pos_y, stats, abilities, name):
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.center = (pos_x, pos_y)
        self.stats = stats
        self.abilities = abilities
        self.name = name
    
    def dead(self):
        self.kill()
    
    def display_stats(self):
        enemy_stats.append(f"{str(self.stats[0]['stat']['name'])}: {str(self.stats[0]['base_stat'])}")
        enemy_stats.append(self.name.capitalize())
        print(self.stats[0])


#################
# Sprite Groups #
#################

# Player
player_sprite = pygame.sprite.Group()
player = Player('player.png', spawn_x, spawn_y, 5)
player_sprite.add(player)

# Enemy
enemy_sprite = pygame.sprite.Group()
enemy = None
        
        
#############
# Game Loop #
#############
run = True
while run:

    # Drawing the Screen
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    player_sprite.draw(screen)
    if current_poke != None:
        enemy_sprite.draw(screen)
        bottom = 5
        for i in enemy_stats:
            bottom += 30
            text = font.render(i, True, black)
            screen.blit(text, (30, wind_height - bottom))

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
                if current_poke != None:
                    enemy.dead()
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


    

    