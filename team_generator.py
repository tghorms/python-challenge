# Random Two Man Golf Team Generator
from random import choice

players = ["Clay", "Kyle S.", "Justin",
             "DJ", "Nick", "Eric", 
             "Sean", "Kyle E.", "Max", "Jon", 
             "Keith", "Tommy" ]


print(players)

Team1 = []
Team2 = []
Team3 = []
Team4 = []
Team5 = []
Team6 = []

while len(players) > 0: 
    player1 = choice(players)
    print(player1)
    Team1.append(player1)
    players.remove(player1)
    print("Players left: ", players)

    player2 = choice(players)
    print(player2)
    Team2.append(player2)
    players.remove(player2)
    print("Players left: ", players)

    player3 = choice(players)
    print(player3)
    Team3.append(player3)
    players.remove(player3)
    print("Players left: ", players)

    player4 = choice(players)
    print(player4)
    Team4.append(player4)
    players.remove(player4)
    print("Players left: ", players)
    
    player5 = choice(players)
    print(player5)
    Team5.append(player5)
    players.remove(player5)
    print("Players left: ", players)

    player6 = choice(players)
    print(player6)
    Team6.append(player6)
    players.remove(player6)
    print("Players left: ", players)


print("--------------------------------")
print("Wolfy 2 Man Team, Par 3 Callenge")
print("--------------------------------")
print("Team 1: ", Team1)
print("Team 2: ", Team2)
print("Team 3: ", Team3)
print("Team 4: ", Team4)
print("Team 5: ", Team5)
print("Team 6: ", Team6)
