import pygame, sys

class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.jump = False
        self.jumpCount = 5
        self.left = False
        self.right = False
        self.walkCount = 0