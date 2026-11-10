cards = input("Enter cards separated by spaces: ").split()

n = len(cards)

ace = 0
face = 0
red = 0
black = 0

for card in cards:

    rank = card[:-1]
    suit = card[-1]

    if rank == "A":
        ace += 1

    if rank in ["J", "Q", "K"]:
        face += 1

    if suit in ["H", "D"]:
        red += 1
    else:
        black += 1

# Calculate probabilities
p_ace = ace / n
p_face = face / n
p_red = red / n
p_black = black / n

print("Ace Probability:", p_ace)
print("Face Card Probability:", p_face)
print("Red Card Probability:", p_red)
print("Black Card Probability:", p_black)

# Find most frequent category
categories = {
    "Ace": ace,
    "Face Card": face,
    "Red Card": red
}

most_frequent = max(categories, key=categories.get)

print("Most Frequent Category:", most_frequent)