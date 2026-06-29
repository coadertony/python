print("hello")
for i in range(1000):
    print(i)
    
    
import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)
attempts = 0

print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100.")

# Loop until the player guesses correctly
while True:
    try:
        # Get input and convert it to an integer
        guess = int(input("Take a guess: "))
        attempts += 1
        
        # Check the user's guess against the secret number
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"🎉 Congratulations! You guessed it in {attempts} attempts!")
            break  # Exit the loop
            
    except ValueError:
        print("Invalid input. Please enter a valid number.")
