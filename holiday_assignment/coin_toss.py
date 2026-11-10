import random

guess = input("Predict Heads or Tails: ").lower()

toss = random.choice(["heads", "tails"])

if guess == toss:
    result = "Correct"
else:
    result = "Wrong"

print("Your Guess:", guess)
print("Coin Toss:", toss)
print("Result:", result)