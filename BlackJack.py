import random, os

deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, "B", "D", "K", "A"]*4
random.shuffle(deck)
player1 = []
dealer = []

def drawcard(user):
    user.append(deck.pop())

def checksum(user):
    count = 0
    for a in user:
        if a == "B" or a == "D" or a == "K":
            count += 10
        elif a == "A":
            count += 11
        else:
            count += a
    return count

def showboard():
    os.system('cls')
    print("Dealer:", dealer)
    print("Player: ", player1)


drawcard(player1)
drawcard(player1)
drawcard(dealer)
showboard()

while True:
    morecards = input("(s)tay/(d)raw/s(u)rrender? ")
    if morecards == "d":
        drawcard(player1)
    elif morecards == "s":
        break
    elif morecards == "u":
        break
    showboard()
    print(checksum(player1))


if player1.count("B") == 1 and player1.count("A") == 1:
    print("Black Jack!")