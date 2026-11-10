s = input("Enter first string: ")
t = input("Enter second string: ")

if len(s) != len(t):
    print(False)
else:
    frequency = {}

    for ch in s:
        frequency[ch] = frequency.get(ch, 0) + 1

    for ch in t:
        if ch not in frequency or frequency[ch] == 0:
            print(False)
            break

        frequency[ch] -= 1
    else:
        print(True)