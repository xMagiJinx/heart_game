import sys
from random import random

import pygame

from pygame import mixer

from background import draw_background
from player import Player
from settings import Settings
from flags import Flags
from game_stats import GameStats
from ghosts import Ghosts
from lightning import Lightning
from battery import Battery
from lives import Lives



class HeartGame:
    """Create a main heart game"""

    def __init__(self):
        """Initialize the game"""
        pygame.init()

        self.settings = Settings()
        self.clock = pygame.time.Clock()

        # adding background music
        mixer.init()
        mixer.music.load('sounds/Falling-for-u-lofi-hiphop-mix.ogg')
        mixer.music.play()
        # make the actual game screen
        self.WINDOW_SIZE = (self.settings.screen_width, self.settings.screen_height)
        self.screen = pygame.display.set_mode(self.WINDOW_SIZE)
        self.bg = draw_background(self.WINDOW_SIZE)

        pygame.display.set_caption("Heart Game")
        self.font = pygame.font.Font('fonts/QuinqueFive.ttf', 27)

        self.stats = GameStats(self)

        self.player = Player(self)
        self.flags = pygame.sprite.Group()
        self.ghosts = pygame.sprite.Group()
        self.life = Lives(self)
        self.lightning = pygame.sprite.Group()
        self.battery = pygame.sprite.Group()

    def run_game(self):
        """Start the main loop to run the game"""
        while True:
            self._check_events()
            if self.stats.game_active:
                self.player.update()
                self.create_enemies()
                self.update_enemies()
                self.create_goodstuff()
                self.update_goodstuff()

            self._update_screen()
            self.clock.tick(175)
    def _check_events(self):
        """Respond to events such as keypresses and mouse"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
    def _check_keydown_events(self, event):
        """Respond to keydown events"""
        if event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_LEFT:
            self.player.moving_left = True
        elif event.key == pygame.K_RIGHT:
            self.player.moving_right = True
        elif event.key == pygame.K_a:
            self.player.moving_left = True
        elif event.key == pygame.K_d:
            self.player.moving_right = True

    def _check_keyup_events(self, event):
        """Respond to keyup events"""
        if event.key == pygame.K_RIGHT:
            self.player.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.player.moving_left = False
        elif event.key == pygame.K_d:
            self.player.moving_right = False
        elif event.key == pygame.K_a:
            self.player.moving_left = False

    def create_enemies(self):
        """Create bad stuff that will fall down the screen"""
        if random() < self.settings.flag_appear:
            flag = Flags(self)
            self.flags.add(flag)
        elif random() < self.settings.ghost_appear:
            ghost = Ghosts(self)
            self.ghosts.add(ghost)

    def update_enemies(self):
        """Update flags on the screen"""
        self.flags.update()
        self.ghosts.update()
        # check for flag, ghost and heart collision
        if pygame.sprite.spritecollideany(self.player, self.flags):
            self._player_hit()
        elif pygame.sprite.spritecollideany(self.player, self.ghosts):
            self._player_hit()

    def create_goodstuff(self):
        """Create good stuff or temporary powerups that fall down the screen"""
        if random() < self.settings.good_appear:
            good = Lightning(self)
            self.lightning.add(good)
        if random() < self.settings.good_appear:
            good2 = Battery(self)
            self.battery.add(good2)

    def update_goodstuff(self):
        """Update powerups"""
        self.lightning.update()
        self.battery.update()
        if pygame.sprite.spritecollideany(self.player, self.lightning):
            self._player_gain()
        if pygame.sprite.spritecollideany(self.player, self.battery):
            self._player_gain_health()

    def _player_hit(self):
        """Respond to getting hit by falling objects"""
        if self.stats.hearts_left > 0:
            self.stats.hearts_left -= 1
            # add the image of the hearts in the top left corner
            # need to change heart image to go down as the heart counter goes down
            self.life.update(self.stats.hearts_left)
            # sound effect when hit
            restart_sfx = pygame.mixer.Sound('sounds/Boss hit 1.wav')
            restart_sfx.play()

            # restart the screen
            self.flags.empty()
            self.ghosts.empty()
            self.battery.empty()
            self.lightning.empty()

            self.player.center_heart()
            self.player.score_value -= 5
            pygame.time.delay(999)
        else:
            # self.stats.game_active = False
            end_sfx = pygame.mixer.Sound('sounds/Game Over.wav')
            end_sfx.play()
            self.end_game()
    def end_game(self):
        """Ends the game and resets the information"""
        while True:
            self.screen.fill((186, 209, 245))
            # placing all the words
            self.font = pygame.font.Font('fonts/QuinqueFive.ttf', 15)
            word = "GAME OVER - Press Spacebar"
            end = self.font.render(word, True, (230, 230, 230))
            img_rect = end.get_rect()
            img_rect.center = self.screen.get_rect().center
            self.screen.blit(end, img_rect)
            word = "'If you ignore the red flags, embrace the heartache to come'"
            self.font = pygame.font.Font('fonts/QuinqueFive.ttf', 10)
            img = self.font.render(word, True, (20, 20, 20))
            img_rect = img.get_rect()
            img_rect.midbottom = self.screen.get_rect().midbottom
            self.screen.blit(img, img_rect)
            self.font = pygame.font.Font('fonts/QuinqueFive.ttf', 15)
            img = self.font.render(f"Score: {int(self.player.score_value)}", True, (20, 20, 20))
            img_rect = img.get_rect()
            img_rect.midtop = self.screen.get_rect().midtop
            self.screen.blit(img, img_rect)

            bestScore = self.font.render(f"Best Score: {str(self.updateFile())}", True, (230, 230, 230))
            self.screen.blit(bestScore, ((self.settings.screen_width/2) - 105, (self.settings.screen_height/2) + 55))

            self.font = pygame.font.Font('fonts/QuinqueFive.ttf', 27)

            pygame.display.flip()
            # respond to the key presses to restart
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        sys.exit()
                    if event.key == pygame.K_SPACE:
                        # restart the screen
                        self.flags.empty()
                        self.ghosts.empty()
                        self.battery.empty()
                        self.lightning.empty()

                        self.stats.hearts_left = 3
                        self.life.update(self.stats.hearts_left)
                        self.player.score_value = 0

                        return 0

    def _player_gain(self):
        """Respond to powerup"""
        if self.stats.hearts_left >= 0:
            restart_sfx = pygame.mixer.Sound('sounds/Balloon Pop 1.wav')
            restart_sfx.play()

            self.flags.empty()
            self.ghosts.empty()
            self.battery.empty()
            self.lightning.empty()
            self.player.score_value += 3

    def _player_gain_health(self):
        """Respond to battery powerup"""
        restart_sfx = pygame.mixer.Sound('sounds/Fruit collect 1.wav')
        restart_sfx.play()
        self.battery.empty()
        if 0 <= self.stats.hearts_left < 1:
            self.stats.hearts_left += 1
            self.life.update(self.stats.hearts_left)
        elif 1 <= self.stats.hearts_left < 2:
            self.stats.hearts_left += 1
            self.life.update(self.stats.hearts_left)
        elif 2 <= self.stats.hearts_left < 3:
            self.stats.hearts_left += 1
            self.life.update(self.stats.hearts_left)
        self.player.score_value += 3

    def updateFile(self):
        #Save scores from the game
        # have the text file and open it
        f = open('scores.txt')
        file = f.readlines()
        last = int(file[0])
        score = int(self.player.score_value)

        if last < int(score):
            f.close()
            file = open('scores.txt', 'w')
            file.write(str(score))
            file.close()

            return score
        return last

    def _update_screen(self):
        """Update images on the screen"""
        # make the background screen
        self.screen.blit(self.bg, self.bg.get_rect())

        # show how many lives
        self.life.blitme()
        # add the score
        img = self.font.render(f"Score: {int(self.player.score_value)}", True, (214, 58, 56))
        self.screen.blit(img, (50, 75))

        self.flags.draw(self.screen)
        self.ghosts.draw(self.screen)
        self.lightning.draw(self.screen)
        self.battery.draw(self.screen)
        # insert the player
        self.player.blitme()

        pygame.display.flip()
game_state = 0

heart_game = HeartGame()
heart_game.run_game()
    # Make a game instance and run it
