import random

def play_game():
    choices = ["rock", "paper", "scissors"]
    user_score = 0
    computer_score = 0
    width = 40
    
    print("Welcome to Rock-Paper-Scissors!".center(width))
    
    while True:
        try:
            print(f"\n{'SCOREBOARD'.center(width, '-')}")
            print(f"You: {user_score} | Computer: {computer_score}".center(width))
            
            user_choice = input("\nEnter choice (rock/paper/scissors): ").strip().lower()

            if user_choice not in choices:
                print("Invalid choice. Try again.".rjust(width))
                continue

            computer_choice = random.choice(choices)
            print(f"You chose: {user_choice.upper()}".ljust(width//2) + f"CPU chose: {computer_choice.upper()}".rjust(width//2))

            if user_choice == computer_choice:
                print("RESULT: IT'S A TIE!".center(width))
            elif (user_choice == "rock" and computer_choice == "scissors") or \
                 (user_choice == "scissors" and computer_choice == "paper") or \
                 (user_choice == "paper" and computer_choice == "rock"):
                print("\n" + "-" * width)
                print("RESULT: YOU WIN!!".center(width))
                print("\n" + "-" * width)
                user_score += 1 
            else:
                print("\n" + "-" * width)
                print("RESULT: YOU LOSE!!".center(width))
                print("\n" + "-" * width)
                computer_score += 1 

            while True:
                play_again = input("\nDo you want to play again? (y/n): ".rjust(width-5)).lower().strip()
                if play_again in ['y', 'n']:
                    break
                print("Please enter 'y' or 'n'.".rjust(width))

            if play_again == 'n':
                print("\n" + "-" * width)
                print(f"FINAL SCORE -> You: {user_score} | CPU: {computer_score}".center(width))
                print("Thanks for playing!".center(width))
                print("-" * width)
                break

        except KeyboardInterrupt:
             print("\n\n" + "Game stopped. See you next time!".center(width))
             break
        except Exception as e:
            print(f"Error: {e}".center(width))

if __name__ == "__main__":
    play_game()