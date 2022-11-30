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

#Give players names

for x in range(number_of_players):
    player_name_input = input("Name?: ")
    table1.addPlayer(player_name_input)
    table1.players[x] = Player()
    table1.players[x].setupPlayer(player_name_input)
    table1.players[x].setHands("A")
    print(table1.players[x])

for x in range(number_of_players):
    outputname =  table1.players[x]
    print(outputname.getPlayername())
    print(outputname.getHands())




#Start of Game
#Players draw Cards
#Dealer draws Card
#Check for Blackjack
