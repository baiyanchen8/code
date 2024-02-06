import random
import threading
import pygame
import math
import time

# Initialize the game
pygame.init()

# Set up the screen
screen_width = 1000
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
background_image = pygame.image.load("picture/b1.jpg").convert()
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))
ghost_image=pygame.image.load("picture/R.png").convert_alpha()
# Define the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Define the game objects
class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        # Set the direction of the player to "right"
        self.direction = "right"

        # Load the image of the player
        self.image = pygame.image.load("picture/pacmanR.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (40, 40)) # Resize to 40x40
        self.rect = self.image.get_rect()

        # Set the player speed
        self.speed = 5

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self, walls):
        if self.direction == "right" and self.rect.right < screen_width:
            self.x += self.speed
            self.image = pygame.image.load("picture/pacmanR.png").convert_alpha()
            self.image = pygame.transform.scale(self.image, (40, 40))
        elif self.direction == "left" and self.rect.left > 0:
            self.x -= self.speed
            self.image = pygame.image.load("picture/pacmanL.png").convert_alpha()
            self.image = pygame.transform.scale(self.image, (40, 40))
        elif self.direction == "up" and self.rect.top > 0:
            self.y -= self.speed
            self.image = pygame.image.load("picture/pacmanTOP.png").convert_alpha()
            self.image = pygame.transform.scale(self.image, (40, 40))
        elif self.direction == "down" and self.rect.bottom < screen_height:
            self.y += self.speed
            self.image = pygame.image.load("picture/pacmandown.png").convert_alpha()
            self.image = pygame.transform.scale(self.image, (40, 40))
        self.collide_with_walls(walls)
        self.rect.x = round(self.x)  # Update the rect's x-coordinate
        self.collide_with_walls(walls)
        self.rect.y = round(self.y)  # Update the rect's y-coordinate
        self.collide_with_walls(walls)

    def collide_with_walls(self, walls):
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if self.direction == "right":
                    self.rect.right = wall.rect.left
                elif self.direction == "left":
                    self.rect.left = wall.rect.right
                elif self.direction == "up":
                    self.rect.top = wall.rect.bottom
                elif self.direction == "down":
                    self.rect.bottom = wall.rect.top

class Ghost_1:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed_init= 1
        self.speed = 1
        self.image = ghost_image
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()

    def move(self, player):
        dx = player.rect.centerx - self.rect.centerx
        dy = player.rect.centery - self.rect.centery
        dist = math.hypot(dx, dy)
        if dist != 0:
            dx = dx / dist
            dy = dy / dist
        self.x += dx * self.speed
        self.y += dy * self.speed
        self.rect.x = round(self.x)
        self.rect.y = round(self.y)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

class Ghost_2:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed_init= 2
        self.speed = 2
        self.image = ghost_image
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()

    def move(self, player):
        dx = player.rect.centerx - self.rect.centerx
        dy = player.rect.centery - self.rect.centery
        
        dir=player.direction
        if abs(dx)<=100 and abs(dy)<=100:
            pass
        elif dir=="right":
            dx+=100
        elif dir=="left":
            dx-=100
        elif dir=="up":
            dy-=100
        elif dir=="down":
            dy+=100
        
        dist = math.hypot(dx, dy)
        if dist != 0:
            dx = dx / dist
            dy = dy / dist
        self.x += dx * self.speed
        self.y += dy * self.speed
        self.rect.x = round(self.x)
        self.rect.y = round(self.y)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
class Ghost_3:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed_init= 1
        self.speed = 1
        self.image = ghost_image
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()

    def move(self, player):
        dx = player.rect.centerx - self.rect.centerx
        dy = player.rect.centery - self.rect.centery
        dist = math.hypot(dx, dy)
        if dist != 0:
            dx = dx / dist
            dy = dy / dist
        self.x += dx * self.speed
        self.y += dy * self.speed
        self.rect.x = round(self.x)
        self.rect.y = round(self.y)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)


walls = pygame.sprite.Group()
# create wall sprites and add them to the walls group
wall1 = Wall(0, 0, screen_width, 0)
wall2 = Wall(0, screen_height, screen_width, 0)
wall3 = Wall(0, 0, 0, screen_height)
wall4 = Wall(screen_width , 0,0, screen_height)
walls.add(wall1, wall2, wall3, wall4)


class Pellet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = YELLOW
        self.radius = 5

        # Create a rect for collision detection
        self.rect = pygame.Rect(self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius * 2)

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

# Create the game objects
player = Player(0, 0)
ghosts = [Ghost_1(400,400), Ghost_2(200, 200), Ghost_3(300, 300)]
pellets = []
def randomp(num):
    for i in range(num):
        dx=random.randrange(20, screen_width-20)
        dy=random.randrange(20, screen_height-20)
        pellets.append(Pellet(dx,dy))
randomp(150)
walls = pygame.sprite.Group()
score = 0
# screen_draw
def add_score(points):
    global score
    score += points
def draw_time(screen, time1):
    font = pygame.font.Font(None, 36)
    str1="Time: " + str(round(time1))
    score_text = font.render(str1, True, WHITE)
    screen.blit(score_text, (screen_width/2-len(str1)*9, 10))
def draw_score(screen, score):
    font = pygame.font.Font(None, 36)
    score_text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(score_text, (10, screen_height-50))

        
    # time.sleep(2)
clock = pygame.time.Clock()
# Game loop1
running = True
t1=time.time()
t2=t1
super_time=0
level=0

def player_run():
    while running:
        t2=time.time()
        # it can change the speed of player and ghost
        level=int((t2-t1)/2)/10
        clock.tick(60)
        superpower=False
        for event in pygame.event.get():
        
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.direction = "left"
                elif event.key == pygame.K_RIGHT:
                    player.direction = "right"
                elif event.key == pygame.K_UP:
                    player.direction = "up"
                elif event.key == pygame.K_DOWN:
                    player.direction = "down"
            keys=pygame.key.get_pressed()
            if (keys[pygame.K_END] and score>101):
                score-=100
                player.speed+=1
        # Update the player's movement automatically
        player.update(walls)
        # Check for collisions between the player and the pellets
        for pellet in pellets:
            if player.rect.colliderect(pellet.rect):
                pellets.remove(pellet)
                add_score(1)
        if len(pellets)<=250:
            randomp(100)
        # Draw the game objects on the screen
        screen.blit(background_image,(0,0))
        player.draw(screen)
        for ghost in ghosts:
            ghost.draw(screen)
        for pellet in pellets:
            pellet.draw(screen)
        walls.draw(screen)
        draw_score(screen, score)
    
        draw_time(screen,t2-t1)
        pygame.display.flip()

    
    
def ghost_run():
    while  running:
        # Move the ghosts and check for collisions with the player
        for ghost in ghosts:
            ghost.speed=level+ghost.speed_init
            ghost.move(player)
            if player.rect.colliderect(ghost.rect):
                print("Game over")
                running = False
        # Draw the game objects on the screen
        screen.blit(background_image,(0,0))
        player.draw(screen)
        for ghost in ghosts:
            ghost.draw(screen)
        for pellet in pellets:
            pellet.draw(screen)
        walls.draw(screen)
        draw_score(screen, score)
        draw_time(screen,t2-t1)
        pygame.display.flip()
        
a = threading.Thread(target=player_run())  
b = threading.Thread(target=ghost_run())  
a.start()
b.start()
print(round(t2-t1))
# Quit the game
