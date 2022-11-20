"RPS game"
import random

def get_choices():
    player_choice = input("Enter a choice: ")
    options = ["rock", "paper", "scissor"]
    computer_choice = random.choice(options)
    choices = { "player":player_choice, "computer": computer_choice }
    return choices

def check_win(player, computer):
    print(f"You choose {player}, computer choose {computer}")
    if player == computer:
        return "It's a tie!"
    elif player == 'rock':
        if computer == 'scissor':
            return "Rock smashes scissors! You win!"
        else :
            return "Paper covers rock! You lose."
    elif player == 'paper':
        if computer == 'scissor':
            return "Scissor cuts paper! You lose!"
        else :
            return "Paper covers rock! You win."
    elif player == 'scissor':
        if computer == 'paper':
            return "Scissor cuts paper! You win!"
        else :
            return "Rock smashes scissors! You lose!"
   
choices = get_choices()
result = check_win(choices["player"], choices["computer"])

print(result)





