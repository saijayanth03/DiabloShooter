import pygame
import button

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

BG = pygame.image.load("assets/i01_background.png")

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Main Menu")

game_paused = False
menu_state = "main"

font = pygame.font.SysFont("arialblack", 40)
font2 = pygame.font.SysFont("unique", 60)

TEXT_COL = (255, 255, 255)

start_img = pygame.image.load("assets/start.png").convert_alpha()
options_img = pygame.image.load("assets/options.png").convert_alpha()
quit_img = pygame.image.load("assets/quit.png").convert_alpha()
atlantis_img = pygame.image.load("assets/atlantis.png").convert_alpha()
space_img = pygame.image.load("assets/space.png").convert_alpha()
superhero_img = pygame.image.load("assets/superhero.png").convert_alpha()
rome_img = pygame.image.load("assets/rome.png").convert_alpha()
easy_img = pygame.image.load("assets/easy.png").convert_alpha()
medium_img = pygame.image.load("assets/medium.png").convert_alpha()
hard_img = pygame.image.load("assets/hard.png").convert_alpha()

options_button = button.Button(304, 250, options_img, 1)
quit_button = button.Button(325, 375, quit_img, 1)
start_button = button.Button(325, 150, start_img, 1)
atlantis_button = button.Button(225, 250, atlantis_img, 1)
space_button = button.Button(25, 250, space_img, 1)
superhero_button = button.Button(425, 250, superhero_img, 1)
rome_button = button.Button(625, 250, rome_img, 1)
easy_button = button.Button(325, 125, easy_img, 1)
medium_button = button.Button(325, 250, medium_img, 1)
hard_button = button.Button(325, 375, hard_img, 1)


def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


run = True
while run:
    screen.fill((52, 78, 91))
    screen.blit(BG, (0, 0))

    if game_paused == True:

        if menu_state == "main":
            if start_button.draw(screen):
                menu_state = "Start"
            if quit_button.draw(screen):
                run = False

        if menu_state == "Start":
            if rome_button.draw(screen):
                print("rome")
                menu_state = "rome"
            if atlantis_button.draw(screen):
                print("atlantis")
                menu_state = "atlantis"
            if space_button.draw(screen):
                print("space")
                menu_state = "space"
            if superhero_button.draw(screen):
                print("superhero")
                menu_state = "superhero"

        if menu_state == "rome":
            if easy_button.draw(screen):
                print("easy")
                import easyrome.py
            if medium_button.draw(screen):
                print("medium")
                import mediumrome.py
            if hard_button.draw(screen):
                print("hard")
                import hardrome.py

        if menu_state == "atlantis":
            if easy_button.draw(screen):
                print("easy")
                import easyatlantis.py
            if medium_button.draw(screen):
                print("medium")
                import mediumatlantis.py
            if hard_button.draw(screen):
                print("hard")
                import hardatlantis.py


        if menu_state == "space":
            if easy_button.draw(screen):
                print("easy")
                import easyspace.py
            if medium_button.draw(screen):
                print("medium")
                import mediumspace.py
            if hard_button.draw(screen):
                print("hard")
                import hardspace.py

        if menu_state == "superhero":
            if easy_button.draw(screen):
                print("easy")
            if medium_button.draw(screen):
                print("medium")
            if hard_button.draw(screen):
                print("hard")




    else:
        draw_text("PRESS SPACE TO PLAY", font, TEXT_COL, 160, 300)
        draw_text("DIABLO", font2, TEXT_COL, 320, 100)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_paused = True
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()