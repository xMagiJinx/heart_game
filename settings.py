from background import TILE
import pygame
class Settings:
    """Store settings for heart game"""
    def __init__(self):
        """Initialize game settings"""
        self.TILE = TILE
        self.screen_width = 1000
        self.screen_height = 600

        self.heart_speed = 3
        self.heart_limit = 0

        # Obstacle settings for red flags
        self.flag_appear = .01
        self.flag_speed = .5

        self.ghost_appear = .001
        self.ghost_speed = .1

        self.good_appear = .0001
        self.good_speed = .8