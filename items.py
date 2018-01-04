from params import *
import random
import pygame


class Timer:
    def __init__(self):
        self.gameClock = pygame.time.Clock()
        self.time = 0

    def get_time(self):
        return self.time

    def tick(self):
        self.gameClock.tick()
        self.time += self.gameClock.get_time()


class Drawable:
    def __init__(self):
        self.colour = (0, 0, 0)
        self.head = [0, 0]
        self.live = True

    def set_colours(self, colour):
        self.colour = colour

    def set_head_position(self, head):
        self.head = head

    def update_position(self):
        pass

    def draw(self, screen):
        if self.live:
            screen.fill(self.colour,
                        (self.head[0], self.head[1], DOT_SIZE, DOT_SIZE))


class KeySensitive:
    def __init__(self):
        self.keys = []
        pass

    def set_keys(self, keys):
        self.keys = keys

    def handle_key(self, key):
        pass


class ActivePoint(Drawable):
    def __init__(self):
        Drawable.__init__(self)
        self.live = False
        self.frequency = 0
        self.last_active = 0
        self.players = []
        self.scores = []
        self.total_time = None

    def set_frequency(self, frequency):
        self.frequency = frequency

    def set_players(self, players):
        self.players = players

    def set_scores(self, scores):
        self.scores = scores

    def set_total_time(self, total_time):
        self.total_time = total_time

    def update_position(self):
        assert (self.total_time is not None)

        time_delta = self.total_time.get_time() - self.last_active
        if not self.live and time_delta > self.frequency:
            self.live = True
            self.head = random_point()

            while any(True for player in self.players if
                      self.head in player.body):
                self.head = random_point()


class Item:
    def __init__(self):
        pass

    def interact_with_other_item(self, other_item):
        pass


class Crossover(ActivePoint, Item):
    def __init__(self):
        ActivePoint.__init__(self)
        Item.__init__(self)

    def interact_with_other_item(self, other_item):
        if other_item.__class__ == Player:
            if other_item.head == self.head and self.live:
                other_item.crossovers += 1
                self.last_active = self.total_time.get_time()
                self.live = False


class ScorePoint(ActivePoint, Item):
    def __init__(self):
        ActivePoint.__init__(self)
        Item.__init__(self)

    def interact_with_other_item(self, other_item):
        if other_item.__class__ == Player:
            if other_item.head == self.head and self.live:
                self.scores[self.players.index(other_item)] += 2
                self.last_active = self.total_time.get_time()
                self.live = False


class Player(object, Drawable, KeySensitive, Item):
    def __init__(self):
        Drawable.__init__(self)
        KeySensitive.__init__(self)

        self.body = []
        self.direction = (DOT_SIZE, 0)
        self.crossovers = 0

    def handle_key(self, key):
        if key not in self.keys:
            return self.direction
        self.direction = DIRECTIONS[self.keys.index(key)]

    def interact_with_other_item(self, other_item):
        if other_item.__class__ == Player:
            if other_item.head in self.body:
                other_item.crossovers -= 1
                other_item.live = (other_item.crossovers >= 0)

            # Both players dies.
            if self.head == other_item.head:
                self.live = False
                other_item.live = False

    def update_position(self):
        self.body.append(self.head)
        self.head = [self.head[0] + self.direction[0],
                     self.head[1] + self.direction[1]]

        if (not 0 <= self.head[0] < X_BOARD_SIZE or not 0 <= self.head[
            1] < Y_BOARD_SIZE) \
                or self.head in self.body:
            self.live = False
            return

    def draw(self, screen):
        super(Player, self).draw(screen)

        for body_element in self.body:
            screen.fill(self.colour,
                        (body_element[0], body_element[1], DOT_SIZE, DOT_SIZE))


#########################################################
#                    Helper functions                   #


def random_point():
    return [normalize(random.randrange(0, X_BOARD_SIZE)),
            normalize(random.randrange(0, Y_BOARD_SIZE))]


def init_players():
    players = [Player() for _ in range(NUMBER_OF_PLAYERS)]
    for player, colour, controller, start_position in zip(
            players, COLOURS, CONTROLLERS, START_POSITIONS):
        player.set_colours(colour)
        player.set_keys(controller)
        player.set_head_position(start_position)
    return players


def init_crossovers(players, scores, total_time):
    crossovers = [Crossover() for _ in range(NUMBER_OF_CROSSOVERS)]
    for crossover in crossovers:
        crossover.set_colours(CROSSOVER_COLOUR)
        crossover.set_frequency(FREQUENCY_CROSSOVER)
        crossover.set_players(players)
        crossover.set_scores(scores)
        crossover.set_total_time(total_time)
    return crossovers


def init_score_points(players, scores, total_time):
    score_points = [ScorePoint() for _ in range(NUMBER_OF_SCORE_POINTS)]
    for score_point in score_points:
        score_point.set_colours(SCORE_POINT_COLOUR)
        score_point.set_frequency(FREQUENCY_SCORE_POINT)
        score_point.set_players(players)
        score_point.set_scores(scores)
        score_point.set_total_time(total_time)
    return score_points


def print_scores(players, scores, screen):
    text_to_display = prepare_text(players, scores)
    default_font = pygame.font.Font(pygame.font.get_default_font(),
                                    FONT_SIZE_1)

    rendered_text = [default_font.render(text, 1, BLACK, BACKGROUND_SCORES)
                     for text in text_to_display]
    distance = SECTION_HEIGHT / len(rendered_text)
    for text, y in zip(rendered_text,
                       xrange(Y_BOARD_SIZE + LINE_WIDTH, Y_APPLICATION_SIZE,
                              distance)):
        screen.blit(text, (0, y))


def prepare_text(players, scores):
    to_display_data = [(-score, player.crossovers, "Player_{}".format(index))
                       for player, score, index in
                       zip(players, scores, xrange(1, 5))]
    to_display_data.sort()
    return ["{}   Score {}                  Crossovers {}".format(
        player_name, -score, crossover)
        for (score, crossover, player_name) in to_display_data]
