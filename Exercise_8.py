p1 = ""
p2 = ""

while True:
    p1 = input("Player 1 enter your play: ")
    p2 = input("Player 2 enter your play: ")
    if p1 == "Rock" and p2 == "Scissors":
        print("Player 1 wins!")
        break
    elif p1 == "Scissors" and p2 == "Paper":
        print("Player 1 wins!")
        break
    elif p1 == "Paper" and p2 == "Rock":
        print("Player 1 wins!")
        break
    elif p2 == "Rock" and p1 == "Scissors":
        print("Player 2 wins!")
        break
    elif p2 == "Scissors" and p1 == "Paper":
        print("Player 2 wins!")
        break
    elif p2 == "Paper" and p1 == "Rock":
        print("Player 2 wins!")
        break