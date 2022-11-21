class Settings:
    """Store settings for heart game"""
    def __init__(self):
        """Initialize game settings"""
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (0,0,0)

        self.heart_speed = 3
        self.heart_limit = 3

        # Obstacle settings for red flags
        self.flag_appear = .005
        self.flag_speed = .5