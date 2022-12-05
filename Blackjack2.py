from Game import Player
from Game import Board

#Ask for number of players
def inputspieler():
        while True:
            user_input_players = input("Wieviele Spieler möchten mitspielen? (1-5): ")
            try:
                user_input_players = int(user_input_players)
            except:
                continue
            if int(user_input_players) >=1 and int(user_input_players) <= 5:
                    break
        return user_input_players

table1 = Board()
number_of_players = inputspieler()

for x in range(number_of_players):
    user_name = input("Name: ")
    user_name = Player(user_name)
    print(user_name.getPlayername())
    table1.addPlayer(user_name)
    player = table1.getPlayer(x)
    print(player.getPlayername())


#Give players names
#Start of Game
#Players draw Cards
#Dealer draws Card
#Check for Blackjack