import sys
import random

wins = 0
ties = 0
losses = 0
rounds_played = 0

def switch_case(a, b, c):
    global wins
    global ties
    global losses
    global rounds_played
    if computer_move == a:
        ties += 1
        rounds_played += 0
        return "Its a tie"
    elif computer_move == b:
        wins += 1
        rounds_played += 1
        return "You win this round"    
    elif computer_move == c:
        losses += 1
        rounds_played += 1
        return"You lose this round"
                
while True:
    while True:
        print(f"ROUNDS PLAYED:{rounds_played}   WINS-{wins}   LOSSES-{losses}   TIES-{ties}")
        print("enter move; R for rock P for paper S for scissors.\nTo quit enter Q")
        player_move = input(">>>").lower()
        match player_move:
            case "q":
                print(f"ROUNDS PLAYED:{rounds_played}   WINS-{wins}   LOSSES-{losses}   TIES-{ties}")
                sys.exit("Thanks for playing, bye.")
            case "r"|"p"|"s":
                break
            case _:
                print("Invalid entry!!")
                continue

    random_numbers = random.randint(1, 3)
    match random_numbers:
        case 1:
            computer_move = "r"
        case 2:
            computer_move = "p"
        case 3:
            computer_move = "s"

    if player_move == "r":
        print(switch_case("r", "s", "p"))

    elif player_move == "p":
        print(switch_case("p", "r", "s"))
        
    elif player_move == "s":
        print(switch_case("s", "p", "r"))
    
    if rounds_played == 5:
        print(f"ROUNDS PLAYED:{rounds_played}   WINS:{wins}   LOSSES-{losses}   TIES:{ties}")
        if wins > losses:
            sys.exit("YOU WIN!!!!")
        else:
            sys.exit("Computer wins.....")
