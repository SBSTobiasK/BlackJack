import random, os, time
def init_game():
    global deck
    deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, "B", "D", "K", "A"]*4
    random.shuffle(deck)
    global player1
    player1 = []
    global dealer
    dealer = []
    global gameon
    gameon = True
    global weitermachen
    weitermachen = True
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
    if count > 21:
        if (count - user.count("A")*10) < 21:
            count = count - user.count("A")*10
    return count

def showboard():
    os.system('cls')
    print("Kredits: ", kredit)
    print("Dealer:", dealer)
    print("Player: ", player1)

def showboard_with_count():
    os.system('cls')
    print("Kredits: ", kredit)
    print("Dealer:", dealer, checksum(dealer))
    print("Player: ", player1, checksum(player1))

weitermachen = True
kredit = 10

while weitermachen == True and kredit > 0:
    init_game()

    drawcard(player1)
    drawcard(player1)
    drawcard(dealer)
    showboard()

    while True:
        if player1.count("B") == 1 and player1.count("A") == 1:
            print("Black Jack!")
            kredit +=2
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
        time.sleep(3)

    showboard_with_count()

    if checksum(dealer) > 21:
        print("Casino busted! Sie haben gewonnen!")
        kredit += 1
    elif checksum(dealer) > checksum(player1) or gameon == False:
        print("Das Casino gewinnt.")
        kredit -=1
    elif checksum(dealer) == checksum(player1):
        print("Draw.")
    else:
        print("Sie haben gewonnen!")
        kredit += 1
    userinput = input("Noch eine Runde? (j/n): ")
    if userinput == "j":
        weitermachen = True
    else:
        weitermachen = False

if kredit < 1:
    print("Schade, Sie haben kein Geld mehr.")
else:
    print("Schade, dass sie schon aufhören möchten.")