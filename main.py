from items import *
import os


class Game:
    def __init__(self):
        os.environ[OS_ENVIRON] = "1"
        pygame.init()
        pygame.display.set_caption(GAME_TITLE)
        self.screen = pygame.display.set_mode(
            (X_APPLICATION_SIZE, Y_APPLICATION_SIZE))
        self.scores = [0] * NUMBER_OF_PLAYERS
        # Init items.
        self.total_game_time = None
        self.players = None
        self.crossovers = None
        self.score_points = None
        self.items = None
        self.drawable = None

        self.init_items()

    def run(self):
        # Init Environment
        while True:
            self.total_game_time.tick()

            # Handle events.
            for event in pygame.event.get():
                # Check quit keys.
                if event.type == QUIT \
                        or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    pygame.quit()
                    return

                # Check if key is pressed.
                if event.type != KEYDOWN:
                    continue

                for item in self.players:
                    item.handle_key(event.key)

            # Update items.
            for item in self.drawable:
                item.update_position()

            # Check collisions.
            for item_1 in self.items:
                for item_2 in self.items:
                    if item_1 != item_2:
                        item_1.interact_with_other_item(item_2)

            # Reset screen.
            self.screen.fill(WHITE)

            # Lines around board.
            pygame.draw.line(self.screen, BLACK, (0, Y_BOARD_SIZE),
                             (X_APPLICATION_SIZE, Y_BOARD_SIZE), LINE_WIDTH)

            # Draw items.
            for item in self.drawable:
                item.draw(self.screen)

            print_scores(self.players, self.scores, self.screen)

            # Check if players are live.
            if any(not player.live for player in self.players):
                # Add score for live players.
                for i in range(NUMBER_OF_PLAYERS):
                    if self.players[i].live:
                        self.scores[i] += 10

                pygame.time.wait(2000)

                # Init items.
                self.init_items()

            # Update the full display Surface to the screen.
            pygame.display.flip()

            # Refresh rate setting.
            pygame.time.wait(REFRESH_RATE)

    def init_items(self):
        self.total_game_time = Timer()
        self.players = init_players()
        self.crossovers = init_crossovers(self.players, self.scores,
                                          self.total_game_time)
        self.score_points = init_score_points(self.players, self.scores,
                                              self.total_game_time)

        self.items = self.players + self.crossovers + self.score_points
        self.drawable = self.players + self.crossovers + self.score_points


if __name__ == "__main__":
    game = Game()
    game.run()
