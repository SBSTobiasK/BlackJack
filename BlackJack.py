import random, os, time

deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, "B", "D", "K", "A"]*4
random.shuffle(deck)
player1 = []
dealer = []
gameon = True

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
    if player1.count("B") == 1 and player1.count("A") == 1:
        print("Black Jack!")
        break
    morecards = input("(s)tay/(h)it/s(u)rrender? ")
    if morecards == "h":
        drawcard(player1)
        if (checksum(player1)) > 21:
            showboard()
            print("Busted! ", (checksum(player1)))
            gameon = False
            break
    elif morecards == "s":
        break
    elif morecards == "u":
        gameon = False
        break
    showboard()

while checksum(dealer) < 17 and gameon:
    drawcard(dealer)
    showboard()
    time.sleep(1)

if checksum(dealer) > 21:
    print("Casino busted! Sie haben gewonnen!")
elif checksum(dealer) > checksum(player1) or gameon == False:
    print("Das Casino gewinnt.")
elif checksum(dealer) == checksum(player1):
    print("Draw.")
else:
    print("Sie haben gewonnen!")


