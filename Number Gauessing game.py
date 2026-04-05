import random

number = random.randint(1, 100)
guess = None
attempts = 0

print(" Welcome to Number Guessing Game!")

while guess != number:
    guess = int(input("Enter your guess (1-100): "))
    attempts += 1

    if guess < number:
        print("Too Low ⬇️")

    elif guess > number:
        print("Too High ⬆️")
        print(f"congratulations! Total attempts:{attempts}")

    else:
        print("🎉 Correct! You guessed it!")

print("Game Over")
