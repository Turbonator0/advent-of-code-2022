x = 1
y = 2
z = 3

# A = Rock
# B = Paper
# C = Scissors
score = 0
"""
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
"""
def makeMove(player: str, opponent: str, score: int) -> int:
    if player == "X": # have to lose
        match opponent:
            case "A": # opponent has rock
                score += z
            case "B": # opponent has paper
                score += x
            case "C": # opponent has scissors
                score += y
    elif player == "Y": # have to draw
        match opponent:
            case "A": # opponent has rock
                score += x
            case "B": # opponent has paper
                score += y
            case "C": # opponent has scissors
                score += z
    elif player == "Z": # have to win
        match opponent:
            case "A": # opponent has rock
                score += y
            case "B": # opponent has paper
                score += z
            case "C": # opponent has scissors
                score += x
    return score
with open("input") as f:
    for line in f.readlines():

        moves = line.split(" ")
        opponent = moves[0]
        player = moves[1].strip("\n")
        #print(player)
        print(player)
        match player:
            case "X":
                score += 0
                #score += makeMove(player, opponent, score)
            case "Y":
                score += 3
            case "Z":
                score += 6
        score = makeMove(player, opponent, score)
print(score)