class Board:
    players = []
    dealer = []
    stack = [2, 3, 4, 5, 6, 7, 8, 9, 10, "B", "D", "K", "A"]*4

    def addPlayer(self, name):
        self.players.append(name)