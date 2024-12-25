import random

def get_computer_choice():

    #Function to get the computer's choice.
    return random.choice(['Snake', 'Water', 'Gun'])

def determine_winner(user_choice, computer_choice):
    #Function to determine the winner.
    if user_choice == computer_choice:
        return "It's a tie!"
    
    # Define win conditions
    if (user_choice == 'Snake' and computer_choice == 'Water') or \
       (user_choice == 'Water' and computer_choice == 'Gun') or \
       (user_choice == 'Gun' and computer_choice == 'Snake'):
        
        return "You win!"
    
    return "Computer wins!"

def play_game():
    #Function to play the Snake, Water, Gun game.
    print("Welcome to the Snake, Water, Gun game!")
    user_choice = input("Enter your choice (Snake, Water, Gun): ").capitalize()

    if user_choice not in ['Snake', 'Water', 'Gun']:
        print("Invalid choice! Please select from Snake, Water, or Gun.")
        return

    computer_choice = get_computer_choice()
    print(f"Computer chose: {computer_choice}")
    
    result = determine_winner(user_choice, computer_choice)
    print(result)

if __name__ == "__main__":
    play_game()
