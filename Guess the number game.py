#import random

def guess_the_number():
    NumberToGuess = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("Thinking of a number between 1 and 100.")

    while True:
        try:
            guess = int(input("Take a guess: "))
            attempts += 1

            if guess < NumberToGuess:
                print("Too low! Try again.")
                print("The number generated is : ",)
            elif guess > NumberToGuess:
                print("Too high! Try again.")
                print("The number generated is : ",)
            else:
                print("Congratulations! You guessed it in {attempts} tries.")
                break
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    guess_the_number()
