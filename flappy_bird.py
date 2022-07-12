# Importing all the necessary libraries
import pygame
import neat # Neuro-Evolution of Augmenting Topologies -> It's an Algorithm.
import time
import os
import random # for randomly placing the tubes and bird(at starting generation)

# Set the dimension of the screen
WIN_WIDTH=700 # All capitals because these are constants, it is a convention.
WIN_HEIGHT=800

# Load all the images

BIRD_IMGS=[pygame.transform.scale2x(pygame.image.load(os.path.join("imgs","bird1.png"))),pygame.transform.scale2x(pygame.image.load(os.path.join("imgs","bird2.png"))),pygame.transform.scale2x(pygame.image.load(os.path.join("imgs","bird3.png")))]
PIPE_IMG=pygame.transform.scale2x(pygame.image.load(os.path.join("imgs","pipe.png")))
BASE_IMG=pygame.transform.scale2x(pygame.image.load(os.path.join("imgs","base.png")))
BG_IMG=pygame.transform.scale2x(pygame.image.load(os.path.join("imgs","bg.png")))


