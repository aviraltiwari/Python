from random import randint


def computer_turn():
    comp_hand = randint(1, 3)
    if comp_hand == 1:
        compval = "rock"
    elif comp_hand == 2:
        compval = "paper"
    else:
        compval = "scissor"
    return compval


def game_start():
    playing = True
    you = 0
    comp = 0
    tie = 0
    while playing:
        print("Enter 'rock' 'paper' 'scissor' 'quit'")
        your_hand = input()

        your_hand = your_hand.lower()

        if your_hand == 'rock' or your_hand == 'paper' or your_hand == 'scissor':
            c = computer_turn()
            if your_hand == c:
                print("It's a tie! You = " + your_hand + " Comp = " + c)
                tie = tie + 1
            elif (your_hand == "rock" and c == "scissor") or (your_hand == "paper" and c == "rock") or (
                            your_hand == "scissor" and c == "paper"):
                print("You win! You = " + your_hand + " Comp = " + c)
                you = you + 1
            else:
                print("You lost! You = " + your_hand + " Comp = " + c)
                comp = comp + 1
        elif your_hand == 'quit':
            print("thanks for playing")
            print("Here's the score! You = %d Computer = %d Tie = %d " % (you,comp,tie))
            playing = False
        else:
            print("Invalid!")



game_start()
