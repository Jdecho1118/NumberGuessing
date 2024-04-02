import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I have selected a random number between 1 and 100. Try to guess it!")

    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 7  # Maximum number of attempts allowed

    # Provide a hint about the secret number being odd or even
    if secret_number % 2 == 0:
        print("Hint: The secret number is even.")
    else:
        print("Hint: The secret number is odd.")

    while attempts < max_attempts:
        try:
            # Get the player's guess
            guess = int(input("Enter your guess (between 1 and 100): "))
            if guess < 1 or guess > 100:
                raise ValueError("Guess out of range")
        except ValueError:
            print("Invalid input. Please enter a valid number between 1 and 100.")
            continue
        
        attempts += 1

        # Check if the guess is correct
        if guess == secret_number:
            print(f"Congratulations! You guessed the correct number {secret_number} in {attempts} attempts.")
            break
        elif guess < secret_number:
            print("Too low! ")
        else:
            print("Too high! ")
            
        # Provide additional hints based on the difference between the guess and the secret number
        difference = abs(secret_number - guess)
        if difference >= 20:
            print("Hint: You are very far from the secret number.")
        elif difference >= 10:
            print("Hint: You are getting closer to the secret number.")
        else:
            print("Hint: You are very close to the secret number.")

    if attempts >= max_attempts:
        print(f"Sorry, you've run out of attempts. The correct number was {secret_number}.")

if __name__ == "__main__":
    number_guessing_game()
