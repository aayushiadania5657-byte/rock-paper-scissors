# game using functions
import random

print("🎮 Welcome to Rock, Paper and Scissors 🫡")
print("Rules of the game:")
print("Rock beats Scissors")
print("Scissors beats Paper")
print("Paper beats Rock")

choices = ("rock", "paper", "scissor")

def get_computer_choice():
    return random.choice(choices)
    
def check_winner(user_choice,computer_choice):
    if user_choice == computer_choice:
        return "draw😐"

    elif user_choice == "rock" and computer_choice == "scissor":
        return "user_win🎉"

    elif user_choice == "scissor" and computer_choice == "paper":
        return "user_win🎉"
        

    elif user_choice == "paper" and computer_choice == "rock":
        return "user_win🎉"

    else:  
        return "computer_win🤖"
chance =0 
user_win = 0
computer_win = 0
draw = 0
while chance < 3:
    user_choice=input("Enter your choice:").lower()
    if user_choice not in choices:
        print("Not a valid choice")
        continue
    computer_choice = get_computer_choice()
    result = check_winner(user_choice, computer_choice)
    print("computer_choice: ",computer_choice)
    print(result)
    if result == "user_win🎉":
        user_win +=1
    elif result == "computer_win🤖":
        computer_win +=1
    else:
        draw+=1
    chance += 1
print("\n🏆 FINAL RESULT 🏆")
print("Your wins:", user_win)
print("Computer wins:", computer_win)
print("Draws:", draw)
print("Thanks for playing👋")

           