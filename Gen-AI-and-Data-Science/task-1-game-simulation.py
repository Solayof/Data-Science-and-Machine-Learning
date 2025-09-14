import random

def play_game():
    """
    This function contains the main logic for the Rock, Paper, Scissors game.
    It simulates a game between the user and the computer.
    """

    # Define the possible choices for the game
    choices = ['rock', 'paper', 'scissors']

    # Start a loop that continues until the user decides to stop
    while True:
        # Get the user's choice. Convert the input to lowercase for consistency.
        user_choice = input("Enter a choice (rock, paper, scissors): ").lower()

        # Validate the user's input to make sure it's a valid choice
        if user_choice not in choices:
            print("Invalid choice. Please choose from rock, paper, or scissors.")
            continue  # Restart the loop to ask for input again

        # Generate a random choice for the computer from the list of choices
        computer_choice = random.choice(choices)

        # Print both the user's and the computer's choices
        print(f"\nYou chose: {user_choice}")
        print(f"The computer chose: {computer_choice}\n")

        # Determine the winner using a series of if/elif/else conditions
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'paper' and computer_choice == 'rock') or \
             (user_choice == 'scissors' and computer_choice == 'paper'):
            print("You win!")
        else:
            print("You lose!")

        # Ask the user if they want to play again
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye.")
            break  # Exit the while loop to end the game

# Call the function to start the game
if __name__ == "__main__":
    play_game()
