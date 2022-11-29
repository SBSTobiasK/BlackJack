from Setup import Player

players = []

for x in range(2):
    user_input = input("Name: ")
    players.append(user_input)
    players[x] = Player()
    players[x].setupPlayer(user_input)

for x in range(2):
    print(players[x].getPlayername())
    print(players[x].getKredits())
    print(players[x].getHands())
