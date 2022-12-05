
import pygame
import button

pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Main Menu")

game_paused = False
menu_state = "main"

font = pygame.font.SysFont("aerialblack", 40)

TEXT_COL = (255,255,255)

bkg_menu_img = pygame.image.load("images/Item3.png").convert_alpha()
play_img = pygame.image.load("images/Icon_Tube.png").convert_alpha()
options_img = pygame.image.load("images/Icon_Menu.png").convert_alpha()
quit_img = pygame.image.load("images/Icon_Exit.png").convert_alpha()
ask_img = pygame.image.load("images/Icon_Question.png").convert_alpha()
restart_img = pygame.image.load("images/Icon_Return.png").convert_alpha()

bkg_button = button.Button(250, 50, bkg_menu_img, 1)
play_button = button.Button(475, 150, play_img, 1)
options_button = button.Button(335, 325, options_img, 1)
quit_button = button.Button(610, 325, quit_img, 1)
ask_button = button.Button(500, 225, ask_img, 1)
restart_button = button.Button(485, 325, restart_img, 1)

def draw_text(text, font, text_col, x, y):
    """Render the text"""
    img = font.render(text,True, text_col)
    screen.blit(img, (x,y))

run = True
while run:
    screen.fill((52,78,91))

    if game_paused == True:
        if menu_state == "main":
            bkg_button.draw(screen)

            if play_button.draw(screen):
                break
            elif options_button.draw(screen):
                menu_state = "options"
            elif quit_button.draw(screen):
                run = False
            elif restart_button.draw(screen):
                print("Restart game")
        if menu_state == "options":
            # draw the different options buttons
            bkg_button.draw(screen)
            if ask_button.draw(screen):
                print("Test")
    else:
        draw_text("Press SPACE to pause", font, TEXT_COL, 250, 255)


    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_paused = True
            elif event.key == pygame.K_q:
                run = False
            elif event.key == pygame.QUIT:
                run = False
    pygame.display.update()
pygame.quit()