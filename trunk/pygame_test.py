import os
import sys
import pygame

def getimages(d):
    return [os.path.join(d, f) for f in os.listdir(d) if f.endswith('.png')]

pygame.init()
screen = pygame.display.set_mode((1280, 800))

images = [pygame.image.load(i).convert() for i in getimages('../images')]

while True:
    event = pygame.event.wait()

    if event.type == pygame.QUIT: sys.exit()
