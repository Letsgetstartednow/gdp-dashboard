POINT_NAMES = ["Love", "15", "30", "40"]

class TennisGame:
    """Simple tennis game scoring logic.

    Keep track of points for two players and compute tennis scores
    like ``15 - Love`` or ``Advantage Player 1``. Once a player wins
    the game, the score is reported as ``Game <player>``.
    """

    def __init__(self, player1="Player 1", player2="Player 2"):
        self.player1 = player1
        self.player2 = player2
        self.points = {player1: 0, player2: 0}

    def point_won_by(self, player):
        if player not in self.points:
            raise ValueError("Unknown player: %s" % player)
        self.points[player] += 1

    def score(self):
        p1 = self.points[self.player1]
        p2 = self.points[self.player2]

        # Handle win
        if p1 >= 4 or p2 >= 4:
            if abs(p1 - p2) >= 2:
                winner = self.player1 if p1 > p2 else self.player2
                return f"Game {winner}"

        # Handle deuce/advantage situations
        if p1 >= 3 and p2 >= 3:
            if p1 == p2:
                return "Deuce"
            if p1 > p2:
                return f"Advantage {self.player1}"
            return f"Advantage {self.player2}"

        # Regular scoring
        return f"{POINT_NAMES[p1]} - {POINT_NAMES[p2]}"


def main():
    game = TennisGame()
    print("Willkommen zum Tennisspiel! Geben Sie ein, wer den Punkt gewinnt (1 oder 2).")
    while True:
        current = game.score()
        print("Aktueller Spielstand:", current)
        if current.startswith("Game"):
            break
        winner = input("Wer hat den Punkt gewonnen? (1/2): ")
        if winner == "1":
            game.point_won_by(game.player1)
        elif winner == "2":
            game.point_won_by(game.player2)
        else:
            print("Ungültige Eingabe, bitte 1 oder 2 eingeben.")


if __name__ == "__main__":
    main()
