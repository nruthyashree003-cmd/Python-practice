
s = input("Enter a string: ")

palindromes = []

for i in range(len(s)):
    for j in range(i, len(s)):

        sub = s[i:j+1]

        if sub == sub[::-1]:
            palindromes.append(sub)

print("Total Count:", len(palindromes))

print("Palindromic Substrings:")

for p in palindromes:
    print(p)
