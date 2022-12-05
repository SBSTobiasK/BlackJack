players = []
user_input = "leer"

def create_players(players):
    for player in players:
        player = []

while user_input != "":
    user_input = input("Geben sie einen Spielernamen ein: ")
    if user_input != "":
        players.append(user_input)

print(players)
create_players(players)
