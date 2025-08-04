import pygame
from os.path import join

class Player_Hand(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.image.load(join('images','player_in_play_sized.png')).convert_alpha()
        self.rect = self.image.get_frect(bottomleft = (20, WINDOW_HEIGHT-20))



class Fate_Hand(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.image.load(join('images','fate_sized.png')).convert_alpha()
        self.rect = self.image.get_frect(bottomright = (WINDOW_WIDTH-20, WINDOW_HEIGHT-20))


class Card(pygame.sprite.Sprite):
    def __init__(self, name, value, groups):
        super().__init__(groups)
        self.image = pygame.image.load(join('images', str(value + 1)  + '_' + name + '.png')).convert_alpha()
        self.rect = self.image.get_frect(topleft = (90*value,20))
        self.value = value




WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 820

# COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (13, 153, 255)
YELLOW = (249, 200, 49)

CARDS = {
    names : ['the_magician', 'the_high_priestess', 'the_empress', 'the_emperor', 'the_hierophant', 'the_lovers',
         'the_chariot', 'strength', 'the_hermit', 'the_wheel_of_fortune', 'justice', 'the_hanged_man',
         'death', 'temperance', 'the_devil', 'the_tower', 'the_star', 'the_moon', 'the_sun',
         'judgement', 'the_world', 'the_fool', 'the_soul'],
    values : [n for n in range(1, 24)]
}

# general setup
pygame.init()
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Game of Fate')
pygame.display.set_icon(pygame.image.load(join('images','icon.png')))
running = True
clock = pygame.time.Clock()


all_sprites = pygame.sprite.Group()
# card = Card(all_sprites)
deck = []
for card in CARDS:
    deck.append(Card(card, CARDS.index(card), all_sprites))
player_hand = Player_Hand(all_sprites)
fate_hand = Fate_Hand(all_sprites)

print(deck)


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
    all_sprites.draw(display_surface)
    pygame.display.update()

pygame.quit()