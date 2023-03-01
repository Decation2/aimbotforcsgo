import pygame
import time
import ctypes
import math

# Initialize pygame
pygame.init()

# Set the size of the display window
display_width = 800
display_height = 600

# Set the window
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Aimbot')

# Set the clock
clock = pygame.time.Clock()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Player's mouse position
player_x = display_width // 2
player_y = display_height // 2

# Enemy's mouse position
enemy_x = 0
enemy_y = 0

# Speed of aimbot
aim_speed = 0.5

# Aimbot's current speed
current_speed = 0

# Aimbot's current angle
current_angle = 0

# Aimbot's current x and y coordinates
aimbot_x = 0
aimbot_y = 0

def get_mouse_position():