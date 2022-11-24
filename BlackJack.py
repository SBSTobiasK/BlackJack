import random

deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, "B", "D", "K", "A"]*4
player1 = []

random.shuffle(deck)

print(deck)

player1.append(deck.pop())
player1.append(deck.pop())

print(player1)
print(deck)

if player1.count("B") == 1 and player1.count("A") == 1:
    print("Black Jack!")