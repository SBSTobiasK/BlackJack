class Player:
    __name = ""
    __kredits = ""
    __Hands = []

    def setupPlayer(self, name):
        self.__name = name
        self.__kredits = 10

    def getPlayername(self):
        return self.__name

    def setKredit(self, kredit):
        self.__kredits += kredit

    def getKredits(self):
        return self.__kredits

    def getHands(self):
        return self.__Hands