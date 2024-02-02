import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I have selected a random number between 1 and 100. Try to guess it!")

    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        # Get the player's guess
        guess = int(input("Enter your guess: "))
        attempts += 1

        # Check if the guess is correct
        if guess == secret_number:
            print(f"Congratulations! You guessed the correct number {secret_number} in {attempts} attempts.")
            break
        elif guess < secret_number:
            print("Too low! Try again.")
            # Provide a hint
            if secret_number % 2 == 0:
                print("Hint: The secret number is even.")
            else:
                print("Hint: The secret number is odd.")
            if secret_number % 3 == 0:
                print("Hint: The secret number is divisible by 3.")
            elif secret_number % 5 == 0:
                print("Hint: The secret number is divisible by 5.")
            else:
                print("Hint: The secret number is not divisible by 3 or 5.")
        else:
            print("Too high! Try again.")
            # Provide a hint
            if guess % 2 == 0:
                print("Hint: Your number is even.")
            else:
                print("Hint: Your number is odd.")
            if guess % 3 == 0:
                print("Hint: Your number is divisible by 3.")
            elif guess % 5 == 0:
                print("Hint: Your number is divisible by 5.")
            else:
                print("Hint: Your number is not divisible by 3 or 5.")
            
            # Provide additional hints based on the difference between the guess and the secret number
            difference = abs(secret_number - guess)
            if difference >= 20:
                print("Hint: You are very far from the secret number.")
            elif difference >= 10:
                print("Hint: You are getting closer to the secret number.")
            else:
                print("Hint: You are very close to the secret number.")

if __name__ == "__main__":
    number_guessing_game()
