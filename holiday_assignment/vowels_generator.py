def getvowels(name):
    vowels = "aeiouAEIOU"

    for ch in name:
        if ch in vowels:
            yield ch


name = input("Enter your name: ")

print("Vowels in the name:")

for vowel in getvowels(name):
    print(vowel)