import random

def numBRange(smaller: int, larger: int) -> None:
    """the range between which the player should choose"""
    print(f"Range is now between {smaller} and {larger}.")

smaller = int(input("Enter the smaller number: "))
larger = int(input("Enter the larger number: "))
myNumber = random.randint(smaller, larger)
mYCount = 0
comPCount = 0
while True:

    userNumber = int(input("Enter your guess: "))
    mYCount += 1
    comPGuess = random.randint(smaller, larger)
    print(f"Computer guesses: {comPGuess}")
    comPCount += 1
    if userNumber < myNumber:
        print("Too small")
        smaller = max(smaller, userNumber + 1)
        numBRange(smaller, larger)

    elif userNumber > myNumber:
        print("Too large")
        larger = min(larger, userNumber - 1)
        numBRange(smaller, larger)

    else:
        print("You've got it in", mYCount, "tries!")
        while True:


            if comp_guess < myNumber:
                print("Computer is too small")
                smaller = max(smaller, comp_guess + 1)
            elif comp_guess > myNumber:
                print("Computer is too large")
                larger = min(larger, comp_guess - 1)
            else:
                print(f"Computer got it in {comPCount} round(s)! Computer wins!")
                break
