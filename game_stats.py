class GameStats:
    def __init__(self, heart_game):
        """Initialize the game stats"""
        self.settings = heart_game.settings
        self.reset_stats()

        self.game_active = True

    def reset_stats(self):
        """Reset the game stats"""
        self.hearts_left = self.settings.heart_limit