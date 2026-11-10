s = input("Enter the string: ")
sub = input("Enter the substring: ")

start = s.find(sub)

new_sub = ""

for ch in sub:
    if ch == 'a':
        new_sub += 'z'
    else:
        new_sub += chr(ord(ch) - 1)

result = s[:start] + new_sub + s[start + len(sub):]

print("Result:", result)