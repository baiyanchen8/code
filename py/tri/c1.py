import pygame
import random
import sys

# Load the images
image1 = pygame.image.load('picture/ghost.png')
image2 = pygame.image.load('picture/pacmandown.png')
image1 = pygame.transform.scale(image1, (40, 40))
image2 = pygame.transform.scale(image2, (40, 40))
# Create the Pygame window
screen_width = 1000
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))

# Define the objects' initial positions and velocities
object1_rect = pygame.Rect(0, 0, image1.get_width(), image1.get_height())
object2_rect = pygame.Rect(screen_width - image2.get_width(), 0, image2.get_width(), image2.get_height())

object1_velocity = pygame.math.Vector2(random.uniform(-5, 5), random.uniform(-5, 5))
object2_velocity = pygame.math.Vector2(random.uniform(-5, 5), random.uniform(-5, 5))

# Implement the game loop
clock = pygame.time.Clock()

while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update object positions
    object1_rect.move_ip(object1_velocity)
    object2_rect.move_ip(object2_velocity)

    # Check for collisions
    if object1_rect.colliderect(object2_rect):
        # Calculate new velocities for elastic collision
        normal_vector = pygame.math.Vector2(object2_rect.center) - pygame.math.Vector2(object1_rect.center)
        unit_normal_vector = normal_vector.normalize()
        unit_tangent_vector = pygame.math.Vector2(-unit_normal_vector.y, unit_normal_vector.x)

        object1_normal_velocity = object1_velocity.dot(unit_normal_vector)
        object2_normal_velocity = object2_velocity.dot(unit_normal_vector)

        object1_tangent_velocity = object1_velocity.dot(unit_tangent_vector)
        object2_tangent_velocity = object2_velocity.dot(unit_tangent_vector)

        new_object1_normal_velocity = (object1_normal_velocity * (object1_rect.width - object2_rect.width) + 2 * object2_rect.width * object2_normal_velocity) / (object1_rect.width + object2_rect.width)
        new_object2_normal_velocity = (object2_normal_velocity * (object2_rect.width - object1_rect.width) + 2 * object1_rect.width * object1_normal_velocity) / (object1_rect.width + object2_rect.width)

        new_object1_velocity = (new_object1_normal_velocity * unit_normal_vector) + (object1_tangent_velocity * unit_tangent_vector)
        new_object2_velocity = (new_object2_normal_velocity * unit_normal_vector) + (object2_tangent_velocity * unit_tangent_vector)

        object1_velocity = new_object1_velocity
        object2_velocity = new_object2_velocity

    # Draw objects to screen
    screen.blit(image1, object1_rect)
    screen.blit(image2, object2_rect)
    
    # Update screen
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)
