from pygame.locals import *

#########################################################
#                    BOARD SIZE                         #

# Must be positive
DOT_SIZE = 12


def normalize(x):
    return (x / DOT_SIZE) * DOT_SIZE


X_BOARD_SIZE = 1080
Y_BOARD_SIZE = 732

assert (X_BOARD_SIZE % DOT_SIZE == 0)
assert (Y_BOARD_SIZE % DOT_SIZE == 0)

LINE_WIDTH = 4
SECTION_HEIGHT = 102 + LINE_WIDTH

X_APPLICATION_SIZE = X_BOARD_SIZE
Y_APPLICATION_SIZE = Y_BOARD_SIZE + SECTION_HEIGHT

#########################################################
#                    ADDITIONAL PARAMS                  #

GAME_TITLE = "TRON Simulator"
OS_ENVIRON = "SDL_VIDEO_CENTERED"
REFRESH_RATE = 100
BACKGROUND_SCORES = (255, 255, 204)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
FONT_SIZE_1 = 25
FONT_SIZE_2 = 70

#########################################################
#                    ITEMS PARAMS                       #


NUMBER_OF_PLAYERS = 2
COLOURS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (148, 0, 211)]
CONTROLLERS = [[K_UP, K_DOWN, K_LEFT, K_RIGHT],
               [K_w, K_s, K_a, K_d],
               [K_f, K_v, K_c, K_b],
               [K_i, K_k, K_j, K_l]]
START_POSITIONS = [[normalize(X_BOARD_SIZE / 3), normalize(Y_BOARD_SIZE / 3)],
                   [normalize(2 * X_BOARD_SIZE / 3), normalize(2 * Y_BOARD_SIZE / 3)],
                   [normalize(X_BOARD_SIZE / 3), normalize(2 * Y_BOARD_SIZE / 3)],
                   [normalize(2 * X_BOARD_SIZE / 3), normalize(Y_BOARD_SIZE / 3)]]

assert (all(position[0] % DOT_SIZE == 0 and position[1] % DOT_SIZE == 0
            for position in START_POSITIONS))

# Directions for players
UP = (0, -DOT_SIZE)
DOWN = (0, DOT_SIZE)
LEFT = (-DOT_SIZE, 0)
RIGHT = (DOT_SIZE, 0)
DIRECTIONS = [UP, DOWN, LEFT, RIGHT]

NUMBER_OF_CROSSOVERS = 2
CROSSOVER_COLOUR = (192, 192, 192)
FREQUENCY_CROSSOVER = 2000

NUMBER_OF_SCORE_POINTS = 2
SCORE_POINT_COLOUR = (255, 128, 0)
FREQUENCY_SCORE_POINT = 6000

#########################################################
