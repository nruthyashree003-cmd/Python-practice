s = input("Enter a string: ")

letters = ""
digits = ""

for ch in s:
    if ch.isalpha():
        letters += ch
    elif ch.isdigit():
        digits += ch

result = [letters, digits]

print(result)