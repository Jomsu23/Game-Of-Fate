import pygame
from os.path import join

# class Player_Hand(pygame.sprite.Sprite):
#     def __init__(self, groups):
#         super().__init__(groups)




# class Fate_Hand(pygame.sprite.Sprite):
#     def __init__(self, groups):
#         super().__init__(groups)



class Card(pygame.sprite.Sprite):
    def __init__(self, name, value, groups):
        super().__init__(groups)
        self.image = pygame.image.load(join("images", str(value)  + "_" + name + ".png")).convert_alpha()
        self.rect = self.image.get_frect(topleft = INITIAL_POSITIONS[value-1])
        self.value = value



# WINDOW
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 820

# COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (13, 153, 255)
YELLOW = (249, 200, 49)

CARDS = ["the_magician", "the_high_priestess", "the_empress",           "the_emperor", "the_hierophant", "the_lovers", "the_chariot", "strength", "the_hermit", "the_wheel_of_fortune", "justice", "the_hanged_man", "death", "temperance", "the_devil", "the_tower", "the_star", "the_moon", "the_sun", "judgement", "the_world", "the_fool", "the_soul"]

CARDS_VALUE = {"the_magician" : 1,
          "the_high_priestess" : 2,
          "the_empress" : 3,
          "the_emperor" : 4,
          "the_hierophant" : 5,
          "the_lovers" : 6,
          "the_chariot" : 7,
          "strength" : 8,
          "the_hermit" : 9,
          "the_wheel_of_fortune" : 10,
          "justice" : 11,
          "the_hanged_man" : 12,
          "death" : 13,
          "temperance" : 14,
          "the_devil" : 15,
          "the_tower" :16,
          "the_star" : 17,
          "the_moon" : 18,
          "the_sun" : 19,
          "judgement" : 20,
          "the_world" : 21,
          "the_fool" : 22,
          "the_soul" : 23 }

INITIAL_POSITIONS = [(45,20), (145,20), (245,20), (345,20), (445,20), (545,20), (645,20), (745,20), (845,20), (945,20), (1045,20), (1145,20), (95,208), (195,208), (295,208), (395,208), (495,208), (595,208), (695,208), (795,208), (895,208), (995,208), (1095,208)]

# general setup
pygame.init()
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Game of Fate")
pygame.display.set_icon(pygame.image.load(join("images","icon.png")))
running = True
clock = pygame.time.Clock()



all_sprites = pygame.sprite.Group()
deck = []
for card in CARDS:
    deck.append(Card(card, CARDS_VALUE[card], all_sprites))


# Player corner
player_image = pygame.image.load(join("images","player_in_play_sized.png")).convert_alpha()
player_rect = player_image.get_frect(bottomleft = (20, WINDOW_HEIGHT-20))


# Fate corner
fate_image = pygame.image.load(join("images","fate_sized.png")).convert_alpha()
fate_rect = fate_image.get_frect(bottomright = (WINDOW_WIDTH-20, WINDOW_HEIGHT-20))




while running:
    dt = clock.tick() / 1000
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # update
    all_sprites.update()          


    # draw the game
    display_surface.fill(YELLOW)
    pygame.draw.rect(display_surface, BLACK, [50, WINDOW_HEIGHT-300, WINDOW_WIDTH/2-50-10, 270], 2)
    display_surface.blit(player_image, player_rect) 
    pygame.draw.rect(display_surface, BLACK, [WINDOW_WIDTH/2+10, WINDOW_HEIGHT-300, WINDOW_WIDTH/2-50-10, 270], 2)
    display_surface.blit(fate_image, fate_rect)
    all_sprites.draw(display_surface)
    pygame.display.update()

pygame.quit()