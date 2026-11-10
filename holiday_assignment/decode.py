
s = input("Enter the numeric string: ")

decoded = []

def generate(index, path):
    if index == len(s):
        decoded.append(path)
        return

    # Case 1: Take one digit
    if s[index] != '0':
        num = int(s[index])
        ch = chr(64 + num)

        generate(index + 1, path + ch)

    # Case 2: Take two digits
    if index + 1 < len(s) and s[index] != '0':
        num = int(s[index:index + 2])

        if 10 <= num <= 26:
            ch = chr(64 + num)

            generate(index + 2, path + ch)


generate(0, "")

print("Total Ways:", len(decoded))
print("Decoded Strings:")

if len(decoded) == 0:
    print("None")
else:
    for word in decoded:
        print(word)
