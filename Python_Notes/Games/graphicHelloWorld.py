import pygame, sys
from pygame.locals import *

# First thing we do is start pygame
pygame.init()

# Then we create the window
windowSurface = pygame.display.set_mode((500,400),0,32)
pygame.display.set_caption('Hello World!')  # Caption displayed at top of window

# Globals for colours so we don't have to constantly write the rgb codes
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

# Set up font
# format is (filename, size)
basicFont = pygame.font.SysFont(None, 48)   # Uses system font

# set up text
text = basicFont.render('Hello World!', True, WHITE, BLUE)
textRect = text.get_rect()                  # making a rectangle
textRect.centerx = windowSurface.get_rect().centerx # Centering it in the window w.r.t. x coordinates
textRect.centery = windowSurface.get_rect().centery # Centering it in the window w.r.t. y coordinates

# Draw white background
windowSurface.fill(BLACK)

# Draw a red rectangle onto surface
pygame.draw.rect(windowSurface,RED,(textRect.left-20, textRect.top-20, textRect.width+40, textRect.height+40))
# get pixel array of surface
pixArray = pygame.PixelArray(windowSurface)
pixArray[480][380] = BLACK
del pixArray

# Draw text onto surface
windowSurface.blit(text,textRect)

# Draw window onto screen
pygame.display.update()

# Run game while loop is true
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

