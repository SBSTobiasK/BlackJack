class Player:
    name = ""
    kredits = ""
    Hands = []

    def setupPlayer(self, name):
        self.name = name
        self.kredits = 10

    def getPlayername(self):
        return self.name

    def getKredits(self):
        return self.kredits

    def getHands(self):
        return self.Hands