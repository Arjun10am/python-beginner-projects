import random  # Import random module to let the computer make random choices

choices = ["rock", "paper", "scissor"]  # List of valid choices

user_score = 0  # Initialize user's score
computer_score = 0  # Initialize computer's score

# Loop until either the user or the computer reaches 2 points (best of 3)
while user_score < 2 and computer_score < 2:
    print("\nChoices: rock, paper, or scissor")
    user_choice = input(
        "Enter your Choice: "
    ).lower()  # Take input and convert to lowercase

    # Check if the user's input is valid
    if user_choice not in choices:
        print("Enter a valid choice")
        continue  # Skip the rest of the loop if invalid input

    # Computer randomly selects a choice
    computer_choice = random.choice(choices)
    print("Computer chose:", computer_choice)

    # Check for a draw
    if user_choice == computer_choice:
        print("It's a draw!")

    # Check if the user wins
    elif (
        (user_choice == "rock" and computer_choice == "scissor")
        or (user_choice == "scissor" and computer_choice == "paper")
        or (user_choice == "paper" and computer_choice == "rock")
    ):
        print(" You win this round!")
        user_score += 1  # Increment user's score

    # If not a draw or user win, the computer wins
    else:
        print(" Computer wins this round!")
        computer_score += 1  # Increment computer's score

    # Print the current score after each round
    print(f"Score → You: {user_score} | Computer: {computer_score}")

# Announce the final winner after the loop ends
if user_score > computer_score:
    print("Congratulations! You are the champion!")
else:
    print("Computer wins the game!")
