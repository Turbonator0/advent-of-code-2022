x = 1
y = 2
z = 3

# A = Rock
# B = Paper
# C = Scissors
score = 0

def playerWins(opponent: str, player: str) -> bool:
    global score
    if (player == "X" and opponent == "A") or (player == "Y" and opponent == "B") or (player == "Z" and opponent == "C"):
        score += 3
        return False
    elif player == "X" and opponent == "B":
        return False
    elif player == "X" and opponent == "C":
        return True
    elif player == "Y" and opponent == "A":
        return True
    elif player == "Y" and opponent == "C":
        return False
    elif player == "Z" and opponent == "A":
        return False
    elif player == "Z" and opponent == "B":
        return True

with open("input") as f:
    for line in f.readlines():

        moves = line.split(" ")
        opponent = moves[0]
        player = moves[1].strip("\n")
        #print(player)
        print(player)
        match player:
            case "X":
                score += 1
            case "Y":
                score += 2
            case "Z":
                score += 3
        if playerWins(opponent, player):
            score += 6
        else:
            ...
        print(score)
print(score)